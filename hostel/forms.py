
from django import forms
from hostel.models import SignUp,Sharing,Room
from django import forms
from django.core.validators import RegexValidator

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullname', 'email', 'mob', 'pwd', 'rpwd', 'img', 'doc']


class SharingForm(forms.ModelForm):
    class Meta:
        model=Sharing
        fields="__all__"  

class RoomForm(forms.Form):
    class Meta:
        model=Room
        fields="__all__"
    


    