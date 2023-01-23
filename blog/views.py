from django.shortcuts import render, HttpResponse

# Create your views here.

def testIndexBlog(request):
    return HttpResponse('Ini Blog')