from django.contrib import admin
from .models import Contact,User,Product,Whishlist,Cart,Transaction
# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Whishlist)
admin.site.register(Cart)
admin.site.register(Transaction)