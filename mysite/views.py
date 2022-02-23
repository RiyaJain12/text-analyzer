#created by me
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    txt=request.POST.get('text','default')
    removep=request.POST.get('removepunc','off')
    upperc=request.POST.get('upperc','off')
    newlineremove=request.POST.get('newlineremove','off')
    puncuations='''!@#$%^&*():"?>;'''
    analyzed=""
    if removep=='on':
        for char in txt:
           if char not in puncuations:
              analyzed+=char
        params={'analyzed_text':analyzed,'purpose':'Remove punctuations'}
    elif(upperc=='on'):
        for char in txt:
            analyzed+=char.upper()
            params={'analyzed_text':analyzed,'purpose':'change to uppercase'}
    
    elif(newlineremove=='on'):
        for char in txt:
            if char!='\n' and char!='\r':
             analyzed+=char
            params={'analyzed_text':analyzed,'purpose':'removeline'}
    else:
        return HttpResponse("Error")
    #print(txt)
    #print(removep)
    return render(request,'analyze.html',params)