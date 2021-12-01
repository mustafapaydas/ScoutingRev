from django.contrib import admin
from .models import Footballer,Comment,Star,Offer
@admin.register(Footballer)
class FootballerAdmin(admin.ModelAdmin):
    list_display = ["isim_soyisim","ulke","nowTakim"]
    search_fields = ["isim_soyisim","nowTakim"]
    list_editable = ["nowTakim"]

    class Meta:
        model=Footballer
admin.site.register(Comment)
admin.site.register(Offer)


@admin.register(Star)
class Star(admin.ModelAdmin):
    class Meta:
        model=Star

