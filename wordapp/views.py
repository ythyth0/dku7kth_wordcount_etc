from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'wordhome.html')


def detail(request):
    return render(request, 'worddetail.html')


def result(request):
    text = request.GET['fulltext']
    full_words = text.split()

    word_dic = {}

    for wd in full_words:
        if (wd in word_dic):
            word_dic[wd] += 1
        else:
            word_dic[wd] = 1

    return render(request, 'wordresult.html', {'text': text, 'full_length': len(full_words), 'items_word_dic': word_dic.items()})
