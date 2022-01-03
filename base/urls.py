from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from bookstore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('kategori/', views.listKategori),
    path('kategori/add/', views.addKategori),
    path('kategori/edit/<int:id>/', views.editKategori),
    path('toko/', views.listToko),
    path('toko/add/', views.addToko),
    path('toko/edit/<int:id>/', views.editToko),
    path('product/', views.listProduct),
    path('product/add/', views.addProduct),
    path('product/edit/<int:id>/', views.editProduct)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
