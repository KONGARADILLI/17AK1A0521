from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("<h2 style='color:white; background-color:blue'>Welcome to HomePage</h2>")

def chk(request):
	return HttpResponse("<script>alert('Hi Good Afternoon')</script><h2 style='color:white; background-color:blue'>Welcome</h2>")

def homepage(request):
	return render(request,'htm/homepage.html')

def lgn(re):
	return render(re,'htm/login.html')

def reg(rt):
	return render(rt,'htm/register.html')