from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from saleor.product.models import Product


class HomePage(Page):

    def serve(self, request, *args, **kwargs):
        return render(request, self.template, {
            'self': self,
        })


class ShopPage(Page):

    def serve(self, request, *args, **kwargs):
        products = Product.objects.get_available_products()[:12]
        products = products.prefetch_related('categories', 'images',
                                         'variants__stock')
        return render(
            request, self.template,
            {
                'self': self,
                'products': products,
                'parent': None
            })


