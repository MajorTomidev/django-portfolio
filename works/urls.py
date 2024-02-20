from django.urls import path
from .views import home_view, work_view

urlpatterns = [
    path('work/<int:work_id>', work_view, name='works'),
    path('', home_view, name='home'),
]