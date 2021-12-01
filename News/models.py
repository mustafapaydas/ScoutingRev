from django.db import models

class New(models.Model):
    baslik1=models.CharField(max_length=50,verbose_name="Başlık")
    resim1=models.FileField(max_length=25,verbose_name="Haber Resmi")
    yazi=models.TextField(max_length=350,verbose_name="Haber")
    tarih=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Haberler"


