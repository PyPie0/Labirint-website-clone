from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (
	Book,
)


class HomeView(TemplateView):
	template_name = 'books/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['test_book_list'] = Book.objects.all()
		return context