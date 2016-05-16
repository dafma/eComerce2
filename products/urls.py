__author__ = 'mrk2'
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import ProductDetailView, ProductLisView, VariationLisView


urlpatterns = [
    # Examples:
    #url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^$',ProductLisView.as_view(), name='products'),
    url(r'^(?P<pk>\d+)/$',ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/inventory/$',VariationLisView.as_view(), name='product_inventory'),
    #url(r'^(?P<id>\d+)','products.views.product_detail_view_func', name='product_detail_function'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns