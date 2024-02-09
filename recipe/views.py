from django.shortcuts import render,redirect
from django.http import HttpResponse
from  django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from recipe.models import RecipeTable
from django.db.models import Q

# Create your views here.
data={}
def register_user(request):
    if request.method=="POST":
        uname=request.POST['username']
        upass=request.POST['password']
        uconf_pass=request.POST['password2']
        if(uname=='' or upass==''or uconf_pass==''):
            data['error_msg']='Fields are empty'
            return render (request,'recipe/register.html',context=data)
        elif(upass!=uconf_pass):
            data['error_msg'] = 'pass is not proper'
            return render (request,'recipe/register.html',context=data)
        elif (User.objects.filter(username=uname).exists()):
            data['error_msg']=uname+ "already exist"
            return render (request,'recipe/register.html',context=data)
        else:
            user=User.objects.create(username=uname)
            user.set_password(upass)
            user.save()
        return HttpResponse("registration done")
    return render (request,'recipe/register.html')
def login_user(request):
    data={}
    if request.method=="POST":
        uname=request.POST['username']
        upass=request.POST['password']
        if(uname=='' or upass==''):
            data['error_msg']='Fields are empty'
            return render (request,'recipe/login.html',context=data)
        elif(not User.objects.filter(username=uname).exists()):
            data['error_msg'] = uname + ' is not registered'
            return render (request,'recipe/login.html',context=data)
        else:
            user=authenticate(username=uname,password=upass)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('/recipe/home')
            else:
                data['error_msg']='wrong pass'
                return render (request,'recipe/login.html',context=data)
    return render(request,'recipe/login.html')

def home(request):
    data={}
    user_authenticated=request.user.is_authenticated
    print(user_authenticated)
    if(user_authenticated):
        user_id=request.user.id 
        user=User.objects.get(id=user_id)
        data['user_data']=user.username
        return render(request,'recipe/home.html',context=data)
    else:
        print['user_data']='User'
        return render(request,'recipe/home.html',{'user':user})
    
def user_logout(request):
    logout(request)
    return render(request,'recipe/home.html',{'user_data':"User"})
    #################################################################################################

   ##################################################################################################3
def index(request):
    data={}
    fetched_products= RecipeTable.objects.filter(is_active=True)
    data['products']=fetched_products
    return render(request,'recipe/index.html',context=data)

####################################################333
def filter_by_category(request,category_value):
    data={}
    q1=Q(is_active=True)
    q2=Q(category=category_value)
    filterd_products=RecipeTable.objects.filter(q1&q2)
    data['products']=filterd_products
    return render ( request,'recipe/index.html',context=data)

  ###  Product.objects.filter(is_active =True,category=category_value)

def sort_by_time(request,sort_value):
    data={}
    if sort_value=='asc':
        time='time'
    else :
        time='-time'
    sort_products=RecipeTable.objects.filter(is_active=True).order_by(time)
    data['products']=sort_products
    return render ( request,'recipe/index.html',context=data)

def filter_by_rating(request,rating_value):
    data={}
    q1=Q(is_active=True)
    q2=Q(rating__gt=rating_value)
    filterd_products=RecipeTable.objects.filter(q1&q2)
    data['products']=filterd_products
    return render ( request,'recipe/index.html',context=data)