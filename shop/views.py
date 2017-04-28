from django.contrib import auth
from django.http import Http404
from django.shortcuts import render, redirect

from shop.models import BasicProductType, ProductType, Product, CartItem, Order


def index(request):
    args = {'username': auth.get_user(request).username}
    return render(request, 'index.html', args)


def categories(request, cat_name):
    if cat_name == 'guitars':
        pattern = "Гитары"
    elif cat_name == 'keyboards':
        pattern = 'Клавишные инструменты'
    elif cat_name == 'drums':
        pattern = 'Ударные инструменты'
    elif cat_name == 'wind':
        pattern = 'Духовые инструменты'
    elif cat_name == 'string':
        pattern = 'Струнные инструменты'
    else:
        raise Http404()

    basic = BasicProductType.objects.filter(name=pattern)
    product_types = ProductType.objects.filter(basic_type=basic)

    args = {'username': auth.get_user(request).username, 'product_types': product_types}
    return render(request, 'categories/categories.html', args)


def products(request, cat_name):
    product_type = ProductType.objects.filter(internal_name=cat_name)
    if len(product_type) == 0:
        raise Http404()
    goods = Product.objects.filter(type=product_type)

    args = {'username': auth.get_user(request).username, 'products': goods, 'cat_name': product_type[0].name}
    return render(request, 'categories/products.html', args)


def concrete_product(request, product_id):
    product = Product.objects.filter(id=product_id)[0]

    if product is None:
        raise Http404()

    args = {'username': auth.get_user(request).username, 'product': product}
    return render(request, 'product.html', args)


def add_to_cart(request):
    product_id = request.POST.get('product_id', '')
    amount = request.POST.get('amount', '')
    item = CartItem(product=Product.objects.get(id=product_id), quantity=amount, owner=auth.get_user(request))
    item.save()
    return redirect('/shop/')


def cart(request):
    user = auth.get_user(request)
    if user.username is '':
        return redirect('/auth/login/')

    cart_items = CartItem.objects.filter(owner=user, is_active=True)

    sum = 0
    for it in cart_items:
        sum += it.product.price * it.quantity

    cart_items = None if len(cart_items) == 0 else cart_items

    args = {'username': user.username, 'cart_items': cart_items, 'sum': sum}
    return render(request, 'cart.html', args)


def plus_quantity(request):
    item_id = request.POST.get('itemId', '')
    item = CartItem.objects.get(id=item_id)
    quantity = item.quantity + 1
    if quantity > item.product.amount:
        return redirect('/shop/cart/')
    item.quantity += 1
    item.save()
    return redirect('/shop/cart/')


def minus_quantity(request):
    item_id = request.POST.get('itemId', '')
    item = CartItem.objects.get(id=item_id)
    quantity = item.quantity - 1
    if quantity < 1:
        return redirect('/shop/cart/')
    item.quantity -= 1
    item.save()
    return redirect('/shop/cart/')


def remove_cart_item(request):
    item_id = request.POST.get('itemId', '')
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('/shop/cart/')


def create_order(request):
    if request.POST:
        items = CartItem.objects.filter(owner=auth.get_user(request), is_active=True)
        order = Order(owner=auth.get_user(request), total=0)
        order.save()

        items_sum = 0
        for item in items:
            item.order = order
            item.is_active = False
            item.product.amount -= item.quantity
            item.product.save()
            item.save()
            items_sum += item.product.price * item.quantity

        order.total = items_sum
        order.save()
    return redirect('/shop/orders/')


def orders(request):
    user = auth.get_user(request)
    if user.username is '':
        return redirect('/auth/login/')

    ords = Order.objects.filter(owner=user)
    ords = None if len(ords) == 0 else ords

    args = {'username': user.username, 'orders': ords}
    return render(request, 'orders.html', args)


def concrete_order(request, order_id):
    user = auth.get_user(request)
    if user.username is '':
        return redirect('/auth/login/')

    order = Order.objects.get(id=order_id)

    if user != order.owner:
        raise Http404()

    items = CartItem.objects.filter(order=order)
    args = {'username': auth.get_user(request).username, 'order': order, 'cart_items': items}

    return render(request, 'order.html', args)


def contacts(request):
    args = {'username': auth.get_user(request).username}
    return render(request, 'contacts.html', args)
