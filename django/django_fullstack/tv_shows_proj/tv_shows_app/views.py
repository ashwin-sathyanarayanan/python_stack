from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *

# Create your views here.

def redirect_view(request):
    return redirect('/shows')

def index(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request,'index.html', context)

def new_show(request):
    return render(request,'new_show.html')

def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        new_show = Show.objects.create(title = request.POST['title'],network = request.POST['network'], release_date = request.POST['release_date'], description = request.POST['description'])
    return redirect(f'/shows/{new_show.id}')

def view_show(request,show_id):
    context = {
        'this_show' : Show.objects.get(id=show_id)
    }
    return render(request, 'view_show.html', context)

def edit_show(request,show_id):
    context = {
        'this_show' : Show.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)

def update_show(request,show_id):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{show_id}/edit')
    else:
        this_show = Show.objects.get(id = show_id)
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        print(request.POST['release_date'])
        this_show.release_date = request.POST['release_date']
        this_show.description = request.POST['description']
        this_show.save()
        return redirect(f'/shows/{this_show.id}')

def delete_show(request,show_id):
    this_show = Show.objects.get(id = show_id)
    this_show.delete()
    return redirect('/shows')