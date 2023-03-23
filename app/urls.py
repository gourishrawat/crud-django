from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('studentadd/',views.student),
    path('table/',views.table),
    path('edit/<int:uid>/',views.edit),
    path('editdata/',views.editdata),
    path('delete/<int:uid>/',views.delete),
]
