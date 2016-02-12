from django.contrib import admin

# import your model
from collection.models import Shop

# set up automated slug creation
class ShopAdmin(admin.ModelAdmin): 
	model = Shop
	list_display = ('name', 'description', 'zip_code') 
	prepopulated_fields = {'slug': ('name',)}


# and register it
admin.site.register(Shop, ShopAdmin)