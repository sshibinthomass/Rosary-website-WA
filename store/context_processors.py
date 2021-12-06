from .models import Category
from .models import Risk
from .models import Product
from django.db.models import F


def categories(request):
    Product.objects.update(price=F('price'))
    return {
        'categories': Category.objects.all()
    }

def risks(request):
    return {
        'risks': Risk.objects.all()
    }
