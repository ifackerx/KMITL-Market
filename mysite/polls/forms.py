from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import forms
from django import forms

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError('%(value)s ไม่ใช่เลขคู่', params={'value' : value})

class PollForm(forms.Form):
    title = forms.CharField(label="ชื่อโพล", max_length=100, required=True)
    email = forms.CharField(validators=[validators.validate_email])
    no_questions = forms.IntegerField(label="จำนวนคำถาม", min_value=0, max_value=10, required=True, validators=[validate_even])
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    def clean_title(self):
        data = self.cleaned_data['title']

        if 'ไอทีหมีแพนด้า' not in data:
            raise forms.ValidationError('คุณลืมชื่อคณะ')
        return data

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if start and not end:
            # raise forms.ValidationError('โปรดเลือกวันที่ส้นสุด')
            self.add_error('end_date', 'โปรดเลือกวันสิ้นสุด')
        elif end and not start:
            # raise forms.ValidationError('โปรดเลือกวันที่เริ่มต้น')
            self.add_error('start_date', 'โปรดเลือกวันที่เริ่มต้น')


def validate_title(value):
    if len(value) > 100:
        raise ValidationError('ตัวอักษรต้องไม่เกิน 100 ตัวอักษร')

def validate_body(value):
    if len(value) > 500:
        raise ValidationError('ตัวอักษรต้องไม่เกิน 500 ตัวอักษร')

def validate_tel(value):
    if len(value) != 10:
        raise ValidationError('ต้องเป็นตัวเลข 10 ตัว')
    if not value.isdigit():
        raise ValidationError('ต้องเป็นตัวเลขทั้งหมด')



class CommentForm(forms.Form):
    title = forms.CharField(validators=[validate_title])
    body = forms.CharField(widget=forms.Textarea, validators=[validate_body])
    email = forms.EmailField(required=False)
    tel = forms.CharField(max_length=10, required=False, validators=[validate_tel])

    def clean(self):
        cleaned_data = super().clean()
        mail = cleaned_data.get('email')
        mobile = cleaned_data.get('tel')

        if not mail and not mobile:
            raise forms.ValidationError('ต้องกรอก email หรือ moblie number')
