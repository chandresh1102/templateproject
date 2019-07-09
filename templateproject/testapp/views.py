from django.shortcuts import render
import datetime

# Create your views here.
def tempview(request):
	date=datetime.datetime.now()
	d={'time':date}
	return render(request,'testapp/wish.html',context=d)
