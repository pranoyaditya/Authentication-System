from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm, UpdateUserForm
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages

# Create your views here.
def signUp(request):
    if request.user.is_authenticated:
        return redirect('profile')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            storage = messages.get_messages(request)
            storage.used = True  # Marks all messages as used

            messages.success(request, 'Account created successfully.')
            return redirect('user_login')
    return render(request, 'user_app/signup.html', {'form':form})

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request=request, data = request.POST)
        if form.is_valid():
            userName = form.cleaned_data['username']
            userPass = form.cleaned_data['password']
            user = authenticate(username = userName, password = userPass)
            if user:
                login(request, user)

                storage = messages.get_messages(request)
                storage.used = True  # Marks all messages as used

                messages.success(request, 'Logged in successfully.')
                return redirect('profile')
    return render(request, 'user_app/login.html', {'form' : form})

@login_required
def user_logout(request):
    logout(request)

    storage = messages.get_messages(request)
    storage.used = True  # Marks all messages as used

    messages.success(request, 'Logged out successfully')
    return redirect('homePage')

@login_required
def profile(request):
    form = UpdateUserForm(instance = request.user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            form.save()

            storage = messages.get_messages(request)
            storage.used = True  # Marks all messages as used

            messages.success(request, 'Updated information successfully.')
    return render(request, 'user_app/profile.html', {'form' : form})

@login_required
def changePassword(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user ,data = request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)

            storage = messages.get_messages(request)
            storage.used = True  # Marks all messages as used

            messages.success(request, 'Password updated successfully')
            return redirect('profile')
    return render(request, 'user_app/password_change.html', {'form' : form, 'type': 'Update'})

@login_required
def resetPassword(request):
    form = SetPasswordForm(request.user)
    if request.method == 'POST':
        form = SetPasswordForm(user = request.user ,data = request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)

            storage = messages.get_messages(request)
            storage.used = True  # Marks all messages as used

            messages.success(request, 'Password updated successfully')
            return redirect('profile')
    return render(request, 'user_app/password_change.html', {'form' : form, 'type': 'Reset'})
