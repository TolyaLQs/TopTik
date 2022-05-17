from django.db import models
from user.models import User
from django.utils.safestring import mark_safe
# Create your models here.


class Tag(models.Model):
    name = models.CharField(verbose_name='Тег', unique=True, max_length=128)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128, blank=True)
    desc = models.TextField(verbose_name='Описание', blank=True)
    img = models.ImageField(verbose_name='Фото', blank=True, upload_to='post/photo')
    date_add = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    active = models.BooleanField(verbose_name='Активность', default=True)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    # auto_increment_id = models.AutoField(primary_key=True)

    # def quantity(self):
    #     quantity = PostLike.objects.filter(post_id=id).count()
    #     return quantity

    def __str__(self):
        return f'{self.date_add} | {self.title}'

    def get_img(self):
        if not self.img:
            return '/static/img/no-photo.png'
        return self.img.url

    def img_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_img())

    class Meta:
        ordering = ['-date_add']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostTag(models.Model):
    tag = models.ForeignKey(Tag, verbose_name='Тег', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag.name} | {self.post.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий', blank=True)
    img = models.ImageField(verbose_name='Картинка', blank=True, upload_to='post/comment')
    date_add = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    active = models.BooleanField(verbose_name='Активность', default=True)

    def __str__(self):
        return f'{self.date_add} | {self.post.title} | {self.author.name}'

    def get_img(self):
        if not self.img:
            return '/static/img/no-photo.png'
        return self.img.url

    def img_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_img())

    class Meta:
        ordering = ['-date_add']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class PostLike(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.name} | {self.post.title} | {self.post.date_add}'
