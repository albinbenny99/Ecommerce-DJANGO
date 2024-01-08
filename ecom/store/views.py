from django.shortcuts import render,get_object_or_404
from .models import product
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.http import HttpResponse


# Create your views here.
def store(request,category_slug=None):
  categories = None
  products = None
  if category_slug!=None:
     categories=get_object_or_404(Category,slug=category_slug)
     products=product.objects.all().filter(category=categories,is_available=True)
     paginator=Paginator(products,1)
     page=request.GET.get('page')
     paged_products = paginator.get_page(page)
     product_count = products.count()
  else:
     products = product.objects.all().filter(is_available="True")
     paginator=Paginator(products,3)
     page=request.GET.get('page')
     paged_products = paginator.get_page(page)
     product_count=products.count()

  context = {
    'products':paged_products ,
     'product_count': product_count,
  }
  return render(request, 'store/store.html',context)

def product_detail(request,category_slug,product_slug):
   try:
      single_product = product.objects.get(category__slug=category_slug,slug=product_slug)
      in_cart= CartItem.objects.filter(cart__cart_id=_cart_id(request),Product=single_product).exists()
      
   except Exception as e:
      raise e
   
   context={
      'single_product': single_product,
      'in_cart': in_cart,
   }

   return render(request, 'store/product_detail.html',context)

def search(request):
   if 'keyword' in request.GET:
      keyword=request.GET['keyword']
      if keyword:
         products=product.objects.order_by('-created_date').filter(description__icontains=keyword)
      
   return render(request, 'store/product_detail.html')
