from django.db import models

class KategoriModel(models.Model):
  nama    = models.CharField(max_length=50)

  class Meta:
    db_table = 'tbl_kategori'

  def __str__(self):
    return self.nama

class TokoModel(models.Model):

  nama    = models.CharField(max_length=100)
  pemilik = models.CharField(max_length=100)
  email   = models.CharField(max_length=80)
  no_telp = models.CharField(max_length=50, null=True)
  logo    = models.ImageField(upload_to='toko_img/', null=True, blank=True)
  alamat  = models.TextField(null=True, blank=True)

  class Meta:
    db_table = 'tbl_toko'

  def __str__(self):
    return self.nama

class ProdukModel(models.Model):
  nama = models.CharField(max_length=100)
  harga = models.FloatField()
  berat = models.FloatField()
  stok = models.IntegerField()
  deskripsi = models.TextField()
  gambar = models.ImageField(upload_to='produk_img/', null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  kategori = models.ManyToManyField(KategoriModel)

  class Meta:
    db_table = 'tbl_produk'

  def __str__(self):
    return self.nama


