from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name='Изображение')
    text = models.TextField(verbose_name="Содержимое поста")
    publish_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.author} - {self.title}"


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


