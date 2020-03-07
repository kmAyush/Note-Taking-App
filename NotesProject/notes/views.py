from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Note


def index(request):
    noteList = Note.objects.order_by('created')
    template = loader.get_template('notes/note.html')
    context = {'noteList': noteList}
    return render(request, 'notes/note.html', context)
