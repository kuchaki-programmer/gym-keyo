from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, RegisterForm, CheckOtpForm
from django.contrib.auth import login, authenticate, logout
from uuid import uuid4
from random import randint
from django.urls import reverse
from .models import Otp


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:show_home')

        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'account/login.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home:show_home')
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['phone']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:show_home')
            return redirect('account:login')

        return render(request, 'account/login.html', context={'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:show_home')

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            token = str(uuid4())
            code = randint(1000, 9999)
            print(code)
            otp = Otp.objects.create(verification_code=code, token=token, user=user)
            return redirect(reverse('account:check_otp') + f'?token={token}')



        return render(request, 'account/register.html', {'form': form})


class CheckOtp(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/check_otp.html', {'form': form})

    def post(self, request):

        form = CheckOtpForm(request.POST)
        token = (request.POST.get('token'))
        if form.is_valid():
            code = form.cleaned_data['verification_code']
            print(code)
            user_otp = Otp.objects.filter(verification_code=code, token=token).first()
            if user_otp:
                user = user_otp.user  # دسترسی به کاربر مربوطه
                user.is_active = True  # فعال کردن کاربر
                user.save()  # ذخیره کردن تغییرات
                user_otp.delete()
                return redirect('account:login')
            form.add_error('verification_code', 'Wrong!')

        return render(request, 'account/check_otp.html', {'form': form})

