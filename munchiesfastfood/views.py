from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("<h2>G2G<h2>")
# Create your views here.
