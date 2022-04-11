from cgitb import text
import requests

from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def external(request):

	response = requests.get("https://sandbox.api.service.nhs.uk/hello-world/hello/world")

	if response.status_code == 200:
		#return HttpResponse(response.text)
		return render(request, "hello/external.html",{
			"response": response.json()
		})
	else:
		return HttpResponse("Error: invalid status code")