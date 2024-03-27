from django.shortcuts import render
from .models import Student

# Create your views here.

def Home(request):
    return render(request,"stdapp/home.html",{})

def std_add(request):

    if request.method=='POST':
        print("Added Student Successfully")

        #retrieve the user inputs
        
       # std_roll=request.POST.get("stdapp_roll")
       # std_name=request.POST.get("stdapp_name")
        #std_email=request.POST.get("stdapp_email")
        #std_contact=request.POST.get("stdapp_contact")
        #std_address=request.POST.get("stdapp_address")
        
        #create an object for model
        #s=Student()
        #s.roll=std_roll
        #s.name=std_name
        #s.email=std_email
        #s.contact=std_contact
        #s.address=std_address


        #s.save()


    return render(request,"stdapp/std_add.html",{})