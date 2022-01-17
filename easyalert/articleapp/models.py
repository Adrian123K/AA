from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    
    # 게시글 작성 날짜를 자동으로 등록
    created_at = models.DateField(auto_now_add=True, null=True)