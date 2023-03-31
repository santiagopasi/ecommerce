from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            return redirect('user-login')
        else:
            message='There was a problem with the registration, try again.'
            form=CreateUserForm()
            context={
                        'form':form,
                        'message':message,
            }
            return render(request,'user/register.html',context)
            
    else:
        message='There was a problem with the registration, try again.'
        form=CreateUserForm()
        
    context={
        'form':form,
        'message':message,
    }
    return render(request,'user/register.html',context)

def edit_profile(request):
    if request.method == 'POST':
        form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            #get the old image
            old_image = Profile.objects.filter(id = request.user.profile.id)
            #eliminate the old image
            for i in old_image:
                i.image.delete()

            form.save()
            

            

           

            message='User has been updated with succes.'
            
            return redirect('user-profile')
        else:
            print(form.errors)
            message='There was a problem with the data, try again.'
            form=ProfileUpdateForm(instance=request.user.profile)
            context={
                        'form':form,
                        'message':message,
            }
            return render(request,'user/edit_profile.html',context)
            
    else:
     
        form=ProfileUpdateForm(instance=request.user.profile)
      
    context={
        'form':form,
        
    }
    return render(request,'user/edit_profile.html',context)

def profile(request):
 
    return render(request,'user/profile.html')

