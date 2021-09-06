from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import * 
# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def store(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitems_set.all()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total': 0}

    context= {'items': items,
        'order':order
    }
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitems_set.all()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total': 0}

    context= {'items': items,
        'order':order
    }
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productID = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductId:', productID)

    customer = request.user.customer
    product = Product.objects.get(id = productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItems.objects.get_or_create(order = order, product = product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)  
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse("Item is added", safe=False)