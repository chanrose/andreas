 
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from notekeeper.models import Note
from django.contrib import messages

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'notekeeper/home.html'
    context_object_name = 'all_notes'

    def get_queryset(self):
        return Note.objects.all()[:5]

def create_new_note(request):
    title = request.POST['title']
    all_notes = Note.objects.all()
    already_contain = False
    for note in all_notes:
        if note.title == title:
            already_contain = True
    if already_contain:
        messages.info(request, "Cannot input the same title")
        return HttpResponseRedirect(reverse('notekeeper:index'))
    else:
        new_note = Note(title=title, content=request.POST['content'])
        new_note.save()
        return HttpResponseRedirect(reverse('notekeeper:index'))

class DetailView(generic.DetailView):
    model = Note
    template_name = 'notekeeper/single_note.html'

class EditView(generic.DetailView):
    model = Note
    template_name = 'notekeeper/edit_single_note.html'

def update_note(request, pk):
    note_pk = pk
    title = request.POST['title']
    content = request.POST['content']
    now = timezone.now()
    find_note = Note.objects.get(pk = note_pk)
    find_note.title = title
    find_note.content = content
    find_note.date_update = now
    find_note.save()
    return HttpResponseRedirect(reverse('notekeeper:single_note', args=[note_pk]))

def delete_note(request, note_pk):
    Note.objects.filter(pk=note_pk).delete()
    return HttpResponseRedirect(reverse('notekeeper:index'))
