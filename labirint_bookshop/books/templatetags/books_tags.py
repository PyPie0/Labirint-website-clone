from django import template
from books.models import (
	Book,
)


register = template.Library()


@register.inclusion_tag('books/promo_slider.html')
def promo_slider():
	pass


@register.inclusion_tag('books/book_slider1.html')
def book_slider1(book_list):
	return {
		'books': book_list,
	}