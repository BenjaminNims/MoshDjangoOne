from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product


def say_hello(request):

    queryset = Product.objects.prefetch_related(
        'promotions').select_related('collection').all()

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
