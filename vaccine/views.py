from django.shortcuts import render
from user.models import CustomUser
from vaccine.models import VaccineStatus 
from vaccine.forms import createForm 

def vaccine_list(request):
    role = CustomUser.objects.filter(email=request.user)[0].user_type
    vaccines = VaccineStatus.objects.all()

    context = {
                "vaccines": vaccines,
                "role": role
            }
    return render(request, "vaccine_list.html", context)

def vaccine_new(request):

    form = createForm()
    context = {
        "form": form
    }

    if request.method == "POST":
        new_update = VaccineStatus.objects.create()

        user = CustomUser.objects.filter(email = request.user)[0]
        new_update.user = user

        new_update.status = request.POST["status"]
        new_update.vtype = request.POST["vtype"]
        new_update.vplace = request.POST["vplace"]
        new_update.save()


    return render(request, "vaccine_new.html", context)

