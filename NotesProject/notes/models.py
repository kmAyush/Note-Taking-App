from django.db import models

class Note(models.Model): 
	text = models.TextField(max_length = 120)
	created = models.DateTimeField(auto_now = True)