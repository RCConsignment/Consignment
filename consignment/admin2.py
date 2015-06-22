from django.contrib import admin

from consignment

models import Seller,ItemStatus,Brand,Item

class Seller(admin.ModelAdmin):
	list_filter=['name']
	search_fields=['first_name','last_name','phone_number','email']
	
	class Item(admin.ModelAdmin):
	
	list_display = ['item_name','brand','status','seller']
	
	list_filter = ['id']
	
	search_fields=['id','seller','brand','item_name','description']
	

	
	class Brand(admin.ModelAdmin):
	
	list_filter = ['name']
	
	search_fields=['name']


	admin.site.register(Seller)

	admin.site.register(ItemStatus)

	admin.site.register(Brand)

	admin.sit