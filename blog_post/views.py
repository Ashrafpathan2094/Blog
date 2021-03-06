from ast import Delete
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from turtle import title
from urllib.request import Request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from  django.contrib import messages
from .models import Post
from datetime import datetime

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):
    
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        
        if password == repeat_password:

            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'Password does not match.Please eneter the same password in both fields')
            return redirect('register')

    else:
        return render(request,'register.html')

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})


def user_profile(request):
    user = User.objects.all()
    username = request.POST['username']
    return render(request, '/user_profile.html', {"user":user},{"username":username})

def del_user(request,username):

    try:
        u = User.objects.get(username = username)
        u.delete()
    except User.DoesNotExist:

        messages.info(request,'User Doesnt Exists')
        return redirect('login')


def upload(request):
    if request.method == 'GET':
        return render(request, 'Upload.html',)
    elif request.method == 'POST':
        Post.author = request.user
        title = request.POST['title']       
        body = request.POST['body']
        post = Post.object.create(title=title,body=body)
        post.save()


        # user = User.objects.all()

        # if request.user.is_authenticated():
        #     post = Post.objects.create(title=request.POST['title'],body=request.POST['body'],author=user, created_at=datetime.utcnow(),)
        #     messages.info(request,'Post uploaded')
        #     return render(request, 'Uplaod.html',)




    return render(request,"upload.html")
     




