from django.contrib import admin
from colorzapp.models import *

class CatagoryAdmin(admin.ModelAdmin):
	catagory_list=["name","image","description","status","trending","created_at"]
	
class ProductAdmin(admin.ModelAdmin):
	product_list=["category","name","vendor","product_image","quantity","original_price","selling_price","description","status","trending","created_at"]

class CartAdmin(admin.ModelAdmin):
	cart_list=["user","product","created_at"]
	
class InfoAdmin(admin.ModelAdmin):
	info=["name","address","mobile"]
	
admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Admin_page,InfoAdmin)


