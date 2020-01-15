from django.urls import path
from blog import views

urlpatterns = [
    path('index/', views.index),
    path('tag_detail/<int:tag_id>/', views.tag_detail),
    path('note_detail/<int:note_id>/',views.note_detail),
    path('index/search/',views.search),
    path('detail/comment/', views.add_comment),
    path('detail/<int:note_id>/', views.detail),
]
