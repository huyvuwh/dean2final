from rest_framework import serializers
from .models import Store, CustomerGroup, Customer, ProductCategory, Product, Invoice, InvoiceDetail

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['ma_cua_hang', 'doanh_nghiep', 'dia_chi']

class CustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroup
        fields = ['ma_nhom_kh', 'thong_tin_nhom_kh']
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['ma_nhom_hang', 'nhom_hang']

class ProductSerializer(serializers.ModelSerializer):
    ma_nhom_hang = ProductCategorySerializer()
    class Meta:
        model = Product
        fields = ['ma_hang', 'mat_hang', 'dvt', 'don_gia', 'ma_nhom_hang']

class InvoiceDetailSerializer(serializers.ModelSerializer):
    ma_hang = ProductSerializer()  # Serialize the Product model

    class Meta:
        model = InvoiceDetail
        fields = ['ma_hang', 'sl_ban', 'tam_tinh']

class InvoiceSerializer(serializers.ModelSerializer):
    ma_cua_hang = StoreSerializer()  # Serialize the Store model
    ma_kh = CustomerSerializer()  # Serialize the Customer model
    invoicedetail_set = InvoiceDetailSerializer(many=True)  # Serialize InvoiceDetail

    class Meta:
        model = Invoice
        fields = ['ma_hoa_don', 'ma_cua_hang', 'ma_kh', 'nam', 'thang', 'api_code', 'invoicedetail_set']
