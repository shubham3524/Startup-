from django.contrib import admin
from news.models import Article,UserArticle
# Register your models here.
admin.site.register(Article)
admin.site.register(UserArticle)