from django.db import models
from django.db.models.fields import CharField, URLField,TextField

class Article(models.Model):
    title= CharField(max_length=300)
    author= CharField(max_length=20)
    content= TextField(5000)
    image= models.ImageField(upload_to="articles")
    source= URLField(max_length=225)


    class Meta:
       

        verbose_name =  'Article'
        verbose_name_plural =  'Articles'

    def __str__(self):
          return self.title
          

class UserArticle(models.Model):
    title= CharField(max_length=100)
    author= CharField(max_length=20)
    content= TextField()
    image= models.ImageField(upload_to="articles")
    source= URLField(max_length=225)


    class Meta:
       

        verbose_name =  'UserArticle'
        verbose_name_plural =  'UserArticles'

    def __str__(self):
          return self.title
