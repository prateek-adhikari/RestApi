from django.urls import path
from api import views
urlpatterns = [
    path('articles', views.articleApi),
    path('createarticles', views.createArticleApi)
]