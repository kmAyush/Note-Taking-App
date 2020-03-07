from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Note
from .forms import NoteForm

def index(request):
	noteList = Note.objects.order_by('created')
	template = loader.get_template('notes/note.html')
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data['text']
			node = Note(text=data)
			node.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form = NoteForm()
	context = {'noteList':noteList, 'form':form}
	return render(request, 'notes/note.html',context)
