from django.shortcuts import render
from datetime import date
from collection.models import Shop


# Create your views here.
def index(request):
	#defining a variable
	user_name = "HERMOINE GRANGER".lower()
	user_review_num = 9
	today = date(2016,2,10)
	last_post = date(2016,02,14)
	shops = Shop.objects.all()
	# this is your new view
	return render(request, 'index.html', {
		'user_name': user_name,
		'user_review_num': user_review_num,
		'today': today,
		'last_post': last_post,
		'shops': shops,
		})

