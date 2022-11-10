from django.shortcuts import render

# Create your views here.
def addP(request):
    return render(request,'Adminstracion/addPackage.html')