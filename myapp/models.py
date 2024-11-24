from django.db import models


class Store(models.Model):
    ma_cua_hang = models.CharField(max_length=50, primary_key=True)
    doanh_nghiep = models.CharField(max_length=255, blank=True, null=True)
    dia_chi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.doanh_nghiep


class CustomerGroup(models.Model):
    ma_nhom_kh = models.CharField(max_length=50, primary_key=True)
    thong_tin_nhom_kh = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nhom_kh


class Customer(models.Model):
    ma_kh = models.CharField(max_length=50, primary_key=True)
    ma_nhom_kh = models.ForeignKey(CustomerGroup, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.ma_kh
class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    api_code = models.CharField(max_length=100, unique=True) 
    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.customer} - {self.store}"

class ProductCategory(models.Model):
    ma_nhom_hang = models.CharField(max_length=50, primary_key=True)
    nhom_hang = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nhom_hang


class Product(models.Model):
    ma_hang = models.CharField(max_length=50, primary_key=True)
    ma_nhom_hang = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, blank=True, null=True)
    mat_hang = models.CharField(max_length=255, blank=True, null=True)
    dvt = models.CharField(max_length=50, blank=True, null=True)
    don_gia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.mat_hang


class Invoice(models.Model):
    ma_hoa_don = models.CharField(max_length=50, primary_key=True)
    ma_cua_hang = models.ForeignKey(Store, on_delete=models.SET_NULL, blank=True, null=True)
    ma_kh = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    nam = models.IntegerField(blank=True, null=True)
    thang = models.IntegerField(blank=True, null=True)
    api_code = models.CharField(max_length=255, blank=True, null=True) 
    

    def __str__(self):
        return self.ma_hoa_don


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    ma_hang = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    sl_ban = models.IntegerField(blank=True, null=True)
    tam_tinh = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.invoice.ma_hoa_don} - {self.ma_hang.mat_hang}"
