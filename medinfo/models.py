from django.db import models

# Create your modelss here.
class Medicine(models.Model):
	name = models.CharField(max_length=40)
	indications = models.CharField(max_length=600, blank=True)
	adult_dose = models.CharField(max_length=200, blank=True)
	child_dose = models.CharField(max_length=200, blank=True)
	renal_dose = models.CharField(max_length=200, blank=True)
	contraindications = models.CharField(max_length=100, blank=True)
	side_effects = models.CharField(max_length=800, blank=True)
	precautions_and_worning = models.CharField(max_length=800, blank=True)
	pregnancy_category = models.CharField(max_length=800, blank=True)
	therapeutic_class = models.CharField(max_length=100, blank=True)
	mode_of_action = models.CharField(max_length=600, blank=True)
	interaction = models.CharField(max_length=800, blank=True)
	pack_size_price = models.CharField(max_length=300, blank=True)

	def __str__(self):
		return self.name