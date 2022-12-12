from django.contrib import admin
from .models import sanpham, danhmuc, user, giohang, donhang
# Register your models here.
class danhmuc_admin(admin.ModelAdmin):
    list_display = ('id', 'ten')
    search_fields = ['ten']
    list_filter = ['ten']

class sanpham_admin(admin.ModelAdmin):
    list_display = ('id', 'ten', 'mota', 'hinhanh', 'gia', 'danhmuc')
    search_fields = ['ten', 'mota']
    list_filter = ['ten', 'gia']

class user_admin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ['username', 'first_name', 'last_name']
    list_filter = ['username', 'first_name', 'last_name']

class donhang_inline(admin.TabularInline):
    model = donhang

class giohang_admin(admin.ModelAdmin):
    inlines = [donhang_inline]
    list_display = ('id', 'ngaymua', 'trangthai', 'diachi', 'user')
    search_fields = ['ngaymua', 'diachi', 'user']
    list_filter = ['trangthai', 'ngaymua', 'user']


admin.site.register(giohang, giohang_admin)
admin.site.register(user, user_admin)
admin.site.register(danhmuc, danhmuc_admin)
admin.site.register(sanpham, sanpham_admin)