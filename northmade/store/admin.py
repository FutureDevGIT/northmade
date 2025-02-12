from django.contrib import admin

from .models import Product, Category, Order, Customer, OrderItem, ShippingAddress, PaymentMethod

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(PaymentMethod)