from .models import *
from django.shortcuts import render,redirect,get_object_or_404




from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Club,CommentClub
from django.contrib.auth.decorators import login_required

def Takımlar(request):
    club=Club.objects.all()
    return render(request,"club.html",{"clubs":club})

def ClubDetail(request,id):
    oku = CommentClub.objects.all()
    kulup=Club.objects.filter(id=id)
    return render(request,"clubs.html",{"clubs":kulup,"yorum":oku})
@login_required(login_url="user:giriş")
def CommentClubs(request,id):
    argo = ["basketbol"]  # burada yorumlara küfür edilmesi yasaklanıyor Örnek olarak basketbol girdik
    futbolcu = get_object_or_404(Club, id=id)
    if request.method == "POST":
        yazar = request.user
        yorum = request.POST.get("Yorumumuz")

        if "basketbol" in yorum:
            messages.warning(request, "Sakıncalı Eylem  Tespit Edildi...")

        else:
            newCommentClub = CommentClub(author=yazar, comment_content=yorum)
            newCommentClub.club = futbolcu
            newCommentClub.save()

    return redirect("clubs/" + str(id))

def readComment(request):
    oku=CommentClub.objects.all()
