from django.http import HttpResponse
from django.shortcuts import render
from .models import place,pakages


# Create your views here.
def fun(request):
    psg = pakages.objects.all()
    obj=place.objects.all()
    return render(request,'index.html',{'results':obj,'maxs':psg})

# def addition(request):
#     num1=int(request.POST['num1'])`
#     num2 = int(request.POST['num2'])
#     num3=num1+num2
#     return render(request,'result.html',{'n':num3})