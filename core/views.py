from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class Home(TemplateView):
    template_name = "home.html"

# Create your views here.
class QuestionCreateView(CreateView):
    model = Question
    template_name = "question/question_form.html"
    fields = ['name', 'email', 'message']
    success_url = reverse_lazy('home')