from django.shortcuts import render, HttpResponse, redirect
from .models import User

from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def regUpdate(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = request.POST["passwordLabel"]
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            name = request.POST["nameLabel"],
            alias = request.POST["aliasLabel"],
            email = request.POST["emailLabel"],
            password = pw_hash
        )
        return redirect("/")

def loginProcess(request):
    user = User.objects.filter(email=request.POST["emailLabel"])
    if len(user) == 0:
        messages.error(request, "please check your email and password")
        return redirect("/")
    if bcrypt.checkpw(request.POST["passwordLabel"].encode(), user[0].password.encode()):
        print("password match")
    else: 
        messages.error(request, "please check your email and password")
    if user:
        logged_user = user[0]

        if bcrypt.checkpw(request.POST["passwordLabel"].encode(), logged_user.password.encode()):
            request.session["userid"] = logged_user.id
            request.session["username"] = logged_user.name
            return render(request, "success.html")

    return redirect("/")

def loggingOut(request):
    request.session.clear()
    return redirect("/")


#Adding a book
def addingBook(request):


    return redirect("add.html")