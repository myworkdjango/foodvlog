from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth



def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        psw = request.POST['psw']
        psw2 = request.POST['psw-repeat']
        if psw==psw2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=psw)
                user.save()
        else:
            print("no matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['psw']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    return render(request, 'login.html')

# Create your views here.
