from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def login_page(request):
    return render(request, "login.html")

@csrf_exempt
def login_ajax(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/blog") #...
            else:
                return HttpResponse("something weird here")
        else:
            return HttpResponse("wrong pass or username")

def blog(request):
    return render(request, "blog.html")

