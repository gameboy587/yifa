import logging
import json
import pyodbc

from django.shortcuts import render
from django.http import HttpResponse

from lib import xinge

logger = logging.getLogger(__name__)

SECRET_KEY = ''

# Create your views here.
def finish_order(request):
  # Obtain request body and order information
  json_encoded = request.read()
  logger.info('Received RAW json object: ' + json_encoded)

  json_obj = json.loads(json_encoded)
  logger.info('Json object decoded: ' + json_obj)

  order_id = json_obj.orderId
  # TODO: test if it's valid
  logger.info('OrderId: ' + order_id) 
  ############################################################################
  # Make a DB request to get the token
  usr_account = finish_order_db_write(order_id)
  ############################################################################
  # Call Xinge API to push notification to client side
  # Generate title and content
  title = ''
  content = ''
  # Change the accessId, title, content
  push_response = xinge.PushAccountAndroid(
      000, SECRET_KEY, 'title', 'content', usr_account)
  logger.info('Push response' + push_response)
  ############################################################################
  # Return Success message
  response = HttpResponse() # Default status is 200 OK
  return response

def finish_order_db_write(order_id):
  # Modify this
  db = pyodbc.connect('DRIVER={SQL Server};SERVER=10.143.82.133:?;DATABASE=?;UID=sa;PWD=123456 ')
  cursor = db.cursor()
  # Get User ID
  cursor.execute('SELECT userPhone FROM T_Order WHERE orderId=' + order_id)
  user_id = cursor.fetchone()[0]
  # Mark order as finished
  cursor.execute('UPDATE T_Order SET status=2 where orderId=' + order_id)
  db.commit()
  db.close()
  return user_id
