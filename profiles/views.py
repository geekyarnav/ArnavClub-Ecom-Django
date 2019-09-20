from django.shortcuts import render
from django.http import HttpResponse
# from .models import BlogArticle
from django.contrib.auth import authenticate,login 


# Create your views here.
def home_view(request):
    context=locals()
    return render(request,"home.html",context)

def about_view(request):
    context=locals()
    return render(request,"about.html",context)

def contact_view(request):
    context=locals()
    return render(request,"contact.html",context)

def services_view(request):
    context=locals()
    return render(request,"services.html",context)

def products_view(request):
    context=locals()
    return render(request,"products.html",context)

#ADD ND SOME MODIFICATION    
#def index(request):
#helps to display string
#return HttpResponse('TEST STRING',)
#render =helps to display the HTML-TEMPLATE

# def blogs_view(request):
#     context=locals()
#     return render(request,"blogs.html",context)  
#     blogs= BlogArticle.objects.all()
#     if request.method=="POST":
#         usname=request.POST['username']
#         pwd=request.POST['password']
#         user=authenticate(username=usname,password=pwd)
#         if user is not None:
#             login(request,user)
#             return render(request,"main.html",{'testvar':"teststring 2",'blogs':blogs,'user':user})
#     return render(request,"main.html",{'testvar':"teststring 2",'blogs':blogs ,'user':None})

# # add blog section
# def createblog(request):
#     newBlog = BlogArticle()
#     newBlog.title = request.POST['TITLE']
#     #newBlog.author = request.user
#     newBlog.blog_content = request.POST['blog_content']
#     newBlog.save()
#     return render(request,"main.html") 

