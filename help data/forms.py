from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

from report.models import Product_Corection, Seller_Corection
from django.forms import ModelChoiceField, ModelMultipleChoiceField

from gharardad.models import Gharardad, SoratKind, AttachKind


class PModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.product_nick_name


class SModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.seller_from_parti


# class GField(ModelMultipleChoiceField):
class GField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.subject


class attachChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.atach_kind


class GharardadForm(forms.Form):
    product = PModelChoiceField(
        widget=forms.Select(
            attrs={
                'placeholder': 'پروژه',
                'class': 'selectpicker mr-sm-2',
                'data-live-search' : "true",
            }),
        queryset=Product_Corection.objects.order_by('product_nick_name').filter(zone__zone_code='406'),
        label='پروژه',
        required=True,
        empty_label='پروژه را انتخاب کنید',
    )

    seller = SModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'طرف قرارداد', 'class': 'selectpicker','data-live-search' : "true",}),
        queryset=Seller_Corection.objects.order_by('seller_from_parti').filter(zone__zone_code='406'),
        label='طرف قرارداد',
        required=True,
        empty_label='طرف قرارداد را انتخاب کنید',
    )

    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'موضوع قرارداد', 'class': 'form-control'}),
        label=' موضوع قرارداد',

    )

    gharardad_no = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'شماره قرارداد', 'class': 'form-control'}),
        label=' شماره قرارداد',

    )
    gharardad_price = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'مبلغ قرارداد', 'class': 'form-control'}),
        label=' مبلغ قرارداد',

    )
    gharardad_date = forms.DateField(
        widget=forms.DateInput(),
    )

    gharardad_end_date = forms.DateField(
        widget=forms.DateInput(),
    )

    is_end = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            # attrs={'class': 'form-control'}
        ),
        label=' تکمیل قرارداد',
    )

    khateme_date = forms.DateField(
        required=False,
        widget=forms.DateInput(),
    )

    def __init__(self, *args, **kwargs):
        super(GharardadForm, self).__init__(*args, **kwargs)
        self.fields['gharardad_date'] = JalaliDateField(
            label=('تاریخ قرارداد'),
            widget=AdminJalaliDateWidget
        )
        self.fields['gharardad_end_date'] = JalaliDateField(
            label=('تاریخ پایان قرارداد'),
            widget=AdminJalaliDateWidget
        )
        self.fields['khateme_date'] = JalaliDateField(
            label=('تاریخ تکمیل قرارداد'),
            required=False,

            widget=AdminJalaliDateWidget
        )


class SoratForm(forms.Form):
    sorat_kind = ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'نوع صورت وضعیت', 'class': 'custom-select mr-sm-2'}),
        queryset=SoratKind.objects.filter(zone__zone_code='406'),
        label='نوع صورت وضعیت',
        required=True,
        empty_label='نوع صورت وضعیت انتخاب کنید',
    )

    sorat_no = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'شماره صورت وضعیت', 'class': 'form-control'}),
        label=' شماره صورت وضعیت',

    )

    peymankar_date = forms.DateField(
        widget=forms.DateInput(),
    )

    moshaver_date = forms.DateField(
        widget=forms.DateInput(),
    )

    karfarma_date = forms.DateField(
        widget=forms.DateInput(),
    )

    peymankar_total_price = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'مبلغ کل پیمانکار', 'class': 'form-control'}),
        label=' مبلغ پیمانکار',
    )

    moshaver_total_price = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'مبلغ کل مشاور', 'class': 'form-control'}),
        label=' مبلغ مشاور',
    )

    moshaver_no = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'شماره نامه مشاور', 'class': 'form-control'}),
        label=' شماره نامه مشاور',
    )


    karfarma_total_price = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'مبلغ کل کارفرما', 'class': 'form-control'}),
        label=' مبلغ کارفرما',
    )

    form_file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            'type': 'file',
            # 'accept':['.pdf','.jpg'],
        }
        ),
        label='اسکن روکش'
    )

    def __init__(self, *args, **kwargs):
        super(SoratForm, self).__init__(*args, **kwargs)
        self.fields['peymankar_date'] = JalaliDateField(
            label=('تاریخ نامه پیمانکار'),
            required=False,
            widget=AdminJalaliDateWidget
        )

        self.fields['moshaver_date'] = JalaliDateField(
            label=('تاریخ نامه مشاور'),
            required=False,
            widget=AdminJalaliDateWidget
        )

        self.fields['karfarma_date'] = JalaliDateField(
            label=('تاریخ تائید کارفرما'),
            required=False,
            widget=AdminJalaliDateWidget
        )


class AttachForm(forms.Form):
    a_kind = ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'نوع پیوست', 'class': 'custom-select mr-sm-2'}),
        queryset=AttachKind.objects.filter(zone__zone_code='406'),
        label='نوع پیوست',
        required=True,
        empty_label='نوع پیوست را انتخاب کنید',
    )

    a_describe = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'توضیحات', 'class': 'form-control'}),
        label='توضیحات',

    )

    a_file = forms.FileField(
        required=True,
        widget=forms.FileInput(attrs={
            'type': 'file',
            # 'accept':['.pdf','.jpg'],
        }
        ),
        label='فایل پیوست'
    )

    a_expire = forms.DateField(
        widget=forms.DateInput(),
    )

    def __init__(self, *args, **kwargs):
        super(AttachForm, self).__init__(*args, **kwargs)
        self.fields['a_expire'] = JalaliDateField(
            label=('تاریخ انقضا'),
            required=False,
            widget=AdminJalaliDateWidget
        )
