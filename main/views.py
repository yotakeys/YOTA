from django.shortcuts import render

# Create your views here.


def homeView(request):
    f = open("version.txt", 'r')
    version = f.readline()
    f.close()
    return render(request, 'main/index.html', {'version': version})
