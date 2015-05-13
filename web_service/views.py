import logging
import json
import mysql.connector

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
    config = {
      'user': 'root',
      'password': '?',
      'host': '10.66.122.203:3306',
      'database': 'orders',
      'raise_on_warnings': True,
    }
    
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    # Get User ID
    cursor.execute('SELECT user_id FROM orders WHERE order_id=' + order_id)
    user_id = [row[0] for row in cursor.fetchall()]
    # Mark order as finished
    cursor.execute('UPDATE orders SET finished=true where order_id=' + order_id)
    db.close()
    return user_id
