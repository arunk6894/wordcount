from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'countwords.html')

def count(request):
    words_count = {}
    mess = request.GET['message']
    w1 = mess.split()
    x = sorted(set(w1))
    for i in x:
        x = w1.count(i)
        words_count[i] = x

    return render(request, 'count.html', context = {"mess" : mess, "length": len(w1), "count_of_words": words_count})


def aboutus(request):
    return render(request, "aboutus.html")