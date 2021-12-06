from django.shortcuts import get_object_or_404, render
from store.models import Category, Product,Risk
import re
# Create your views here.

def find_val(val):
    val=val.split(',')
    lst=[]
    l1=[]
    plantQua=[]
    plantNam=[]
    plantPhoto=[]
    allplant=[]
    plantPrice=[]
    SNo=[]
    count=1
    plant_after_split=[]
    l1=[]
    for i in val:
        a=re.split('-',i)
        try:
            for j in range(int(a[1])):
                plant_after_split.append(int(a[0]))
        except:
            plant_after_split.append(int(a[0]))
    set_of_plants=set(plant_after_split)
    num=1
    for i in set_of_plants:
      SNo.append(num)
      count1=plant_after_split.count(i)
      plantQua.append(count1)
      num+=1
    lst.append(SNo)
    lst.append(set_of_plants)
    tot=sum(plantQua)
    for j in set_of_plants:
      for i in Product.objects.all():
        if (j == i.pid):
          plantNam.append(i.title)
          plantPhoto.append(i.image.url)
          plantPrice.append(i.price)
          break
    lst.append(plantNam)
    lst.append(plantQua)
    lst.append(plantPhoto)
    lst.append(plantPrice)
    price=0
    for i in range(len(set_of_plants)):
      price+=plantQua[i]*plantPrice[i]
    return zip(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5]), tot, price

def find_valbill(val):
    val=val.split(',')
    lst=[]
    l1=[]
    plantQua=[]
    plantNam=[]
    plantPhoto=[]
    allplant=[]
    plantPrice=[]
    SNo=[]
    risk=[]
    count=1
    plant_after_split=[]
    l1=[]
    for i in val:
        a=re.split('-',i)
        try:
            for j in range(int(a[1])):
                plant_after_split.append(int(a[0]))
        except:
            plant_after_split.append(int(a[0]))
    set_of_plants=set(plant_after_split)
    num=1
    for i in set_of_plants:
      SNo.append(num)
      count1=plant_after_split.count(i)
      plantQua.append(count1)
      num+=1
    lst.append(SNo)
    lst.append(set_of_plants)
    tot=sum(plantQua)
    for j in set_of_plants:
      for i in Product.objects.all():
        if (j == i.pid):
          plantNam.append(i.title)
          plantPhoto.append(i.image.url)
          plantPrice.append(i.price)
          risk.append(i.risk)
          break
    lst.append(plantNam)
    lst.append(plantQua)
    lst.append(plantPhoto)
    lst.append(plantPrice)
    lst.append(risk)
    price=0
    for i in range(len(set_of_plants)):
      price+=plantQua[i]*plantPrice[i]
    return zip(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]), tot, price

def plantfinder(request):
    return render(request,'store/plantfinder.html')

def plantlist(request):
    val=request.POST['plantnumb']
    lst,l2,price=find_valbill(val)
    return render(request,'store/plantlist.html',{'plantID':lst,'l2':l2,'price':price})

def local(request):
  pid=[]
  name=[]
  photo=[]
  ava=[]
  for i in Product.objects.order_by('pid'):
    name.append(i.Nickname)
    pid.append(i.pid)
    photo.append(i.image.url)
    if i.is_active==True:
      val="Available"
    else:
      val="Not Available"
    ava.append(val)
  prod=zip(pid,name,photo,ava)
  typen="All Plants List"
  return render(request,'store/local.html',{'prod':prod,'typen':typen})

def localna(request):
  pid=[]
  name=[]
  photo=[]
  ava=[]
  for i in Product.objects.order_by('pid'):
    if i.is_active==False:
      name.append(i.Nickname)
      pid.append(i.pid)
      photo.append(i.image.url)
      if i.is_active==True:
        val="Available"
      else:
        val="Not Available"
      ava.append(val)
  prod=zip(pid,name,photo,ava)
  typen="Not available plants"
  return render(request,'store/local.html',{'prod':prod,'typen':typen})


def localava(request):
  pid=[]
  name=[]
  photo=[]
  null=[]
  for i in Product.products.order_by('pid'):
    name.append(i.Nickname)
    pid.append(i.pid)
    photo.append(i.image.url)
    null.append("Available")
  prod=zip(pid,name,photo,null)
  typen="Available Plants List"
  return render(request,'store/local.html',{'prod':prod,'typen':typen})

def local_find_val(val):
    val=val.split(',')
    lst=[]
    l1=[]
    plantQua=[]
    plantNam=[]
    plantPhoto=[]
    allplant=[]
    plantPrice=[]
    SNo=[]
    count=1
    plant_after_split=[]
    l1=[]
    for i in val:
        a=re.split('-',i)
        try:
            for j in range(int(a[1])):
                plant_after_split.append(int(a[0]))
        except:
            plant_after_split.append(int(a[0]))
    set_of_plants=set(plant_after_split)
    num=1
    for i in set_of_plants:
      SNo.append(num)
      count1=plant_after_split.count(i)
      plantQua.append(count1)
      num+=1
    lst.append(SNo)
    lst.append(set_of_plants)
    tot=sum(plantQua)
    for j in set_of_plants:
      for i in Product.objects.all():
        if (j == i.pid):
          plantNam.append(i.Nickname)
          plantPhoto.append(i.image.url)
          plantPrice.append(i.price)
          break
    lst.append(plantNam)
    lst.append(plantQua)
    lst.append(plantPhoto)
    lst.append(plantPrice)
    price=0
    for i in range(len(set_of_plants)):
      price+=plantQua[i]*plantPrice[i]
    return zip(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5]), tot, price

def lplantlist(request):
    val=request.POST['plantnumb']
    lst,l2,price=local_find_val(val)
    return render(request,'store/local_plantlist.html',{'plantID':lst,'l2':l2,'price':price})

def lplantfinder(request):
    return render(request,'store/local_plantfinder.html')