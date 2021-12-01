from django.shortcuts import render,redirect,get_object_or_404
from .models import Footballer,Comment,Star,Offer
from django.contrib import messages
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth.decorators import login_required
def index(request):

    keyword=request.GET.get("keyword")
    if keyword:
        futbol=Footballer.objects.filter(isim_soyisim__contains=keyword)
        return render(request,"search.html", {"futbol": futbol})
    keyword_mevki=request.GET.get("keyword_mevki")
    if keyword_mevki:
        futbol=Footballer.objects.filter(mevki__contains=keyword_mevki)
        return render(request,"search.html", {"futbol": futbol})

    star = Star.objects.all()
    football=Footballer.objects.all()

    return render(request,"index.html",{"futbol":football,"st":star})
def detail(request,id,):

    futbolcu=Footballer.objects.get(id=id)
    comments = futbolcu.comments.all()
    return render(request, "detail.html", {"fut":futbolcu,"comments":comments})
@login_required(login_url="user:giriş")
def yorumEkle(request,id):
    argo = ["basketbol"] #burada yorumlara küfür edilmesi yasaklanıyor Örnek olarak basketbol girdik
    futbolcu=get_object_or_404(Footballer,id=id)
    if request.method == "POST":
        yazar=request.user
        yorum=request.POST.get("comment_content")
        for i in argo:
            if i in yorum:
                messages.warning(request,"Sakıncalı Eylem {} kelimesinden dolayı uyarıldınız...".format(i))

            else:
                newComment=Comment(author=yazar,comment_content=yorum)
                newComment.futbolcu=futbolcu
                newComment.save()

    return redirect("detail/"+str(id)+"#git")
@login_required(login_url="user:giriş")
def Tekliver(request,id):
    futbolcu=get_object_or_404(Footballer,id=id)

    if request.method == "POST":
        tVeren=request.user
        verilenteklif=request.POST.get("teklif_ver")
        newOffer=Offer(teklif_eden=tVeren,teklif=verilenteklif)
        newOffer.futbolcu=futbolcu
        newOffer.save()
    return redirect("detail/"+str(id))


