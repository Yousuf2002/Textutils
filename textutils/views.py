from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    djtext = request.POST.get('text' , 'default')
    removepunc = request.POST.get('removepunc' , 'off')
    fullcaps = request.POST.get('fullcaps' , 'off')
    newlineremover = request.POST.get('newlineremover' , 'off')
    charcount = request.POST.get('charcount' , 'off')

    if removepunc == "on":
        punctuations = ''',!()-[]{}:;'"\/,.<>?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Remove Punctuations' , 'analyzed_text' : analyzed}
        # return render(request , 'analyze.html' , params)
        djtext = analyzed
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Changed to UpperCase' , 'analyzed_text' : analyzed}
        # return render(request , 'analyze.html' , params)
        djtext = analyzed
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
        params = {'purpose' : 'Remove New Lines' , 'analyzed_text' : analyzed}
        # return render(request , 'analyze.html' , params)
        djtext = analyzed
    if (charcount == "on"):
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed = analyzed + 1

        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    
    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and charcount != "on"):
        return HttpResponse("ERROR")
    
    return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("ERROR")
# def capfirst(request):
#     return HttpResponse('capitalize first </br> <button> <a href="http://127.0.0.1:8000/">Back</a></button>')

# def newlineremove(request):
#     return HttpResponse('capitalize first </br> <button> <a href="http://127.0.0.1:8000/">Back</a></button>')


# def spaceremove(request):
#     return HttpResponse('space remover</br> <button> <a href="http://127.0.0.1:8000/">Back</a></button>')

# def charcount(request):
#     return HttpResponse('charcount </br> <button> <a href="http://127.0.0.1:8000/">Back</a></button>')