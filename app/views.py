from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from .models import User
# Create your views here.



def index(request):

	news=requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=cca5b584c05b4d4db1143d5837a31a06')
	api=json.loads(news.content)
	return render(request,'index.html',{'api':api})

def show_by_country(request):
	return render(request,'country.html')

def india(request):
	news=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=cca5b584c05b4d4db1143d5837a31a06')
	api=json.loads(news.content)
	return render(request,'country.html',{'api':api})

def usa(request):
	news=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=cca5b584c05b4d4db1143d5837a31a06')
	api=json.loads(news.content)
	return render(request,'country.html',{'api':api})

def newzealand(request):
	news=requests.get('https://newsapi.org/v2/top-headlines?country=nz&apiKey=cca5b584c05b4d4db1143d5837a31a06')
	api=json.loads(news.content)
	return render(request,'country.html',{'api':api})

def australia(request):
	news=requests.get('https://newsapi.org/v2/top-headlines?country=au&apiKey=cca5b584c05b4d4db1143d5837a31a06')
	api=json.loads(news.content)
	return render(request,'country.html',{'api':api})


def blogcount(request):
	email_c=request.session.get('email')
	user=User.objects.filter(email=email_c)

	for x in user:
		x.blogcount+=1
		
	x.save()

	count=user.values('blogcount')
	return render(request,'homepage.html',{'c':count})
	#user=User.model.get()