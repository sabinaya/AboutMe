from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('index.html')

def about(request):
	return HttpResponse("<br/> <a href='/website/index'>Back to home page</a>")