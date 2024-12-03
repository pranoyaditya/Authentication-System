from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages

# Create your views here.
def signUp(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('user_login')
    return render(request, 'user_app/signup.html', {'form':form})

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['username']
            userPass = form.cleaned_data['password']
            user = authenticate(username = userName, password = userPass)
            if user:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('profile')
    return render(request, 'user_app/login.html', {'form' : form})