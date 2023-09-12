from django.shortcuts import render,get_object_or_404
from . models import interior,interior1

# Create your views here.

def home(request):
     obj=interior.objects.all()
     obj2=interior1.objects.all()
     return render(request,'index.html',{'data':obj,'data1':obj2})

def about(request):
     return render(request,'about-us.html')

def contact(request):
     return render(request,'contact.html')

def single(request,id):
     obj1=get_object_or_404(interior,pk=id)
     return render(request,'single-post.html',{'obj':obj1})

