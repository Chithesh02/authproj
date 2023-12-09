from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# Create your views here.
def home(request):
    return render(request,'home.html')
    
def user_registration(request):
 if request.method=='POST':
      frist_name=request.POST.get('frist_name')
      last_name=request.POST.get('last_name')
      user_name=request.POST.get('user_name')
      email=request.POST.get('email')
      mobile=request.POST.get('mobile')
      password1=request.POST.get('password1')
      password2=request.POST.get('password2')
      print(user_name)
      if password1==password2:
         if User.objects.filter(username=user_name).exists():
            messages.add_message(request,messages.INFO,'user_alreday_taken')
            return redirect('user_registration')
 elif User.objects.filter(email=email).exists():
    messages.info(request,'email already taken')
    return redirect('user_registration')
             
 else:
      user=User.objects.create_user(frist_name=frist_name,
                                    last_name=last_name,
                                    username=user_name,
                                    password=password1,
                                    email=email)
      user.save()
 return redirect('login')
 else:
          return redirect('user_registration')
              return redirect('/')
    else:
             
         return render(request,'user_registration.html')

def login(request):
    if request.method=='POST':
        user_name=request.POST.get('user_name')
        password=request.POST.get('password')
        User=auth(username=user_name,password=password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.add_message(request,messages.INFO,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/') 



