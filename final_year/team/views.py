from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import HttpResponse

# Create your views here.
    #Login required function (decorators function)

@login_required(login_url='signin')


def index(request):
    return render(request, 'index.html')

    #Settings Function
@login_required(login_url='signin') #to change setting first jlog into account

def settings(request):
    # user_profile=Profile.objects.get(user=request.user)
    # if request.method == 'POST':
        
    #     if request.FILES.get('image') == None:
    #         image = user_profile.profileimg   ,{'user_profile': user_profile}
    #         bio = request.POST['bio']
    #         location = request.POST['location']
    #         user_profile.profileimg = image
    #         user_profile.bio=bio
    #         user_profile.location=location
    #         user_profile.save()
            #   if request.FILES.get('image') !=None
            # image = request.FILES.get('image')
            # bio = request.POST['bio']
            # location = request.POST['location']


    return render(request, 'setting.html')



# Signup function

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cnf_password = request.POST['cnf_password']
        if password==cnf_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect ('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect(signup)
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to setting page
                user_login=auth.authenticate(username=username, password=password)
                auth.login(request,user_login)


                #create a profile object for the new user

                user_model = User.objects.get(username=username)
                new_profile= Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')

        else:
            messages.info(request, 'Password not matching')
            return redirect ('signup')

        
    else:  
        return render(request, 'signup.html')
    

    
            # Sign in function

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Wrong Credential')
            return redirect('signin')
    else:
         return render(request, 'signin.html')
    

    #Logout Function

def logout(request):
    auth.logout(request)
    return redirect('signin')
