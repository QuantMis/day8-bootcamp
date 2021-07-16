from django.shortcuts import render
from user.models import CustomUser
from .models import Premise, MockScanEvent 
from .forms import createForm, createForm2 
import requests, json

from django.shortcuts import render, redirect

# Create your views here.
def premise_list(request):
    # check role
    user = CustomUser.objects.filter(email=request.user)
    role = user[0].user_type

    if role == "A":
        premises = Premise.objects.all()
    else:
        premises = Premise.objects.filter(user=user[0])

    context = {
            "premises": premises,
            "role": role
    }

    return render(request, "premise_list.html", context)

def premise_activity(request):

    res = []
    premises = Premise.objects.all()
    for i in premises:
        temp = {"premise": i.premise_name} 
        me = MockScanEvent.objects.filter(premise=i)
        temp["scanEvent"] = me
        res.append(temp)
    context = {
            "data": res
    }
    print(res)
        
    return render(request, "premise_activity.html", context)



def premise_new(request):

    form = createForm()
    context = {
        "form": form
    }

    user = CustomUser.objects.filter(email=request.user)

    if request.method == "POST":
        new_premise = Premise.objects.create()
        new_premise.user = user[0]
        new_premise.premise_name = request.POST["premise_name"]
        new_premise.premise_address = request.POST["premise_address"]
        new_premise.save()

        return redirect('premise_list')

    return render(request, "premise_new.html", context)

def mock_scan(request):

    user = CustomUser.objects.filter(email=request.user)
    form = createForm2()
    context = {
        "form": form
    }

    if request.method == "POST":
        scan = MockScanEvent.objects.create()
        
        premise = Premise.objects.filter(id=request.POST["premise"])

        scan.user  = user[0]
        scan.premise = premise[0] 

        # ip function
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        res = requests.get('http://ip-api.com/json/' +ip_data["ip"])  # data from json
        location_data_one = res.text
        # convert jason to python dictionary
        location_data = json.loads(location_data_one)

        scan.latitude = location_data['lat']
        scan.longitude =  location_data['lon']
        scan.save()
        
    return render(request, "scan_qr.html", context)


    





