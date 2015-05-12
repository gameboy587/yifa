from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def confirm_reservation(request):
	# Obtain request body and user information
	
	# Make a DB request to get the token
	# Call Xinge API to push notification to client side
	# Return Success message
    return HttpResponse("Hello, world. You're at the web_service index.")