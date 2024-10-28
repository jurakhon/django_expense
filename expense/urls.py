from django.urls import path
from .views import *

urlpatterns = [
    path("", expense_list, name="expense_list"),
    path("create/", create_expense, name="create_expense"),
    path("update/<int:pk>", expense_update, name="expense_update"),
    path("delete/<int:pk>", expense_delete, name="expense_delete"),





]
