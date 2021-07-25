from django.shortcuts import render, HttpResponse

# Create your views here.
def first_route(request):
    return HttpResponse("This is the first route in the first app")

def second_route(request):
    return HttpResponse("This is the second route in the first app")