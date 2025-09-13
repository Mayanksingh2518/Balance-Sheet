from django.urls import path
from . import views

urlpatterns = [
    path('balance-sheet/', views.balance_sheet_form, name='balance_sheet_form'),
]
