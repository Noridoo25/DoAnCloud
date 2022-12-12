"""shoponline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index),
    path('sanpham/<int:id>/', views.get_sanpham),
    path('danhmuc', views.get_danhmuc),
    path('load', views.ajax_load),
    path('giohang', views.get_cart),
    path('themdonhang', views.add_donhang),
    path('login', views.Login.as_view()),
    path('logout', views.Logout.as_view()),
    path('register', views.Register.as_view()),
    path('giohang/deletedh/<int:id>/', views.deleteDh),
    path('thanhtoan', views.thanhtoan),
    path('person', views.get_all_gh),
    path('person/detail-gh/<int:id>/', views.get_detail_gh)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
