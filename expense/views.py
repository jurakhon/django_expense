from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Exp
from .forms import expenseForm


# Create your views here.


def expense_list(request):
    expenses = Exp.objects.all()
    return render(request, "expense_list.html", {"expenses": expenses})


def create_expense(request):
    if request.method == "POST":
        form = expenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = expenseForm()
    return render(request,"expense_form.html",{"form":form})

# def expense_detail(request, pk):
#     expense = Exp.objects.filter(id=pk).first()
#     if expense:
#         return render(request,


def expense_update(request, pk):
    exp = Exp.objects.filter(id=pk).first()
    if exp:
        form = expenseForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
        else:
            form = expenseForm(instance=exp)
        return render(request,"expense_form.html",{"form":form})
    else:
        return HttpResponse("Expense ID Not Found")

def expense_delete(request, pk):
    exp = Exp.objects.filter(id=pk).first()
    if exp:
        if request.method == "POST":
            exp.delete()
            return redirect("expense_list")
        else:
            return render(request,"confirm_delete_expense.html",{"form":exp})
    else:
        return HttpResponse("Expense ID Not Found")