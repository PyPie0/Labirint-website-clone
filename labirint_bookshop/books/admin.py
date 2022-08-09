from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import (
	Category,
	Author,
	Translator,
	Illustrator,
	Book,
	PublishingHouse,
	Series,
)


class PublishingHouseAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


class SeriesAdmin(admin.ModelAdmin):
	pass


class AuthorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('first_name', 'last_name')}


class TranslatorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('first_name', 'last_name')}


class IllustratorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('first_name', 'last_name')}


class CategoryAdmin(DraggableMPTTAdmin):
	prepopulated_fields = {'slug': ('title',)}


class BookAdmin(admin.ModelAdmin):
	pass


admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Illustrator, IllustratorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Series, SeriesAdmin)