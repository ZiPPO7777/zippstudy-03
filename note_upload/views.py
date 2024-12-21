# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User  # Import the default User model
from .models import Note
from .forms import NoteForm

def home(request):
    query = request.GET.get('q', '')
    if query:
        notes = Note.objects.filter(title__icontains=query)
    else:
        notes = Note.objects.all()
    return render(request, 'notes_upload/home.html', {'notes': notes, 'query': query})

@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploaded_by = request.user
            note.save()
            messages.success(request, 'Note uploaded successfully!')
            return redirect('dashboard')
    else:
        form = NoteForm()
    return render(request, 'notes_upload/upload_note.html', {'form': form})

@login_required
def dashboard(request):
    user_notes = Note.objects.filter(uploaded_by=request.user)
    total_uploads = user_notes.count()
    recent_uploads = user_notes[:5]  # Get 5 most recent uploads
    
    context = {
        'user_notes': user_notes,
        'total_uploads': total_uploads,
        'recent_uploads': recent_uploads,
    }
    return render(request, 'notes_upload/dashboard.html', context)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, uploaded_by=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('dashboard')
    return render(request, 'notes_upload/delete_confirm.html', {'note': note})