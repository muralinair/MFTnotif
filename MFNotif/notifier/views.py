from django.shortcuts import render,redirect

def homePage(request):
    return redirect("/login")

def login(request):
    return render(request,"login.html")
def register(request):
    pass

