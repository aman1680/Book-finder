from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Repository 

# Create your views here.


def repository(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')

        if title and file:
            fs = FileSystemStorage()
            print(file.name)
            filename = fs.save(title+'.pdf', file)
            file_url = fs.url(filename)

            Repository.objects.create(title=title, file=filename)

            return redirect('success')
        else:
            error = "Both title and file is required."
    elif request.method == 'GET':
        name = None
        if request.GET.get('search') != '':
            name = request.GET.get('search')
        db = Repository.objects.all()

        results = []

        for i in db:
            if i.title == name:
                results.append(i)

        return render(request, 'repository.html', {'title': name, 'result': results})
    else:
        error = None
        return render(request, 'repository.html')

def success(request):
    return render(request, 'success.html')
