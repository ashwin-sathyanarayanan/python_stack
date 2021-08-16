from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        if (str.isalpha(postData['first_name']) == False):
            errors["first_name_letters"] = "First Name should only contain letters"
        if len(postData['last_name']) < 2:
            errors["last_name_letters"] = "Last name should be at least 2 characters"
        if (str.isalpha(postData['last_name']) == False):
            errors["last_name"] = "Last Name should only contain letters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if (postData['password'] != postData['confirm_pw']):
            errors["match"] = "The password entered does not match with Confirm Password"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        existing_users = User.objects.filter(email = postData['email'])
        print(existing_users)
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address"
        elif len(existing_users) == 0:
            errors['does_not_exist'] = "User not found."
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        elif not bcrypt.checkpw(postData['password'].encode(), existing_users[0].password.encode()):
            errors["mismatch"] = "Please enter a valid email and password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()