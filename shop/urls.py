from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^categories/(?P<cat_name>\w+)$', views.categories, name='categories'),
    url(r'^product/(?P<product_id>\w+)$', views.concrete_product, name='product'),
    url(r'^products/(?P<cat_name>\w+)$', views.products, name='products'),
    url(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart'),
    url(r'^remove_item/$', views.remove_cart_item, name='remove_cart_item'),
    url(r'^create_order/$', views.create_order, name='create_order'),
    url(r'^orders/$', views.orders, name='orders'),
    url(r'^order/(?P<order_id>\w+)$', views.concrete_order, name='order'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^plus/$', views.plus_quantity, name='plus'),
    url(r'^minus/$', views.minus_quantity, name='minus'),
    url(r'^$', views.index, name='index'),
]
