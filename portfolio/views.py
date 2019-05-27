from django.shortcuts import render
from .models import Portfolio
# Create your views here.


def myportfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': portfolios})
