from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    #url(r'^review/', views.review, name='review'),
    #url(r'^gallary/', views.gallary, name='gallary'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^', views.tweetArticle, name='tweets'),
    url(r'^', views.summaryArticle, name='search'),

    
]
