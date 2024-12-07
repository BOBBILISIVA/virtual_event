from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Event, Note
from .forms import EventForm, NoteForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Replace 'login' with the name of your login URL
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Event

@login_required
def dashboard(request):
    # Corrected query to filter events by the logged-in user
    events = Event.objects.filter(created_by=request.user)
    return render(request, 'dashboard.html', {'events': events})

# Event Management Views
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user  # Assign the logged-in user to the created_by field
            event.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})
@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, created_by=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form, 'event': event})

from datetime import datetime, timedelta
from django.utils.timezone import now, make_aware
from django.contrib import messages

@login_required
def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Combine date and time to create a datetime object
    event_datetime = make_aware(datetime.combine(event.date, event.time))

    # Check if registration is still allowed (30 minutes before event start)
    registration_closed = now() > event_datetime - timedelta(minutes=30)

    # Check if the user is already registered for the event
    is_registered = event.registered_users.filter(id=request.user.id).exists()

    if request.method == 'POST':
        # Handle registration
        if 'register' in request.POST and not registration_closed and not is_registered:
            event.registered_users.add(request.user)
            event.save()
            messages.success(request, "You have successfully registered for the event!")
            return redirect('event_details', event_id=event.id)

        # Handle cancel registration
        if 'cancel_registration' in request.POST and is_registered:
            event.registered_users.remove(request.user)
            event.save()
            messages.success(request, "You have successfully canceled your registration!")
            return redirect('event_details', event_id=event.id)

    return render(request, 'event_details.html', {
        'event': event,
        'registration_closed': registration_closed,
        'is_registered': is_registered,
    })


@login_required
def available_events(request):
    events = Event.objects.all()
    if 'search' in request.GET:
        query = request.GET['search']
        events = events.filter(name__icontains=query)
    return render(request, 'available_events.html', {'events': events})

# Notes Management Views
@login_required
def notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes')
    else:
        form = NoteForm()
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes.html', {'form': form, 'notes': notes})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('notes')
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, created_by=request.user)
    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect('dashboard')
@login_required
def registered_events(request):
    # Fetch all events the user has registered for
    events = request.user.registered_events.all()
    return render(request, 'registered_events.html', {'events': events})
