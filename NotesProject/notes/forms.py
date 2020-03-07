from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
	"""docstring for NoteForm"""
	class Meta:
		model = Note
		fields = {'text'}

	def clean_text(self):
		data = self.cleaned_data['text']
		return data 