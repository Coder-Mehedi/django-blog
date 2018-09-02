from django.shortcuts import render

# Create your views here.
def bmi(request):
	result = ['','']
	if request.POST:
		height = request.POST['height']
		weight = request.POST['weight']
		height = float(height)
		weight = float(weight)
		mbi=round(weight/(height*height),2)
		
		if mbi < 18.5:
			result = ('Underweight', mbi)
		elif mbi >= 18.5 and mbi <= 23.9:
			result = ['Normal', mbi]
		elif mbi>=24 and mbi<=27.9:
			result = "overweight"
		else:
			result = "obese"
	bmi = {
		'result' : result[0],
		'point' : result[1],
	}
	print(result)
	return render(request, 'bmi/bmi_home.html' , {'bmi': bmi})
