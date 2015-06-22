from django.db import models

class Seller(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	phone_number=models.CharField('phone number', max_length=15)
	address_street = models.CharField(max_length=500)
	address_city = models.CharField(max_length=500)
	address_state = models.CharField(max_length=2)
	address_country = models.CharField(max_length=55)
	email = models.CharField('paypal email', max_length=200)
	active=models.BooleanField('Is Active?')
	def __str__(self):
		return self.first_name + ' ' + self.last_name

class ItemStatus(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name
		
class Brand(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Item(models.Model):
	seller = models.ForeignKey(Seller)
	item_name = models.CharField(max_length=200)
	brand_name = models.ForeignKey(Brand)
	description = models.CharField(max_length=500)
	damages = models.CharField(max_length=1000)
	color = models.CharField(max_length=100)
	num_pieces = models.IntegerField()
	price_1 = models.DecimalField(max_digits=7,decimal_places=2)
	price_2 = models.DecimalField(max_digits=7,decimal_places=2)
	status = models.ForeignKey(ItemStatus)
	def __str__(self):
		return self.item_name



