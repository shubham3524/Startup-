from django.urls import path
from django.views.generic import TemplateView
from news import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('about/', TemplateView.as_view(template_name='about_us.html'),name='about_us'),
    path('contact/', TemplateView.as_view(template_name='contact_us.html'),name='contact_us'),
    path('news/',views.article_view,name='news'),
    path('submityourideas/',views.userarticle_add,name='submityourideas'),
    path('userideas/',views.User_view,name='userideas'),
    path('newsdetail/<int:id>',views.article_detail_new,name='newsdetail'),
    path('ideadetail/<int:id>',views.article_detail,name='ideadetail'),
    path('login/', TemplateView.as_view(template_name='registration/login.html'),name='login'),
    

]