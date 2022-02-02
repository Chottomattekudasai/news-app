import requests
from django.shortcuts import render

def index(request):
    search = request.GET.get('search')
    if search is None:
        url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=c34769406bda439c911f3d1749555ef7'
    else:
        keyword = search
        url = 'https://newsapi.org/v2/everything?q=' + keyword + '&apiKey=c34769406bda439c911f3d1749555ef7'

    news = requests.get(url).json()
    a = news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    my_list = zip(title, desc, img)

    context = {'my_list': my_list}

    return render(request, 'index.html', context)