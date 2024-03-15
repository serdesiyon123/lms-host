from django.shortcuts import render, redirect
from .forms import RegisterUsers
from django.contrib.auth import login,logout




def sign_up(request):
    if request.method == 'POST':
        form = RegisterUsers(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    elif request.method == 'GET':
        form = RegisterUsers()

        return render(request, 'registration/signup.html',{'form': form})


def log_out(request):
    logout(request)
    return redirect('/home')

