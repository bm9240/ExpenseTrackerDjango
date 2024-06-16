from django.shortcuts import render, redirect
from django.contrib.auth import login 
from .models import Account, Expense
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import ExpenseForm
from django.db.models import Sum
import plotly.express as px 
from plotly.graph_objs import *


def home(request):
    return render(request , 'home/home.html')

def authenticate(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request , 'registration/register.html', {'form' : form})

class expenseListView(FormView):
    template_name = 'components/expenseForm.html'
    form_class = ExpenseForm
    success_url = '/'
    
    def form_valid(self,form):
        account, _ = Account.objects.get_or_create(user=self.request.user)
        expense = Expense(
            title=form.cleaned_data['title'],
            amount=form.cleaned_data['amount'],
            category=form.cleaned_data['category'],
            date=form.cleaned_data['date'],
            description=form.cleaned_data['description'],
            user=self.request.user
        )
        expense.save()
        account.expense_list.add(expense)
        return super().form_valid(form)
    
    def get_context_data(self,**kwargs): 
        context = super().get_context_data(**kwargs)
        user = self.request.user
        accounts = Account.objects.filter(user = user)
        expenses = Expense.objects.filter(user = user)
        context['expenses'] = expenses
    
        expense_data_graph = {}
        expense_data = {}

        for account in accounts:
            for expense in account.expense_list.all():
                if expense.category in expense_data_graph:
                    expense_data_graph[expense.category] += expense.amount
                else:
                    expense_data_graph[expense.category] = expense.amount
        expense_data = {'Category': list(expense_data_graph.keys()), 'Amount': list(expense_data_graph.values())}
        fig = px.bar(expense_data, x='Category', y='Amount', title='Expenses by Category')
        graph = fig.to_json()
        context['graph'] = graph
        total_expense_amount = expenses.aggregate(Sum('amount'))['amount__sum']
        context['total_expense'] = total_expense_amount
        return context









