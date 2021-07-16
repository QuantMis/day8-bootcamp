from django.shortcuts import render, redirect
from user.models import CustomUser
from vaccine.models import VaccineStatus 
from vaccine.forms import createForm, createForm2 

def vaccine_list(request):
    user = CustomUser.objects.filter(email=request.user)
    role = user[0].user_type
    status = "not_applied"
    if role == "A":
        vaccines = VaccineStatus.objects.all()
        status = "applied"

    else:
        vaccines = VaccineStatus.objects.filter(user=user[0])
        if len(vaccines) >= 1:
            status ="applied"
    

    context = {
                "vaccines": vaccines,
                "role": role,
                "status": status

            }
    return render(request, "vaccine_list.html", context)

def vaccine_new(request):
    user = CustomUser.objects.filter(email=request.user)
    role = user[0].user_type

    if role == "A": 
        form = createForm()
    else: 
        form = createForm2()
    context = {
        "form": form
    }

    if request.method == "POST":
        new_update = VaccineStatus.objects.create()

        user = CustomUser.objects.filter(email = request.user)[0]
        new_update.user = user

        new_update.vtype = request.POST["vtype"]
        new_update.vplace = request.POST["vplace"]
        new_update.save()
        return redirect('vaccine_list')


    return render(request, "vaccine_new.html", context)

def vaccine_approve(request, id):
    vac = VaccineStatus.objects.filter(id=id)[0]
    vac.status = "A"
    vac.save()
    return redirect('vaccine_list')

def vaccine_delete(request, id):
    vac = VaccineStatus.objects.filter(id=id)[0]
    vac.delete()
    return redirect('vaccine_list')

