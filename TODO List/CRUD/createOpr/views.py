from xmlrpc.client import Boolean, boolean

from django.shortcuts import render
from django.http import HttpResponse
from .models import register


def base(request):
    mydata = register.objects.all().values()

    return render(request, "ShowData.html", {'UserData':mydata})

def insertData(request):

    return render(request, "InsertData.html")

def processDataDb(request):
    if request.method == "POST":
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')
        rePassword = request.POST.get('user_rePassword')
        checkBox = boolean(request.POST.get("user_checkBox"))

        saveUser = register.objects.create(name = name, email_id = email, password = password, rePassword = rePassword, isTermsAgree = boolean(checkBox))
        saveUser.save()
        return showDataList(request)
    else:
        return HttpResponse("Invalid Data Transfer")

def showDataList(request):
    mydata = register.objects.all().values()

    return render(request, 'ShowData.html', {'UserData':mydata})

def delete(request):
    mydata = register.objects.all().values()

    return render(request, 'ShowData.html', {'UserData':mydata})

def deleteData(request, id):
    user = register.objects.get(id = id)
    user.delete()

    return delete(request)

def updateData(request, id):
    user = register.objects.get(id=id)

    if request.method == "POST":
        user.name = request.POST.get('user_name')
        user.email_id = request.POST.get('user_email')
        user.password = request.POST.get('user_password')
        user.rePassword = request.POST.get('user_rePassword')
        user.isTermsAgree = Boolean(request.POST.get("user_checkBox"))
        user.save()
        return showDataList(request)

    return render(request, 'UpdateData.html', {'UserData':user})


