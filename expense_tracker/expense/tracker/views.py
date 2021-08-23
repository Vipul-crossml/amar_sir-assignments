# from django.http.response import HttpResponseGone
from tracker.models import Category
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import Expense, Category
from tracker.models import Expense
# Create your views here.
def index(request):
    expense_list = Expense.objects.all()

    form = ExpenseForm()

    if request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title')
        Expense(name=title).save()
        return redirect('/')
    else:
        context = {'expense_list' : expense_list,'form':form}
    return render(request,'tracker/index.html',context)


def category(request):
    category_list = Category.objects.all()
    context1 = {'category_list':category_list}
    return render(request,'tracker/index.html',context1)