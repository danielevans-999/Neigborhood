from django.shortcuts import render,redirect
from . models import *
from . forms import *
from . email import send_welcome_email
from django.contrib.auth.decorators import login_required

def home(request):
    neigborhoods = Neigborhood.objects.all()
    return render(request,'neigborhood/index.html',{'neigborhoods':neigborhoods})

@login_required(login_url='/accounts/login/?next=/')   
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
    
@login_required(login_url='/accounts/login/?next=/')      
def new_post(request,id):
    current_user = request.user
    hood = Neigborhood.objects.get(pk=id)
    if request.method == 'POST':
        form = PostUpload(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.neigborhood = hood
            post.user = current_user
            post.save()
        return redirect('single',hood.id)
    else:
        form = PostUpload()
        return render(request,'neigborhood/new_post.html',{"form":form,"hood":hood})
    
def welcome_email(request):
    
    send_welcome_email(request.user.username, request.user.email)
    
    return render (request,'neigborhood/new_user.html')
    
    