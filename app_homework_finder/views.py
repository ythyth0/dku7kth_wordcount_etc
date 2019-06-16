from django.shortcuts import render
from . import crawling
# Create your views here.
def searching(request):
    return render(request, 'searching.html')

def complete(request):
    if request.method=='POST':
        user_id = request.POST['id']
        user_password = request.POST['password']
        user_univ = request.POST['univ']
        user_homework = request.POST['ass_btn']
        final_data = crawling.crawling(user_id,user_password,user_univ,user_homework)
        if final_data==0:
            return render(request, 'searching.html', {'error': 'username or password is incorrect'})
        return render(request,'complete.html',{'data':final_data, 'selected':user_homework})
    else:
        return render(request, 'searching.html')


