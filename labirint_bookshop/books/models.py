from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import ArrayField


class PublishingHouse(models.Model):
	title = models.CharField('Название', max_length=255)
	slug = models.SlugField(
		'Слаг',
		max_length=255,
		db_index=True,
		unique=True
	)
	description = models.TextField('Описание', blank=True)

	class Meta:
		verbose_name = 'Издательство'
		verbose_name_plural = 'Издательства'

	def __str__(self):
		return self.title


class Person(models.Model):
	first_name = models.CharField('Имя', max_length=55)
	last_name = models.CharField('Фамилия', max_length=55)
	middle_name = models.CharField('Второе имя', max_length=55, blank=True)
	slug = models.SlugField(
		'Слаг', 
		max_length=255,
		db_index=True,
		unique=True
	)

	class Meta:
		abstract = True
		ordering = ['first_name', 'last_name']

	def __str__(self):
		return f'{self.last_name} {self.first_name} {self.middle_name}'


class Illustrator(Person):
	class Meta:
		verbose_name = 'Художник'
		verbose_name_plural = 'Художники'


class Translator(Person):
	class Meta:
		verbose_name = 'Переводчик'
		verbose_name_plural = 'Переводчики'


class Author(Person):
	photo = models.ImageField(
		verbose_name='Фото', 
		upload_to='auhtor-photos/%Y/%m/%d', 
		blank=True,
		default='author-photos/default.png',
	)
	bio = models.TextField('Биография', blank=True)

	class Meta:
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'


class Category(MPTTModel):
	title = models.CharField('Название', max_length=255, unique=True)
	slug = models.SlugField(
		'Слаг',
		max_length=255,
		db_index=True,
		unique=True
	)
	parent = TreeForeignKey(
		'self', 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True, 
		related_name='children'
	)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	class MPTTMeta:
		order_insertion_by = ['title']

	def __str__(self):
		return self.title


class Series(models.Model):
	title = models.CharField('Название', max_length=255)
	publishing_house = models.ForeignKey(
		PublishingHouse,
		on_delete=models.SET_NULL,
		blank=True,
		null=True,
		verbose_name='Издательство'
	)
	description = models.TextField('Описание', blank=True)

	class Meta:
		verbose_name = 'Серия'
		verbose_name_plural = 'Серии'


class Book(models.Model):
	title = models.CharField('Название', max_length=255)
	category = TreeForeignKey(
		Category, 
		on_delete=models.SET_NULL,
		null=True, 
		verbose_name='Категория',
	)
	price = models.DecimalField(
		'Цена',
		max_digits=10, 
		decimal_places=2,
		validators=[MinValueValidator(0.0)]
	)
	discount = models.IntegerField(
		'Скидка в процентах', 
		blank=True, 
		default=0
	)
	publishing_house = models.ForeignKey(
		PublishingHouse,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		verbose_name='Издательство'
	)
	ISBN = models.CharField('ISBN', max_length=255)
	page_count = models.PositiveIntegerField('Кол-во страниц')
	weight = models.PositiveIntegerField('Масса', blank=True)
	size = ArrayField(
		models.CharField(max_length=10),
		size=3,
		blank=True,
		verbose_name='Размеры',
	)
	annotation = models.TextField('Аннотация', blank=True)
	image = models.ImageField(
		upload_to='book-photos/%Y/%m/%d', 
		blank=True,
		verbose_name='Изображение',
		default='book-photos/default.png'
	)
	in_storage = models.BooleanField('В наличии', default=True)
	author = models.ManyToManyField(
		Author,
		blank=True,
		verbose_name='Автор',
	)
	illustrator = models.ManyToManyField(
		Illustrator,
		blank=True,
		verbose_name='Художник',
	)
	translator = models.ManyToManyField(
		Translator,
		blank=True,
		verbose_name='Переводчик',
	)
	series = models.ForeignKey(
		Series,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		verbose_name='Издательство'
	)

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'

	def __str__(self):
		return self.title

	def get_discount_price(self):
		return int(self.price * (100 - self.discount) / 100)