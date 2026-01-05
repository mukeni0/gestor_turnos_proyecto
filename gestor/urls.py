from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.turnos_lista, name='lista'),
    path('turno/<int:turno_id>/', views.detalle_turno, name='detalle_turno'),
    path('turno/create/', views.aniadir_turno, name='aniadir_turno'),
    path('turno/<int:turno_id>/delete/', views.eliminar_turno, name='eliminar_turno'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
