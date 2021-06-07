from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views import View



def user_logout(request):
    logout(request)
    return redirect('login')

class AddUser(View):
    template = 'Dashboard/new_user.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.email = request.POST.get('username')
            user.save()
            return redirect('home')
        messages.success(request, "TroubleTicket Successfully!")
        return render(request,self.template,{'error':"fill data carefully"})

class UpdateUser(View):
    template = 'Dashboard/update_user.html'

    def get(self, request,id):
        user_obj =User.objects.get(id=id)
        return render(request, self.template,{'user_obj':user_obj})
    def post(self,request,id):
        # import pdb
        # pdb.set_trace()
        user_obj = User.objects.get(id=id)
        user_obj.first_name =request.POST.get('first_name')
        user_obj.last_name =request.POST.get('last_name')
        user_obj.email =request.POST.get('username')
        user_obj.username =request.POST.get('username')
        user_obj.mob =request.POST.get('mob')
        if request.FILES.get('profile_pic') is not '' and request.FILES.get('profile_pic'):
            user_obj.profile_pic =request.FILES.get('profile_pic')
        user_obj.save()
        return redirect('home')


def delete_User(request,id):
    user_obj = User.objects.get(id=id)
    user_obj.delete()
    return redirect('home')


class Home(View):
    template = 'Dashboard/home.html'
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('login')
        user_obj = User.objects.filter(is_superuser=False)
        context = {
            'user_obj':user_obj,
        }
        return render(request,self.template, context)
    def post(self,request):
        pass

class LogIn(View):
    template = 'Auth/login.html'
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request,self.template)
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')

        return render(request, self.template,{'error': 'Username or Password are wrong.'})

class Registraion(View):
    template = 'Auth/register.html'

    def get(self,request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, self.template)

    def post(self,request):
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.email = request.POST.get('username')
            user.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, self.template)
        return redirect('home')