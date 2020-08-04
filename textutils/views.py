# I have created this file - Gaurav Dubey
from django.http import  HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def contact_us(request):

    return render(request, 'contact_us.html')


def error_file(request):

    return render(request, 'error_file.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')



    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')
    wordcount = request.POST.get('wordcount', 'off')
    linecount = request.POST.get('linecount', 'off')


    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char


        params = {'purpose' : 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose' : 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charactercount == "on"):
        analyzed_char = ""
        analyzed_char_2 = ""
        count = 0
        n = 0
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed_char = analyzed_char + char
            if char == "\n" and char == "\r":
                n = n + 1

        for index, char in enumerate(analyzed_char):
            if not (analyzed_char[index] == " " and analyzed_char[index + 1] == " "):
                analyzed_char_2 = analyzed_char_2 + char

        for char in analyzed_char_2:
            if char != " ":
                count = count + 1
            else:
                count = count + 0

            total = count

        analyzed = f"The total number of characters in your entered text is: {total}"
        params = {'purpose': 'Character Counted', 'analyzed_text': analyzed}

    if (wordcount == "on"):
        import re
        res = len(re.findall(r'\w+', djtext))
        analyzed = f"The total number of words in your entered text is: {res}"

        params = {'purpose': 'Words Counted', 'analyzed_text': analyzed}

    if (linecount == "on"):
        count_1 = 0
        num = djtext.split('\n')
        for i in num:
            if i != "\n":
                count_1 += 1

        analyzed = f"The total number of lines in your entered text is: {count_1}"

        params = {'purpose': 'Lines Counted', 'analyzed_text': analyzed}



    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and
    extraspaceremover != "on" and charactercount != "on" and wordcount != "on" and linecount != "on"):
        return render(request, 'error_file.html')

    return render(request, 'analyze.html', params)

