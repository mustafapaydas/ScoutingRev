from django.db import models

class Club(models.Model):
    takimismi=models.CharField(max_length=50,verbose_name="Takım")
    bayrak=models.FileField(verbose_name="Takımın Bayrağı")
    o=models.IntegerField(verbose_name="O")
    g=models.IntegerField(verbose_name="G")
    b=models.IntegerField(verbose_name="B")
    m=models.IntegerField(verbose_name="M")
    a=models.IntegerField(verbose_name="A")
    y=models.IntegerField(verbose_name="Y")
    av=models.IntegerField(verbose_name="AV")
    p=models.IntegerField(verbose_name="P")
    class Meta:
        ordering=["-p"]
    def __str__(self):
        return self.takimismi

class CommentClub(models.Model):
    club=models.ForeignKey(Club,on_delete=models.CASCADE,verbose_name="Kulüp",related_name="comments")
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Kullanıcı")
    comment_content=models.TextField(max_length=250,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content
    class Meta:
        ordering=["-comment_date"]
