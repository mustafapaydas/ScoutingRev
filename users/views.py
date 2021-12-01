from django.shortcuts import render,redirect
from .forms import kayitForm,Giris
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
def kayit(request):
    if request.method=="POST":
        form=kayitForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data.get("username")
            club=form.cleaned_data.get("club")
            parola=form.cleaned_data.get("password")
            newUser=User(username=username)
            if club == True:
                User.role=club
                newUser.set_password(parola)
                newUser.save()
            else:
                newUser.set_password(parola)
                newUser.save()
            login(request,newUser)
            messages.success(request, "Başarıyla Kayıt Olundu...")
            return redirect("/")
        else:
            form = kayitForm()
            context = {
                "form": form
            }
            messages.success(request,"Kayıt Yapılamadı")
            return render(request, "kayıt.html", context)


    else:
        form=kayitForm()
        context={
            "form":form
        }
        return render(request,"kayıt.html",context)

def giris(request):
    form=Giris(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)

        if user is None:
            messages.warning(request,"Kullanıcı Adı veya Parola Hatalı.")
            return render(request,"giris.html",context)
        messages.success(request,"Başarıyla Giriş Yapıldı.")
        login(request,user)
        return redirect("/")
    else:
        return render(request,"giris.html",context)


def cikis(request):
    logout(request)
    messages.success(request,"Çıkış İşlemi Yapıldı.")
    return redirect("/")
