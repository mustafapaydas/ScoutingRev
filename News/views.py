from django.shortcuts import render
from .models import New
def Haber(request):
    haberler=New.objects.all()
    return render(request,"haberler.html",{"new":haberler})