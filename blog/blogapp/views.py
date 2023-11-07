"""
functions of the blogapp
"""
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, permissions
from blogapp.models import *
from blogapp.serializer import *
from django.db.models import Q

# Create your views here.

class BlogInfoViewSet(viewsets.ModelViewSet):
    queryset=BlogInfo.objects.all()
    serializer_class=BlogInfoSerializer

class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset=ContactInfo.objects.all()
    serializer_class=ContactInfoSerializer
    permission_classes=[permissions.IsAuthenticated]


def index(request):
    """print('hello')"""
    data=BlogInfo.objects.all()
    nontech=BlogInfo.objects.filter(type='nontech')
    techd=data.filter(type='tech')
    return render(request,'blogapp/index.html',{'data':data,'nontech':nontech,'techd':techd})

def search(request):
    query = request.GET.get('query')
    results = []
    print(query)
    print(results)
    if query:
        data=BlogInfo.objects.all()
        results = data.filter(Q(title__icontains=query)| Q(author__icontains=query)|Q (type__iexact=query)| Q(related_to__iexact=query))
    return render(request,'blogapp/search.html',{'results':results})


def about(request):
    return render(request, 'blogapp/aboutus.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ContactInfo.objects.create(name=name,email=email,message=message)
    return render(request, 'blogapp/contactus.html')

def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogInfo, pk=blog_id)
    return render(request, 'blogapp/blog_detail.html', {'blog': blog})

def techpage(request):
    """print('hello')"""
    data=BlogInfo.objects.all()
    posts=data.filter(type='tech')
    type="tech"
    return render(request,'blogapp/specificpage.html',{'posts':posts,'type':type})

def nontechpage(request):
    """print('hello')"""
    posts=BlogInfo.objects.filter(type='nontech')
    return render(request,'blogapp/specificpage.html',{'posts':posts})

