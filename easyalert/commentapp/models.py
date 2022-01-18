from django.db import models

# Create your models here.
from articleapp.models import Article
from django.contrib.auth.models import User


class Comment(models.Model):
    # 서버에서 확인해야지
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    
    # 입력 받고
    content = models.TextField(null=False)
    
    # 자동 생성하고
    created_at = models.DateTimeField(auto_now=True)