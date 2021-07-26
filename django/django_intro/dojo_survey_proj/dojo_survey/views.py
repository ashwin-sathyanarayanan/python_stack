from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    context = {

    }
    return render(request,'index.html', context)

def process(request):
    if (request.method != "POST"):
        return redirect('/')
    request.session['name'] = request.POST['name']
    request.session['locations'] = request.POST['locations']
    request.session['languages'] = request.POST['languages']
    request.session['comment'] = request.POST['comment']
    return redirect('/results')

def results(request):
    return render(request, 'result.html')

def back(request):
    request.session.flush()
    return redirect('/')
