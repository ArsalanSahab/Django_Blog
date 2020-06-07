from django.urls import path
from . import views



app_name = 'blog'

urlpatterns = [

    # Post Views

    path('', views.posts_list, name='posts_list'),
    # path('', views.PostListView.as_view(), name='posts_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_details, name='post_details'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.posts_list, name= 'post_list_by_tag'),




]