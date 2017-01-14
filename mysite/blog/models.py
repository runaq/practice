from django.db import models
from django.utils import timezone

class Color(models.Model):
	id = models.AutoField( primary_key=True)
	name_color = models.CharField(max_length=20, unique=True, verbose_name='Название')
	color_number = models.CharField(max_length=6, verbose_name='RGB номер')
	text = models.TextField(verbose_name='Текст')
	
	def __str__(self):
		return self.name_color
  
class Post(models.Model):
	author = models.ForeignKey('auth.User', verbose_name='Автор')
	title = models.CharField(max_length=200, verbose_name='Название фрукта')
	color = models.ForeignKey(Color, to_field='name_color', verbose_name='Цвет')
	text = models.TextField( verbose_name='Описание')
	created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
	published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
	image = models.ImageField(blank=True, help_text='150x150px', verbose_name='Ссылка картинки')
    
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
		
	def image_img(self):
		if self.image:
			return u'<a href="{0}" target="_blank"><img src="{0}" width="100 px"/></a>'.format(self.image.url)
		else:
			return '(Нет изображения)'
	image_img.short_description = 'Картинка'
	image_img.allow_tags = True
		
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', verbose_name='Выберите цвет')
    author = models.CharField(max_length=200, verbose_name='Автор комментария')
    text = models.TextField( verbose_name='Комментарий')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата комментария')
    approved_comment = models.BooleanField(default=False, verbose_name='Утвержден')

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
	
def approved_comments(self):
	return self.comments.filter(approved_comment=True)
	
