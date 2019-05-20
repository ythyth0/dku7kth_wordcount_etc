from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)  #제목
    pub_date=models.DateTimeField('date published') #시간
    body=models.TextField() #내용

    def __str__(self):      # 객체 이름 내가 만든 제목으로 만들기
        return self.title
    
    def summary(self):          # 본문 100글자 상한선
        return self.body[:100]  # slicing(리스트 자르기), 처음부터 100글자까지 


