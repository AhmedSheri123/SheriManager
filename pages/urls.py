from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetDate, name="GetDate"),
    path('index/<str:selected_date>', views.index, name="index"),
    path('Pay/<int:id>', views.Pay, name="Pay"),
    path('remove/<int:id>/<str:selected_date>', views.RemovePayment, name="RemovePayment"),
    path("AddUser", views.AddUser, name="AddUser")
]