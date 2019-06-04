from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import forms
from django import forms

from .models import UserProfile, Shop


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',

        )

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    choices = forms.ChoiceField(choices=(('01', 'ลูกค้า'), ('02', 'พ่อค้าแม่ค้า')), initial='ลูกค้า', widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
        # widgets = {
        #     'username':
        # }

    def clean_username(self):
        data = self.cleaned_data['username']

        if len(data) < 5 or len(data) > 15:
            raise forms.ValidationError('Username ต้องอยู่ระหว่าง 5-15ตัวอักษร')
        return data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user



class BookingForm(forms.ModelForm):

    shop_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    shop_open = forms.TimeField(label='เวลาเปิดร้าน', widget=forms.TimeInput(format='%H:%M',attrs={'class': 'form-control','placeholder': 'HH:MM'}))
    shop_close = forms.TimeField(label='เวลาปิดร้าน', widget=forms.TimeInput(format='%H:%M',attrs={'class': 'form-control','placeholder': 'HH:MM'}))
    shop_detail = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Shop
        exclude = [
            'shop_area', 'shop_owner', 'shop_booking']

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('shop_open')
        end = cleaned_data.get('shop_close')

        if str(start) > str(end):
            # raise forms.ValidationError('โปรดเลือกวันที่ส้นสุด')
            self.add_error('shop_close', 'เวลาปิดร้านไม่ถูกต้อง')


class ReviewForm(forms.Form):
    review_title = forms.CharField(label="Titile :", max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    review_message = forms.CharField(label="Desicription", max_length=500, required=True, widget=forms.Textarea(attrs={'class':'form-control'}))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']