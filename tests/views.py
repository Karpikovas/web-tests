from django.shortcuts import render, HttpResponse, Http404, get_object_or_404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from .models import Test, Tag, Question, Answer
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views import generic
from django.contrib.auth import logout
from django.urls import reverse
from .forms import Testsystem



def test_suite(request):
	tags_list = Tag.objects.all().order_by('name')
	context = {'tags_list': tags_list}
	return render(request, 'tests/tests.html', context)

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "tests/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "tests/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('test_suite'))

"""class TestDetailView(generic.DetailView)
	model = Test
	template_name = 'tests/test_system.html'

	def get_questions(self):
		return Test.question_set.all()
"""

def test_system(request, test_id):
	
    form = Testsystem(request.POST)
    test = get_object_or_404(Test, pk=test_id)
    if request.method == "POST":
        if form.is_valid():
            choice = request.POST["choice"]

    return render(request, 'tests/test_system.html', {'form': form})

class QuestionDetailView(generic.DetailView):
    model = Test
    template_name = 'tests/questions.html'

