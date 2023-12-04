from django.shortcuts import render
from .models import MathTest

def test_list(request):
    tests = MathTest.objects.all()
    return render(request, 'simpleapp/test_list.html', {'tests': tests})
