from django.contrib import admin
from .models import Club,CommentClub
@admin.register(Club)
class Club(admin.ModelAdmin):
    list_display = ["takimismi","o","g","b","m","a","y","av","p"]
    list_editable = ["p","o","g","b","m","a","y","av","p"]
    class Meta:
        model=Club


admin.site.register(CommentClub)