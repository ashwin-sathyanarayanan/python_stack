from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def num_display(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def destroy(request,number):
    return redirect('/')