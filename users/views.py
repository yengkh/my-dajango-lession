from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')  # Ensure this URL pattern exists
        else:
            print(form.errors)  # Debug: print form errors
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else :
                return redirect('posts:list')  # Ensure this URL pattern exists
        else:
            print(form.errors)  # Debug: print form errors
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('users:login')