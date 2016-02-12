from django.shortcuts import render, redirect
from collection.forms import ShopForm
from datetime import date
from collection.models import Shop


# Create your views here.
def index(request):
	#defining a variable
	user_name = 'HERMOINE GRANGER'.lower()
	user_review_num = 9
	today = date(2016,2,10)
	last_post = date(2016,02,14)
	shops = Shop.objects.all()
	shops_20009 = Shop.objects.filter(zip_code='20009').order_by('name')
	shops_name = Shop.objects.filter(name__contains='coffee').order_by('?')
	# this is your new view
	return render(request, 'index.html', {
		'user_name': user_name,
		'user_review_num': user_review_num,
		'today': today,
		'last_post': last_post,
		'shops': shops,
		'shops_20009': shops_20009,
		'shops_name': shops_name,
		})

def shop_detail(request, slug):
	shop = Shop.objects.get(slug=slug)
	return render(request, 'shops/shop_detail.html', {
		'shop': shop,
		})

def edit_shop(request, slug):
	shop = Shop.objects.get(slug=slug)
	form_class = ShopForm
	# if we're coming to this view from a submitted form,
	if request.method == 'POST':
		# grab the data from the submitted form
		form = form_class(data=request.POST, instance=shop) 
		if form.is_valid():
			# save the new data
			form.save()
			return redirect('shop_detail', slug=shop.slug)
	# otherwise just create the form
	else:
		form = form_class(instance=shop)
	# and render the template
	return render(request, 'shops/edit_shop.html', {
		'shop': shop,
		'form': form, 
	})

