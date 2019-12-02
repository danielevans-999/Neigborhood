from django.shortcuts import render
from . models import *
from . forms import UpdateProfileForm

def home(request):
    neigborhoods = Neigborhood.objects.all()
    return render(request,'neigborhood/index.html',{'neigborhoods':neigborhoods})

def single_neigborhood(request,id):
    single_hood = Neigborhood.objects.get(pk=id)
    business = single_hood.business_set.all
    post = single_hood.post_set.all
    return render (request, 'neigborhood/neigborhood.html',{'hood':single_hood,'bizz':business,'posts':post})

def profile_info(request):
    
    current_user=request.user
    profile_info = UserProfile.objects.filter(user=current_user).first()
    post =  request.user.post_set.all()
    
    return render(request,'neigborhood/profile.html',{'posts':post,'profile':profile_info,'current_user':current_user})

def update_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    # form = UpdateProfileForm(instance=request.user)
    
    if request.method == "POST":
        form =  UpdateProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user.userprofile)
        return render(request,'neigborhood/update_profile.html', {'form':form})