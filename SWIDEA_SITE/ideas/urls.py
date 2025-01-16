from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  # 메인 페이지
    path('idea/<int:idea_id>/', views.idea_detail, name='idea_detail'),
    path('idea/delete/<int:idea_id>/', views.delete_idea, name='delete_idea'),
    path('idea/<int:idea_id>/update/', views.update_idea, name='update_idea'),
    path('add-idea/', views.add_idea, name='add_idea'),  # Add Idea 페이지
    path('add-tool/', views.add_tool, name='add_tool'),  # Add Tool 페이지
    path('manage-tools/', views.manage_tools, name='manage_tools'),  # Manage Tools 페이지  # 아이디어 상세 페이지
    path('dev_tool/<int:tool_id>/', views.dev_tool_detail, name='dev_tool_detail'),
    path('dev_tool/<int:tool_id>/delete/', views.delete_tool, name='delete_tool'),
    path('dev_tool/<int:tool_id>/update/', views.dev_tool_update, name='dev_tool_update'),
    path('toggle-star/<int:idea_id>/', views.toggle_star, name='toggle_star'),
]
