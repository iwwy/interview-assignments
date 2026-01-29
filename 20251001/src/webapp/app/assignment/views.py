from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import ProductSearchForm
from .models import Product


class ProductsView(View):  # type: ignore
    """Products Search View"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """return products data filtered by search form"""
        form = ProductSearchForm(request.GET)
        products = Product.objects.none()
        if form.is_valid():
            products = Product.objects.filter(**form.filters())
        return render(
            request,
            "assignment/products.html",
            {"form": form, "products": products},
        )
