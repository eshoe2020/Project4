from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('articles/', views.articles_index, name='articles_index'),
    path('articles/<int:article_id>/', views.articles_detail, name= 'articles_detail'),
    path('articles/<int:article_id>/add_comment/', views.add_comment, name= 'add_comment'),
    # path('articles/<int:pk>/comment/create/', views.CommentCreate.as_view(), name='comments_create'),
    # path('articles/<int:pk>/comments/update/<int:comment_id>/', views.CommentUpdate.as_view(), name='comments_update'),
    # path('articles/<int:pk>/comments/delete/<int:comment_id>/', views.CommentDelete.as_view(), name='comments_delete'),
]