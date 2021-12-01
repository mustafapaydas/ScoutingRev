from django.contrib import admin
from django.urls import path
from Footballer.views import *
from users.views import *
from Takım.views import *
from django.conf import settings
from News.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("clubs/<int:id>",ClubDetail),
    path('detail/<int:id>',detail),
    path("giris", giris,name="giriş"),
    path("club",Takımlar),
    path("kayıt",kayit),
    path("cikis",cikis),
    path("yorum<int:id>",yorumEkle,name="yorums"),
    path("yorumcu<int:id>",CommentClubs,name="coments"),
    path("teklif<int:id>",Tekliver,name="offers"),
    path("haberler",Haber),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
