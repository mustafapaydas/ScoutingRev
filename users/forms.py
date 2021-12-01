from django import forms

class kayitForm(forms.Form):
    # İsim_Soyisim=forms.CharField(max_length=25,label="İsim Soyisim")
    username=forms.CharField(max_length=25,label="Kullanıcı Adı       ")
    password=forms.CharField(max_length=50,label="Parola              ",widget=forms.PasswordInput)
    control=forms.CharField(max_length=50,label="Parolayı Doğrula",widget=forms.PasswordInput)
    # profile_Photo=forms.FileField(label="Resminiz")
    def clean(self):

        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        control=self.cleaned_data.get("control")
        if password and control and password != control:
            raise forms.ValidationError("Parolalar Eşleşmiyor")


        values={
            "username":username,
            "password": password,

        }
        return values

class Giris(forms.Form):
    username=forms.CharField(label="Kullanıcı Adı")
    password=forms.CharField(label="Parola",widget=forms.PasswordInput)

