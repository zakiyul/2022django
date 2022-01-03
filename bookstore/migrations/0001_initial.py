# Generated by Django 3.2.9 on 2022-01-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tbl_kategori',
            },
        ),
        migrations.CreateModel(
            name='TokoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('pemilik', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=80)),
                ('no_telp', models.CharField(max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='toko_img/')),
                ('alamat', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_toko',
            },
        ),
        migrations.CreateModel(
            name='ProdukModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('harga', models.FloatField()),
                ('berat', models.FloatField()),
                ('stok', models.IntegerField()),
                ('deskripsi', models.TextField()),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='produk_img/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kategori', models.ManyToManyField(to='bookstore.KategoriModel')),
            ],
            options={
                'db_table': 'tbl_produk',
            },
        ),
    ]
