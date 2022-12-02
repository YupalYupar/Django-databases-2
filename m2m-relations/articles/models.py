from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тег')
    article = models.ManyToManyField('Article', through='RelationShip')

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class RelationShip(models.Model):
    article = models.ForeignKey('Article', verbose_name='Статья', on_delete=models.CASCADE, related_name='scopes')
    topic = models.ForeignKey('Tag', verbose_name='Тег', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='Главный тег')

    class Meta:
        verbose_name = 'О статьи'
