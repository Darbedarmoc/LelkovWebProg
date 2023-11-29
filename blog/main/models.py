from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

    
# Модель статья
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='articles', verbose_name='Категория')

# Модель комментарии
class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True, blank=True)
    
# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    description = models.TextField()
    
#Модель тэги
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
