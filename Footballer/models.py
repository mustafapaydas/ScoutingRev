from django.db import models
from django.utils import timezone

from Takım.models import Club


class Footballer(models.Model):
    isim_soyisim=models.CharField(max_length=50,verbose_name="İsim Soyisim")
    dogumYili=models.CharField(max_length=4,verbose_name="Futbolcunun Doğum Yılı")
    ulke=models.CharField(max_length=50,verbose_name="Futbolcunun Uyruğu")
    #nowTakim=models.CharField(max_length=50,verbose_name="Futbolcunun Oynadığı Takım",blank=True,null=True)
    enSonFiyat=models.CharField(max_length=20,verbose_name="Son Satış Bedeli",blank=True,null=True)
    sozlesme_tarihi=models.DateTimeField(auto_created=True,verbose_name="Bonservis Bitiş Tarihi")
    mevki=models.CharField(max_length=50,verbose_name="Oynadığı Mevki")
    ayak = models.CharField(max_length=50,verbose_name="Etkili Ayak")
    nowTakim=models.ForeignKey(Club,on_delete=models.CASCADE)


    image=models.FileField(blank=True,null=True,verbose_name="Fotoğraf ekleme")
    image1=models.FileField(blank=True,null=True,verbose_name="Fotoğraf ekleme")
    image2=models.FileField(blank=True,null=True,verbose_name="Fotoğraf ekleme")
    image3=models.FileField(blank=True,null=True,verbose_name="Fotoğraf ekleme")

    def __str__(self):
         return self.isim_soyisim
    def dogum(self):
        zaman=timezone.now().year
        gercekYas=int(zaman)-int(self.dogumYili)
        return gercekYas



from django.db import models

class Star(models.Model):
    birinci_resim=models.FileField(verbose_name="Birinci Yıldız")
    birinci_isim=models.CharField(max_length=50,verbose_name="İsim")


    ikinci_resim=models.FileField(verbose_name="Birinci Yıldız")
    ikinci_isim=models.CharField(max_length=50,verbose_name="İsim")

    ucuncu_resim=models.FileField(verbose_name="Birinci Yıldız")
    ucuncu_isim=models.CharField(max_length=50,verbose_name="İsim")

    def __str__(self):
        return "Yıldızlar"



class Comment(models.Model):
    futbolcu=models.ForeignKey(Footballer,on_delete=models.CASCADE,verbose_name="Futbolcu",related_name="comments")
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Kullanıcı")
    comment_content=models.TextField(max_length=250,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering=["-comment_date"]


class Offer(models.Model):
    futbolcu=models.ForeignKey(Footballer,on_delete=models.CASCADE,verbose_name="Futbolcu",related_name="offers")

    teklif_eden=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    teklif=models.CharField(max_length=20,verbose_name="Teklif Bedeli")

    def __str__(self):
        return self.teklif