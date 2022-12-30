from math import floor
from django.shortcuts import render

# Create your views here.
def wordCounter(request):
    __textPass = ""
    __characters = 0
    __words = 0
    __sentences = 0
    __paragraphs = 0
    __readingTime = 0
    __readingTimeMinute = 0
    __readingTimeSecond = 0
        
    if request.method == 'POST':
        __text = request.POST.get('textInput')
        __textPass = __text
        #cleaning text
        while '\n\n' in __text or '\r\n' in __text:
            __text = __text.replace("\r\n","\n")
            __text = __text.replace("\n\n","\n")

        __characters = len(__text)
        __words = len(__text.split(' '))
        __sentences = len(__text.split('.')) - 1
        __paragraphs = len(__text.split('\n'))
        
        __readingTime = __words / 4
        __readingTimeMinute = floor(__readingTime / 60)
        __readingTimeSecond = floor(__readingTime % 60)
        

    return render(request,'wordCounter/index.html', context = {
        'text' : __textPass,
        'char' : __characters,
        'word' : __words,
        'sentence' : __sentences,
        'paragraph' : __paragraphs,
        'readingTimeMinute' : __readingTimeMinute,
        'readingTimeSecond' : __readingTimeSecond,
    })
