from django.shortcuts import render
from .models import Medicine

# Create your views here.
def med_view(request):
	name = ''
	medi = Medicine.objects.all()
	# aa = Medicine.objects.get(name=name)
	print(medi)
	if request.POST:
		name = request.POST['med_name']

	context = {
		'name': name
	}

	return render(request, "medinfo/med_home.html", context)