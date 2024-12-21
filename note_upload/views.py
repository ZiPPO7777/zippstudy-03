from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def home(request):
    query = request.GET.get('q', '')
    if query:
        notes = Note.objects.filter(title__icontains=query)
    else:
        notes = Note.objects.all()
    return render(request, 'notes_upload/home.html', {'notes': notes, 'query': query})

def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes_upload/upload_note.html', {'form': form})
