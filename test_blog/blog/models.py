from django.db import models


class Post(models.Model):
    title = models.CharField('Заголовок записи', max_length=50)
    desctiption = models.TextField('Описание запись')
    author = models.CharField('Автор', max_length=50)
    date = models.DateField('Дата публикации')
    image = models.ImageField('Изображения', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.desctiption}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя пользователя", max_length=15)
    text_comments = models.TextField("Комментарий", max_length=100)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

