
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request,'loginapp/index.html')

def signup(request):
     if request.method == "POST":
       
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = first_name
        myuser.last_name = last_name

        myuser.save()

        messages.success(request, "Your account has been created successfully..")

        return redirect('signin')
     
     return render(request,'loginapp/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "loginapp/index.html",{'fname': fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
        
    return render(request,'loginapp/signin.html')



def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')
