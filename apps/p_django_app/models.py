from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import bcrypt
from django.db import models
import re
from django.contrib import messages
from django.db.models import Q
from datetime import date, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class UserManager(models.Manager):
	def registeration(self, name, alias, email, password, confirm_password, bday):
		errors = {}
		if not self.validate_length(name, 'name', 2, 'Name is too short')[0]:
			errors.update(self.validate_length(name, 'name', 2, 'Name is too short')[1])
		if not self.validate_length(alias, 'alias', 2, 'Alias is too short')[0]:
			errors.update( self.validate_length(alias, 'alias', 2, 'Alias is too short')[1])
		if not self.validate_email(email)[0]:
			errors.update( self.validate_email(email)[1])
		if not self.validate_passwords(password, confirm_password)[0]:
			errors.update(self.validate_passwords(password, confirm_password)[1])
		if not self.validate_dob(bday)[0]:
			errors.update(self.validate_dob(bday)[1])

		names=name.split(" ")

		if not errors:
			pw_bytes = password.encode('utf-8')
			hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
			Register.objects.create(first_name = names[0], last_name =names[1], 
			alias = alias, password = hashed, email = email)
			id = Register.objects.latest("created_at")
			for person in Register.objects.all():
				if person.id != id.id:
					Friend.objects.create(user_id = id, is_friend = 0, email = person.email)
					Friend.objects.create(user_id = person, is_friend = 0, email = id.email)				

			success = {}
			success['success'] = "Registeration comeplete, please log in"
			return (True, success)
		else:
			return (False, errors)

	def validate_dob(self, bday):
		date = ""
		try:
			date = datetime.strptime(bday, '%Y-%m-%d')
		except:
			errors = {}
			errors["dob"] = "Date of Birth needs to be in formate mm/dd/yyy"
			return(False, errors)

		if date > datetime.now():
			errors = {}
			errors["dob"] = "You cannot be from the future"
			return(False, errors)
		return (True, "no error")

	def login(self, email, password):
		errors = {}
		valid = True
		try:
			registered = Register.objects.get(email = email)
		except:
			errors['email'] = "Email Not found"
			valid = False

		if(valid):
			pw_bytes = password.encode('utf-8')
			salt = registered.password.encode('utf-8')
			
			if bcrypt.hashpw(pw_bytes, salt) != salt:
				errors['password'] = "Email and password do not match"
				return (False, errors)
			else: 
				return (True, Register.objects.get(email=email))
		else:
			return (False, errors)


	def validate_length(self, test, name, alength, error_string):
		errors = {}
		if len(test) < alength:
			errors[name] = error_string
			return(False, errors)
		return (True, "no error")

	def validate_email(self, email_address):
		errors = {}
		if not EMAIL_REGEX.match(email_address):
			errors['email'] = "Please enter a valid email"
			return(False, errors)
		return (True, "no error")

	def validate_passwords(self, password, confirm_password):
		errors = {}
		if password != confirm_password:
			errors['password'] = "Passwords do not match"
			return(False, errors)
		elif len(password) < 8:
			errors['password'] = "Passwords need to be longer than 8 characters"
			return(False, errors)
		return (True, "no error")


	def get_all(self, email):
		return(True, Friend.objects.filter(email=email, is_friend=0))

	def get_user(self, email):
		return(True, Register.objects.get(email = email))

	def get_friends(self, email):
		return(True, Friend.objects.filter(email=email, is_friend=1))

	def remove_friend(self,id, email):
		user = Register.objects.get(id=id)
		test = Friend.objects.get(user_id = user, email = email)
		test.is_friend = 0
		test.save()

	def get_friend(self, id, email):
		user = Register.objects.get(id=id)
		test = Friend.objects.get(user_id = user, email = email)
		test.is_friend = 1
		test.save()
		return(True)

	def get_friend_info(self, id):
		return(True, Register.objects.get(id=id))


# Create your models here.
class Register(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	alias = models.CharField(max_length=45)
	password = models.TextField(max_length=1000)
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	userManager = UserManager()
	objects = models.Manager()

class Friend(models.Model):
	user_id = models.ForeignKey(Register)
	email = models.EmailField()
	is_friend = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)



