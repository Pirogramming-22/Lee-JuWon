# ideas/models.py
from django.db import models
from django.contrib.auth.models import User

class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='idea_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    interest = models.PositiveIntegerField(default=0, blank=True, null=True)
    dev_tool = models.CharField(max_length=50, default='django', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)  # 아이디어
    session_key = models.CharField(max_length=50, blank=True)  # 세션 기반으로 찜 상태 유지
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session_key} - {self.idea.title}"

class Tool(models.Model):
    title = models.CharField(max_length=100)  # 도구 이름
    type = models.CharField(max_length=100)  # 도구 종류
    explain = models.TextField()  # 도구 설명

    def __str__(self):
        return self.title  # 기본적으로 도구 이름을 출력