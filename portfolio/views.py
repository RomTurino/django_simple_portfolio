from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def main(request):
    objs = Portfolio.objects.all()
    return render(request, 'portfolio/main.html', {'objs': objs})