from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_event/', views.create_event, name='create_event'),
    path('update_event/<int:event_id>/', views.update_event, name='update_event'),
    path('event_details/<int:event_id>/', views.event_details, name='event_details'),
    path('available_events/', views.available_events, name='available_events'),
    path('notes/', views.notes, name='notes'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('registered-events/', views.registered_events, name='registered_events'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)