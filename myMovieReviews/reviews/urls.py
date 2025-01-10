from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),  # 기능 1
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),  # 기능 2, 4
    path('review/write/', views.review_write, name='review_write'),  # 기능 3, 8
    path('review/<int:review_id>/edit/', views.review_edit, name='review_edit'),  # 기능 6, 9
    path('review/<int:review_id>/delete/', views.review_delete, name='review_delete'),  # 기능 7
]
