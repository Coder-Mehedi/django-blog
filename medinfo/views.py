from django.shortcuts import render
from .models import Medicine
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

# Create your views here.
def med_view(request):
	data = ''
	url = "http://127.0.0.1:8000/medinfo/api/{}"
	if request.method == 'POST':
		name = request.POST['med_name'].lower()
		response = requests.get(url.format(name))
		data = response.json()
	context = {
		'data': data
	}
	return render(request, 'medinfo/medindex.html', context)



class Medicine_view(APIView):
    def get(self, request, name):
        med = Medicine.objects.get(name=name)
        medicine_name = med.name
        indications = med.indications
        child_dose = med.child_dose
        adult_dose = med.adult_dose
        renal_dose = med.renal_dose
        contraindications = med.contraindications
        side_effects = med.side_effects
        precautions_and_worning = med.precautions_and_worning
        pregnancy_category = med.pregnancy_category
        therapeutic_class = med.therapeutic_class
        mode_of_action = med.mode_of_action
        interaction = med.interaction
        pack_size_price = med.pack_size_price

        return Response({
        	'name': 		medicine_name,
        	'indications':   	indications,
        	'child_dose':   child_dose,
        	'adult_dose':	adult_dose,
        	'renal_dose':	renal_dose,
        	'contraindications': contraindications,
        	'side_effects': side_effects,
        	'precautions_and_worning' : precautions_and_worning,
        	'pregnancy_category': pregnancy_category,
        	'therapeutic_class' :therapeutic_class,
        	'mode_of_action':	mode_of_action,
        	'interaction':	interaction,
        	'pack_size_price': pack_size_price
        	})