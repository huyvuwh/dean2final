from django import forms
from .models import Invoice, Customer, Store, InvoiceDetail, Product

class CSVUploadForm(forms.Form):
    file = forms.FileField()

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['ma_cua_hang', 'thang', 'nam']
        widgets = {
            'thang': forms.NumberInput(attrs={'min': 1, 'max': 12}),
            'nam': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        } 

class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['ma_kh', 'ma_cua_hang']  # Danh sách các trường từ mô hình Invoice
        
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['ma_cua_hang', 'ma_kh', 'nam', 'thang']

class InvoiceDetailForm(forms.Form):
    product_ids = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Chọn sản phẩm"
    )
    quantities = forms.CharField(label="Số lượng (vd: 1,2,3)", required=True)
    
    
class UploadFileForm(forms.Form):
    file = forms.FileField()