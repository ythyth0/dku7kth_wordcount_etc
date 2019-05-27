from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    # 제목을 정상적으로 가질 수 있게 해주는 함수
    def __str__(self):
        return self.title
