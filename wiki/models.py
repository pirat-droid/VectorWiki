from django.db import models
from django.conf import settings
from django.urls import reverse
from pytils.translit import slugify

class PostModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField('Название статьи', max_length=150)
    img = models.ImageField('Логотип', upload_to='images/', default='images/images.jpg')
    slug = models.SlugField('Сылка поста', max_length=150, unique=True)
    description = models.TextField('Описание')
    date_create = models.DateTimeField('Дата создания', auto_now_add=True, blank=True)
    date_update = models.DateTimeField('Дата изменения', auto_now=True, blank=True)
    draft = models.BooleanField('Опубликовать', default=True)
    border = models.BooleanField('Доска', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postmodel_detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class GroupModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Название группы', max_length=150)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True, blank=True)
    date_update = models.DateTimeField('Дата изменения', auto_now=True, blank=True)
    draft = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class PhoneModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Имя контакта', max_length=150)
    group = models.ForeignKey(GroupModel, verbose_name='Група контактов', on_delete=models.CASCADE)
    email = models.EmailField('Email адрес', blank=True)
    phone = models.CharField('Номер телефона', max_length=13)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True, blank=True)
    date_update = models.DateTimeField('Дата изменения', auto_now=True, blank=True)
    draft = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

