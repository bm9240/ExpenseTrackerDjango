from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('expenses',views.expenseListView.as_view(), name = 'expenses'),
    path('accounts/register/',views.authenticate,name = 'register'),
    path('accounts/',include('django.contrib.auth.urls')),

]