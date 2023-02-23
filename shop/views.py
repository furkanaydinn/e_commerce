from django.shortcuts import render, get_object_or_404
from .models import Product,Category,Comment
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

def Shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    category_count = Category.objects.annotate(items_count = Count('product_categories',distinct=True))

    paginator = Paginator(products,per_page = 3)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    context = {
               'products':page_obj.object_list,
               'paginator':paginator,
               'page_number':int(page_number),
               'categories':categories,
               'category_count':category_count
               }

    return render(request,'store/store.html', context)





