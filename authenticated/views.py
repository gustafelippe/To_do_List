from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error('username', 'Nome de usuário ou senha inválidos.')
                context = {
                    'form': form
                }
                return render(request, 'authenticated/login.html', context)
        
        else:
            context = {
                'form': form
            }
            return render(request, 'authenticated/login.html', context)
    
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request,'authenticated/login.html', context)
    
@login_required(login_url='login_page')

def logout_page(request):
    logout(request)
    return redirect('index')

