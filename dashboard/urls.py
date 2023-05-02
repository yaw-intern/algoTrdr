from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)