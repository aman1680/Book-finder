from django.http import HttpResponse
from django.shortcuts import render
from .functions import scrap_websites

def home(request):
    book = ""
    author = ""
    publisher = ""
    results = {}
    avail = False
    try:
        if request.method == 'POST':
            book = request.POST.get('book')
            author = request.POST.get('author')
            publisher = request.POST.get('publisher')

            results = scrap_websites(book = book, author = author, publisher = publisher)

            avail = True
            print("data scrapped")
    except:
        print("Error Occured")

 #  amazon = amazon_scrap(book = book, author = author, publisher = publisher)

    data = {'available': avail, 'sites': results}
    return render(request, 'index.html', data)


