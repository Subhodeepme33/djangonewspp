from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
import app
def home(request):
	return render(request,'login.html')


def signup(request):
	if request.method == 'POST':
		fname= request.POST['fname']
		lname= request.POST['lname']
		uname= request.POST['uname']
		email= request.POST['email']
		passwd= request.POST['passwd']
		confpas= request.POST['confpas']
		if passwd == confpas:
			user=User.objects.create_user(username= uname,first_name=fname,last_name=lname,password=passwd,email=email)
			user.save()
			return render(request,'success.html')

def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	if request.method == 'POST':
		uname=request.POST['uname']
		passwd=request.POST['passwd']
		#Fetching whole users from database
		#user=User.objects.all()
		user=User.objects.filter(username=uname)
		#print(user.values('first_name'))
		error="Invalid Credentials!! Please enter correct details"
		user=auth.authenticate(username=uname,password=passwd)
		if user is not None:
			request.session['user'] = uname 
			request.session['id']=user.id
			request.session['email']=user.email
			return render(request,'homepage.html')
		else:
			return render(request,'login.html',{'err':error})

def logout(request):
    #del request.session['user']
    request.session.flush()
    return render(request,'login.html')
  	#return HttpResponse("You're logged out.")