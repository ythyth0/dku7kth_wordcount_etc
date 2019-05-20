from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs=Blog.objects      # 쿼리셋(객체 목록 받아옴)  # 메소드
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):
    details=get_object_or_404(Blog, pk=blog_id)     # (Blog 객체에서, blog_id번 데이터)
    return render(request, 'detail.html',{'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog=Blog() # 객체 생성
    blog.title=request.GET['title']     # 입력받은 내용을 변수 안에 저장
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()   # 블로그 작성한 시점 넣어주는 함수
    blog.save()     # 객체를 db에 저장
    return redirect('/blog/'+str(blog.id))  # str(정수형을 문자형으로 변경), url+문자열  
