from django.shortcuts import redirect, render
from . import models

def index(req):
  return render(req, 'home.html')

def listKategori(req):
  if req.method == 'POST':
    kategori_id = req.POST.get('kategori_id')
    data = models.KategoriModel.objects.get(id=kategori_id)
    data.delete()
    return redirect('/kategori/')

  return render(req, 'kategori/list-kategori.html', context={
    'kategories': models.KategoriModel.objects.all()
  })

def addKategori(req):
  if req.method == 'POST':
    nama  = req.POST.get('nama')

    data = models.KategoriModel()
    data.nama = nama
    data.save()
    return redirect('/kategori/')

  return render(req, 'kategori/add-form.html')

def editKategori(req, id):
  if req.method == 'POST':
    nama = req.POST.get('nama')
    data = models.KategoriModel.objects.get(id=id)
    data.nama = nama
    data.save()
    return redirect('/kategori/')

  return render(req, 'kategori/edit-form.html', context={
    'kategori': models.KategoriModel.objects.get(id=id)
  })


def listToko(req):
  if req.method == 'POST':
    toko_id = req.POST.get('toko_id')
    data = models.TokoModel.objects.get(id=toko_id)
    data.delete()
    return redirect('/toko/')

  return render(req, 'toko/list-toko.html', context={
    'tokos': models.TokoModel.objects.all()
  })

def addToko(req):
  if req.method == 'POST':
    nama    = req.POST.get('nama')
    pemilik = req.POST.get('pemilik')
    email   = req.POST.get('email')
    no_telp = req.POST.get('no_telp')
    logo    = req.FILES.get('logo')
    alamat  = req.POST.get('alamat')

    data = models.TokoModel()
    data.nama     = nama
    data.pemilik  = pemilik
    data.email    = email
    data.no_telp  = no_telp
    data.logo     = logo
    data.alamat   = alamat
    data.save()
    return redirect('/toko/')

  return render(req, 'toko/add-form.html')

def editToko(req, id):
  if req.method == 'POST':
    data = models.TokoModel.objects.get(id=id)

    if req.FILES:
      logo      = req.FILES.get('logo') 
      data.logo = logo

    nama    = req.POST.get('nama')
    pemilik = req.POST.get('pemilik')
    email   = req.POST.get('email')
    no_telp = req.POST.get('no_telp')
    alamat  = req.POST.get('alamat')

    data.nama     = nama
    data.pemilik  = pemilik
    data.email    = email
    data.no_telp  = no_telp
    data.alamat   = alamat
    data.save()
    return redirect('/toko/')

  return render(req, 'toko/edit-form.html', context={
    'toko': models.TokoModel.objects.get(id=id)
  })