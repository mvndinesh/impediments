from django.shortcuts import render, redirect,reverse
from .models import List,ListAllDefects
from .forms import ListForm,ListDefectForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from datetime import datetime
from django.http import Http404
import smtplib, ssl
from email.message import EmailMessage
import os

# Create your views here.
 
def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		# if form.is_valid():
		# 	form.save
		# 	all_items = List.objects.all
		# 	context = {'all_items' : all_items}
		# 	return render(request,'home.html',context)
		form.save()
		all_items = List.objects.all
		context = {'all_items' : all_items}
		messages.success(request,("Item has been added to List!"))
		return render(request,'home.html',context)
	else:
		all_items = List.objects.all
		context = {'all_items' : all_items}
		return render(request,'home.html',context)

def about(request):
	context = {'firstname':'dinesh','lastname':'maddisetty'}
	return render(request,'about.html',context)

def delete(request,list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,("Item has been deleted"))
	#return HttpResponseRedirect(reverse('home'))
	#return HttpResponseRedirect("/")
	return redirect('/') # Another way of redirecting the page to the home page.
	#return HttpResponseRedirect("http://example.com/")

def cross_off(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return HttpResponseRedirect("/") # Another way of redirecting the page to the home page.
	#return redirect('home')

def uncross(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return HttpResponseRedirect("/")
	#return redirect('home')

def edit(request,list_id):
	if request.session['validated'] != True:
		del request.session
		raise Http404('Unauthorized Access') 
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None,instance = item)
		# if form.is_valid():
		# 	form.save
		# 	all_items = List.objects.all
		# 	context = {'all_items' : all_items}
		# 	return render(request,'home.html',context)
		if form.is_valid():
			form.save()
			messages.success(request,("Item has been edited to List!"))
			return redirect('/')
	else:
		item = List.objects.get(pk=list_id)
		context = {'item' : item}
		return render(request,'edit.html',context)

def alldefects(request):
	if request.session['validated'] == True:
		# all_items = ListAllDefects.objects.all().order_by('-createddate')
		# context = {'all_items' : all_items}
		# context["all_items_count"] = len(all_items)
		# print(len(all_items))
		context = contextalldefects()
		return render(request,'alldefects.html',context)
	else:
		del request.session["validated"]
		raise Http404('Unauthorized Access')


def contextalldefects():
	all_items = ListAllDefects.objects.all().order_by('-createddate')
	context = {'all_items' : all_items}
	context["all_items_count"] = len(all_items)
	return context


def showdefect(request):
	if request.session['validated'] == True:
		all_items = ListAllDefects.objects.all
		context = {'all_items' : all_items}
		return render(request,'enterdefect.html',context)
	else:
		raise Http404('Unauthorized Access') 

def enterdefect(request):
	if request.session['validated'] != True:
		del request.session
		raise Http404('Unauthorized Access') 

	if request.method == 'POST':
		form = ListDefectForm(request.POST or None)
		form.save()
		context = contextalldefects()
		messages.success(request,("Defect has been added to the Defect List!"))
		return render(request,'alldefects.html',context)
	else:
		context = {}
		datetoday = datetime.today().strftime('%m-%d-%Y')
		print(datetoday)
		context['datetoday'] = datetoday
		context['originator'] = request.session["firstname"]
		context['orgemailid'] = request.session["useremailid"]
		# context = {'datetoday':datetoday,'name'}
		return render(request,'enterdefect.html',context)

def editdefect(request,list_id):
	if request.session['validated'] != True:
		del request.session
		raise Http404('Unauthorized Access') 
	if request.method == 'POST':
		item = ListAllDefects.objects.get(pk=list_id)
		form = ListDefectForm(request.POST or None,instance = item)
		if form.is_valid():
			form.save()
			# if request.POST.get("status") == "Done":

			context = contextalldefects()
			return render(request,'alldefects.html',context)
			alldefects(request)
	else:
		item = ListAllDefects.objects.get(pk=list_id)
		context = {'edit' : item}
		return render(request,'editdefect.html',context)

def selection(request):
	all_items = ListAllDefects.objects.all
	context = {'all_items' : all_items}
	print(context)
	if request.session['validated'] == True:
		return render(request,'selection.html',context)
	else:
		raise Http404('Unauthorized Access') # To see the error set Debug = True in settings app

def alldefectscss(request):
	all_items = ListAllDefects.objects.all()
	context = {'all_items' : all_items}
	context["all_items_count"] = len(all_items)
	print(len(all_items))
	return render(request,'index.html',context)

def sendmail(request):
	if request.session['validated'] != True:
		del request.session
		raise Http404('Unauthorized Access') 

	if request.method == 'POST':

		port = 465  # For SSL
		smtp_server = "smtp.gmail.com"
		sender_email = "ourimpediments@gmail.com"  # Enter your address
		receiver_email = request.POST.get("emailto")  # Enter receiver address
		password = "ourimp123"
		# message = 'Subject: Test message\n'+'Body would go here\n'
		message = 'Subject: '+request.POST.get("emailsubject")+'\n'+request.POST.get("emailbody")+'\n'
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message)

		context1 = {}
		messages.success(request,("Mail has been sent successfully"))
		return render(request,'sendmail.html',context1)

	else:
		context1 = {}
		return render(request,'sendmail.html',context1)


def sendmaillid(request,list_id):
	if request.session['validated'] != True:
		del request.session
		raise Http404('Unauthorized Access') 
	if request.method == 'POST':

		port = 465  # For SSL
		smtp_server = "smtp.gmail.com"
		sender_email = "ourimpediments@gmail.com"  # Enter your address
		receiver_email = request.POST.get("emailto")  # Enter receiver address
		password = "ourimp123"
		# message = 'Subject: Test message\n'+'Body would go here\n'
		message = 'Subject: '+request.POST.get("emailsubject")+'\n'+request.POST.get("emailbody")+'\n'
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message)

		context1 = {}
		messages.success(request,("Mail has been sent successfully"))
		return render(request,'sendmail.html',context1)

	else:
		
		item = ListAllDefects.objects.get(pk=list_id)
		context = {'edit': item}
		return render(request,'sendmail.html',context)

def login(request):
	request.session['validated'] = False
	if request.method == 'POST':
		user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
		if user is not None:
			context = {"username":request.POST.get("username")}
			validated = True
			request.session["validated"] = True
			request.session["useremailid"] = user.email
			request.session["firstname"] = user.first_name
			context["uemailid"] = user.email

			print(user.email)
			return render(request,'selection.html',context)
		else:
			raise Http404('Please check you credentials') 
	else:
		context = {"username":"","password":""}
		return render(request,'login.html',context)

def logout_view(request):
	# del request.session["validated"]
	logout(request) 
	context = {"username":"","password":""}
	return render(request,'loggedout.html',context)
	del request.session["validated"]
	


def loggedout(request):
	# del request.session["validated"]
	context = {"username":"","password":""}
	return render(request,'loggedout.html',context)


	
	





