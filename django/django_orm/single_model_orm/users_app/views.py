from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request,'index.html', context)

def create_user(request):
    new_user = User.objects.create(first_name= request.POST['first_name'], last_name =request.POST['last_name'], email_address = request.POST['email_address'] , age = request.POST['age'])
    return redirect('/')