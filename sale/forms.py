from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.forms import ModelChoiceField, ModelMultipleChoiceField




class KindeForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'دسته بندی کالا', 'class': 'form-control'}),
        label=' نوع',
    )

    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
        ),
        label=' فعال است؟',
    )



class ProducerForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'نام تولید کننده', 'class': 'form-control'}),
        label='نام تولید کننده',
    )

    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
        ),
        label=' فعال است؟',
    )

    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'آدرس', 'class': 'form-control'}),
        label='آدرس',
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل', 'class': 'form-control'}),
        label='ایمیل',
    )

    phone= forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'تلفن', 'class': 'form-control'}),
        label='تلفن',
    )

