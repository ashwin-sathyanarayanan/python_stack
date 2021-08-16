from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.register_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(12)).decode()
    new_user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
    #Storing the user's id in the requestion session
    request.session['user_id'] = new_user.id
    return redirect('/success')

def login(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    this_user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = this_user.id
    messages.success(request,"Successfully registered (or logged in)!")
    return redirect('/success')


def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'this_user': User.objects.get(id = request.session['user_id'])
    }
    return render(request,'success.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')