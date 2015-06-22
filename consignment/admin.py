from django.contrib import admin

from consignment.models import Seller,Item, Brand

class SellerAdmin(admin.ModelAdmin):
	search_fields=['first_name','last_name','phone_number','email']
	
class ItemAdmin(admin.ModelAdmin):
	list_display = ['item_name','brand_name','status','seller']
	search_fields=['id','seller','brand_name','item_name','description']

class BrandAdmin(admin.ModelAdmin):
	search_fields=['name']

admin.site.register(Seller, SellerAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Item, ItemAdmin)

