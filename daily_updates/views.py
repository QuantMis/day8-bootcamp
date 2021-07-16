from django.shortcuts import render
from user.models import CustomUser
from daily_updates.models import DailyUpdates
from daily_updates.forms import createForm 
from django.shortcuts import render, redirect


def daily_updates_list(request):
    # check role
    print(request.user)
    role = CustomUser.objects.filter(email=request.user)[0].user_type

    # get data updates
    daily_updates = DailyUpdates.objects.all()

    context = {
            "daily_updates": daily_updates,
            "role": role
    }

    return render(request, "daily_updates_list.html", context)

def daily_updates_update(request, pk):
    target_row = DailyUpdates.objects.filter(id=pk)[0]
    form = createForm(instance = target_row)
    context = {
        "form": form
    }

    if request.method == "POST":
        new_update = DailyUpdates.objects.filter(id=pk)[0]
        new_update.title = request.POST["title"]
        new_update.content = request.POST["content"]
        new_update.save()
        return redirect('daily_updates')

    return render(request, "daily_updates_update.html", context)

def daily_updates_new(request):

    form = createForm()
    context = {
        "form": form
    }

    if request.method == "POST":
        new_update = DailyUpdates.objects.create()
        new_update.title = request.POST["title"]
        new_update.content = request.POST["content"]
        new_update.save()
        return redirect('daily_updates')



    return render(request, "daily_updates_new.html", context)

def test(request):
    print("masuk")
