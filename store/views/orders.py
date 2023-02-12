from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
<<<<<<< HEAD

class OrderView(View):


=======
from django.contrib.auth.decorators import login_required

class OrderView(View):
    @login_required
>>>>>>> 1cb3347 (Parcheo1S)
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
