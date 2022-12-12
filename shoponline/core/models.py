from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class user(AbstractUser):
    hinhanh = models.ImageField(upload_to='images', null=False, default=None)

class danhmuc(models.Model):
    ten = models.CharField(max_length=100, null=False)
    def __str__(self):
        return f"{self.id}, {self.ten}"

class sanpham(models.Model):
    ten = models.CharField(max_length=100, null=False)
    mota = models.CharField(max_length=500)
    gia = models.IntegerField(default=None, null=False)
    hinhanh = models.ImageField(upload_to='images', null=False, default=None)
    danhmuc = models.ForeignKey(danhmuc, on_delete=models.CASCADE)
    def __str__(self):
        return f"id : '{self.id}', ten : '{self.ten}'"

class giohang(models.Model):
    ngaymua = models.DateTimeField(auto_now=True)
    trangthai = models.BooleanField(default=False)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    sanphams = models.ManyToManyField(sanpham, related_name= 'sanphams' ,through='donhang')
    diachi = models.CharField(max_length=300, null=True, default=None)
    
class donhang(models.Model):
    sanpham = models.ForeignKey(sanpham, related_name='donhangs', on_delete=models.CASCADE)
    giohang = models.ForeignKey(giohang, related_name='donhangs', on_delete=models.CASCADE)
    soluong = models.IntegerField(default=1, null=False)