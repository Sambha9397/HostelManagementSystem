from django.shortcuts import render,redirect
from hostel.models import SignUp
from hostel.forms import SignUpForm,SharingForm,RoomForm
from hostel.models import SignUp,Sharing,Room
from django.urls import reverse

# Create your views here.
def booking_view(request):
    
    return render(request,'hostel/booking.html')

def base_view(request):
     return render(request,'hostel/base.html')

def home_view(request):
    return render(request,'hostel/home.html')

def facilitys_view(request):
     return render(request,'hostel/facilitys.html')

def schedules_view(request):
     return render(request,"hostel/schedules.html")

def contact_view(request):
     return render(request,"hostel/contact.html")

def main_view(request):
     return render(request,"hostel/main.html")

# Rooms Sherings Views
def twoshering_view(request):
    
    return render(request,"hostel/twoshering.html")

def threeshering_view(request):
    return render(request,"hostel/threeshering.html")

def fourshering_view(request):
    return render(request,"hostel/fourshering.html")

def fiveshering_view(request):
    return render(request,"hostel/fiveshering.html")

def sixshering_view(request):
    return render(request,"hostel/sixshering.html")

def payment_view(request):
    return render(request,"hostel/payment.html")


def register_view(request):
    if request.method=="POST": 
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            email=request.POST.get('email')
            pwd=request.POST.get('pwd')
            if SignUp.objects.filter(email=email,pwd=pwd).exists():
                return redirect('login')
            else:
                form.save(commit=True)
                return redirect('home')
        
    elif request.method=="GET":
        form=SignUpForm()
    return render(request,'hostel/base.html',context={'form':form})    


def login_view(request):
    if request.method=="POST":  
        Email=request.POST.get('email')
        pwd=request.POST.get('password')
        if SignUp.objects.filter(email=Email,pwd=pwd).exists():
            return redirect('home')
        else:
            return render(request,'hostel/base.html')
        
    elif request.method=="GET":
        return render(request,"hostel/base.html")
        



def shering_view(request):
    sharing_obj = Sharing.objects.all()

    sharing_numbers = []
    rents = []

    for i, sharing in enumerate(sharing_obj[:5]):
        sharing_numbers.append(sharing.sharing_number)
        rents.append(sharing.rent)

    context = {
        'sharing1': sharing_numbers[0] if len(sharing_numbers) > 0 else None,
        'sharing2': sharing_numbers[1] if len(sharing_numbers) > 1 else None,
        'sharing3': sharing_numbers[2] if len(sharing_numbers) > 2 else None,
        'sharing4': sharing_numbers[3] if len(sharing_numbers) > 3 else None,
        'sharing5': sharing_numbers[4] if len(sharing_numbers) > 4 else None,

        'rent1': rents[0] if len(rents) > 0 else None,
        'rent2': rents[1] if len(rents) > 1 else None,
        'rent3': rents[2] if len(rents) > 2 else None,
        'rent4': rents[3] if len(rents) > 3 else None,
        'rent5': rents[4] if len(rents) > 4 else None,
    }

    return render(request, 'hostel/shering.html', context)