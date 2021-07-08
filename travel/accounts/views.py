from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('user logged')
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            print('invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST['firstname']
        username= request.POST['username']
        last_name=request.POST['lastname']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is alredy exist!!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is alredy exist!!")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                print("user is created")
                return redirect('/')

        else:
            print("password Uncorrected")
            messages.info(request, "password Uncorrected!!")
            return redirect('register')
    else:
        return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')