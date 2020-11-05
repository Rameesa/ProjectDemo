from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Welcome")
def fn_new(request):
	return render(request,'new.html')