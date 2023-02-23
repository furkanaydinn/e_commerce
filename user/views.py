from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


from user.models import UserProfile
from .forms import SignUpForm



# Create your views here.

@login_required(login_url='/login')
def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.id)
    context = {'profile':profile}

    return render(request, 'user/user_profile.html',context)

def Login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            request.session

            return HttpResponseRedirect('/')

        else:
            messages.warning(request,"Kullanıcı adı veya parola yanlış")
            return HttpResponseRedirect('/login/')

    return render(request, 'user/login.html')


def Log_Out(request):
    logout(request)
    return HttpResponseRedirect('/')


def Sign_Up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')

        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup/')

    form = SignUpForm()
    context = {'form':form}
    
    return render(request,"user/signup.html",context)
