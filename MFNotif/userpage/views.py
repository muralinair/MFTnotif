from django.shortcuts import render,redirect
#from userpage.forms import UserForm,UserProfileInfoForm
from userpage.forms import UserForm
from userpage.models import UserProfileInfo

def homePage(request):
    return redirect("/login")

def login(request):
    return render(request,"login.html")
def register(request):
    registered=False
    if(request.method == "POST"):
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmPassword=request.POST.get("confirmPassword")
        category=request.POST.get("category")
        if user_form.is_valid():
            newUser=UserProfileInfo.objects.create(username=username,password=password,email=email)
    #if(request.method == "POST"):
    #    user_form=UserForm(data=request.POST)
    #    #profile_form=UserProfileInfoForm(data=request.POST)
    #    if user_form.is_valid():# and profile_form.is_valid():
    #        user=user_form.save()
    #        user.set_password(user.password)
    #        user.save()
    #        #profile=profile_form.save(commit=False)
    #        #profile.user = user
    #        #profile.save()
    #        registered=True
    #    else:
    #        print(user_form.errors)#,profile_form.errors)
    #else:
    #    user_form=UserForm()
    #    #profile_form=UserProfileInfoForm()
    return render(request,"registration.html",{
        'registered':registered,
        'user_form':user_form
        #'profile_form':profile_form
    })
