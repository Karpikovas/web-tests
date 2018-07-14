from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def test_suite(request):
	return render(request, 'tests/test_suite.html', {}) 