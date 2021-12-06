from django.shortcuts import get_object_or_404, render
from .models import Category, Product,Risk

states=["All States-H","Tamil Nadu-H","Andhra Pradesh-H","Assam-M","Bihar-L","Chhattisgarh-L","Goa-M","Gujarat-L","Haryana-M","Himachal Pradesh-L","Jharkhand-L","Karnataka-H","Kerala-H","Madhya Pradesh-L","Maharashtra-M","Meghalaya-L","Odisha-L","Punjab-M","Rajasthan-L","Telangana-M","Uttarakhand-L","Uttar Pradesh-L","West Bengal-M","Chandigarh-L","Delhi-H","Dadra, Nagar Haveli,Daman & Diu-L","Puducherry-H"]
stateName=[]
stateID=[]
for i in states:
    stateName.append(i.split('-')[0])
    stateID.append(i.split('-')[1])
state=zip(states,stateName)

def product_all(request):
    products = Product.products
    typeName="All Collection"
    if request.method=='POST':
        #Risk
        try:
            if(request.POST["btn"]=="low"):
                products=Product.products.filter(risk=1)
                typeName="Low Risk Plants"
            elif(request.POST["btn"]=="moderate"):
                products=Product.products.filter(risk=2)
                typeName="Moderate Risk Plants"
            elif(request.POST["btn"]=="high"):
                products=Product.products.filter(risk=3)
                typeName="High Risk Plants"
            elif(request.POST["btn"]=="all"):
                products = Product.products.all()
                typeName="All Collection"
            elif(request.POST["btn"]=="mlow"):
                products=Product.products.filter(maintenance=1)
                typeName="Low Maintenance Plants"
            elif(request.POST["btn"]=="mmoderate"):
                products=Product.products.filter(maintenance=2)
                typeName="Moderate Maintenance Plants"
            elif(request.POST["btn"]=="mhigh"):
                products=Product.products.filter(maintenance=3)
                typeName="High Maintenance Plants"
            elif(request.POST["btn"]=="offer"):
                products=Product.products.filter(tag="On Offer")
                typeName="On Offer"
            elif(request.POST["btn"]=="new"):
                products=Product.products.filter(tag="New")
                typeName="New"
            elif(request.POST["btn"]=="fast"):
                products=Product.products.filter(tag="Fast Selling")
                typeName="Fast Sellingr"
        except:
            pass
        #Category
        try:
            if(request.POST["cat"]=="1"):
                products=products.filter(category=1)
                typeName="Sedum /Ground Cover"
            elif(request.POST["cat"]=="2"):
                products=products.filter(category=2)
                typeName="Cactus"
            elif(request.POST["cat"]=="3"):
                products=products.filter(category=3)
                typeName="Hanging"
            elif(request.POST["cat"]=="4"):
                products=products.filter(category=4)
                typeName="Aloe"
            elif(request.POST["cat"]=="5"):
                products=products.filter(category=5)
                typeName="Haworthia"
            elif(request.POST["cat"]=="6"):
                products=products.filter(category=6)
                typeName="Other Plants"
            elif(request.POST["cat"]=="7"):
                products=products.filter(category=7)
                typeName="Succulents"
            elif(request.POST["cat"]=="8"):
                products=products.filter(category=8)
                typeName="Jade"
            elif(request.POST["cat"]=="9"):
                products=products.filter(indoor=True)
                typeName="Indoor"
            elif(request.POST["cat"]=="10"):
                products=products.filter(mother=True)
                typeName="Mother Plant"
        except:
            pass
        try:
            val=(request.POST["state"])[-1]
            typeName=(request.POST["state"][:-2])
            if(val=="L"):
                products=Product.products.filter(risk=1)
            elif(val=="M"):
                products=Product.products.exclude(risk=3)
            elif(val=="H"):
                products=Product.products.all()
        except:
            pass
        try:
            val=(request.POST["flt"])
            if(val=="wlow"):
                products=Product.products.filter(Watering=1)
            elif(val=="wnormal"):
                products=Product.products.filter(Watering=2)
            elif(val=="whigh"):
                products=Product.products.filter(Watering=3)
            if(val=="slow"):
                products=Product.products.filter(sun=1)
            elif(val=="snormal"):
                products=Product.products.filter(sun=2)
            elif(val=="shigh"):
                products=Product.products.filter(sun=3)
        except:
            pass
    products=products.order_by('pid')
    state=zip(states,stateName)
    if request.method=='POST':
        #Sort
        try:
            if(request.POST["sort"]=="new"):
                products=products.reverse()
            elif(request.POST["sort"]=="l-h"):
                products=products.order_by('price')
            elif(request.POST["sort"]=="h-l"):
                products=products.order_by('price').reverse()
        except:
            pass
    return render(request, 'store/home.html', {'products': products,'typeName':typeName,'state':state})

def risk_list(request,risk_slug=None):
    risk = get_object_or_404(Risk, slug=risk_slug)
    products = Product.objects.filter(risk=risk)
    return render(request, 'store/products/risk.html', {'risk': risk, 'products': products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})

def index(request):
    state=zip(states,stateName)
    return render(request, 'store/index.html',{'state':state})

def contact(request):
    return render(request, 'store/contact.html')

def faq(request):
    return render(request, 'store/faq.html')

def whatsapp(request):
    return render(request, 'store/whatsapp.html')

def photo(request):
    products = Product.products
    for e in Product.objects.all():
        print(e.title)
    products=products.order_by('pid')
    state=zip(states,stateName)
    return render(request, 'store/photo.html', {'products': products})