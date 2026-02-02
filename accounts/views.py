from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('/')
                return redirect('website:index')
            else:
                pass

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    pass

def signup_view(request):
    return render(request, 'accounts/signup.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # return redirect('/')
#             return redirect('website:index')
#         else:
#             pass

#     context = {}
#     return render(request, 'accounts/login.html', context)
