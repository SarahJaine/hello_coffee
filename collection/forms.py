from django.forms import ModelForm 
from collection.models import Shop

class ShopForm(ModelForm): 
	class Meta:
		model = Shop
		fields = ('name', 'description', 'zip_code')