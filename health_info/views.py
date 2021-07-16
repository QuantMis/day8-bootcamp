from django.shortcuts import render
from user.models import CustomUser
from health_info.models import HealthInformation
from health_info.forms import createForm 


def health_info_list(request):
    # check role
    role = CustomUser.objects.filter(email=request.user)[0].user_type

    # get data updates
    if role == "A":
        health_info = HealthInformation.objects.all()
    else:
        target_user = CustomUser.objects.filter(email=request.user)[0]
        health_info = HealthInformation.objects.filter(user = target_user)
    print(role)

    context = {
            "health_info": health_info,
            "role": role
    }

    return render(request, "health_info_list.html", context)

def health_info_update(request, pk):
    target_row = HealthInformation.objects.filter(id=pk)[0]
    form = createForm(instance = target_row)
    context = {
        "form": form
    }

    if request.method == "POST":
        #new_update = DailyUpdates.objects.filter(id=pk)[0]
        #new_update.title = request.POST["title"]
        #new_update.content = request.POST["content"]
        #new_update.save()
        pass

    return render(request, "health_info_updates_new.html", context)
#
#def daily_updates_new(request):
#
#    form = createForm()
#    context = {
#        "form": form
#    }
#
#    if request.method == "POST":
#        new_update = DailyUpdates.objects.create()
#        new_update.title = request.POST["title"]
#        new_update.content = request.POST["content"]
#        new_update.save()
#
#
#    return render(request, "daily_updates_new.html", context)
#
#def test(request):
#    print("masuk") Create your views here.
