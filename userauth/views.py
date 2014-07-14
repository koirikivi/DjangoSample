from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def login_page(request):
    return render(request, "login.html")

@csrf_exempt
def login_ajax(request):
    """A simple view that logs an user in.

    Returns a response with code 200 and the body set to the redirect url on
    success, or a response with code 4XX and the body set to error message on
    error.
    """
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("/blog/")
            else:
                return HttpResponseForbidden("something weird here")
        else:
            return HttpResponseForbidden("wrong pass or username")
    else:
        return HttpResponseBadRequest("Request type must be POST")

def blog(request):
    return render(request, "blog.html")

