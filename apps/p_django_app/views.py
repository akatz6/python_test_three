from django.shortcuts import render
from . models import Register
from datetime import date, datetime



# Create your views here.
def index(request):
	return render(request, 'p_django_app/index.html')

def register(request):
	name = request.POST['name']
	alias = request.POST['alias']
	email = request.POST['email']
	password = request.POST['password']
	confirm_password = request.POST['confirm_password']
	bday = request.POST['bday']

	errors = Register.userManager.registeration(name, alias, email, password, confirm_password, bday)

	context = {
	"errors" : errors[1]
	}

	return render(request, 'p_django_app/index.html', context)

def login(request):
	email = request.POST['email']
	password = request.POST['password']
	request.session['email'] = email
	errors = Register.userManager.login(email, password)
	reg = Register.userManager.get_all(email),
	friends = Register.userManager.get_friends(email)
	# count  = Register.userManager.user_poked(request.session['email'])
	# people  = Register.userManager.user_poked_total(request.session['email'])
	
	if errors[0]:
		context = {
		"users" : errors[1],
		"all_users" : reg[0][1],
		"friends": friends[1]
		# "count" : count[1],
		# "peoples" : people[1],
		}
		return render(request, 'second_app/index.html', context)

	context = {
	"errors_login" : errors[1]
	}
	return render(request, 'p_django_app/index.html', context)

def add_friend(request, id):
	friend= Register.userManager.get_friend(id, request.session['email'] )


	user = Register.userManager.get_user(request.session['email'])
	reg = Register.userManager.get_all(request.session['email'])
	friends = Register.userManager.get_friends(request.session['email'])

	print reg
	# friends = Register.userManager.get_friends(email)
	context = {
	"users" : user[1],
	"all_users" : reg[1],
	"friends": friends[1]
	}
	return render(request, 'second_app/index.html', context)

def remove(request, id):
	friend_delete= Register.userManager.remove_friend(id, request.session['email'] )


	user = Register.userManager.get_user(request.session['email'])
	reg = Register.userManager.get_all(request.session['email'])
	friends = Register.userManager.get_friends(request.session['email'])
	print reg[1]
	# friends = Register.userManager.get_friends(email)
	context = {
	"users" : user[1],
	"all_users" : reg[1],
	"friends": friends[1]
	}
	return render(request, 'second_app/index.html', context)

def view(request, id):
	friend = Register.userManager.get_friend_info(id)
	context = {
	"friends": friend[1]
	}
	return render(request, 'p_django_app/info.html', context)

def home(request, id):
	user = Register.userManager.get_user(request.session['email'])
	reg = Register.userManager.get_all(request.session['email'])
	friends = Register.userManager.get_friends(request.session['email'])
	# friends = Register.userManager.get_friends(email)
	context = {
	"users" : user[1],
	"all_users" : reg[1],
	"friends": friends[1]
	}
	return render(request, 'second_app/index.html', context)



