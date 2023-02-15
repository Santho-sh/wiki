from django.shortcuts import render, redirect
from . import util
from random import choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):
    return render(request, "encyclopedia/content.html", {
        "title": title,
        "entry": util.get_entry(title),
    })


def search(request):
    if request.method == 'POST':
        
        q = request.POST['q'].lower()
        entries = util.list_entries()
        results = []
        
        for entry in entries:
            if q == entry.lower():
                return redirect('/wiki/%s' %entry)
            
            elif q in entry.lower():
                results.append(entry)
        
        else:        
            return render(request, 'encyclopedia/search.html', {'results':results, 'query':q })
    else:
        return redirect('/')
    
    
    
def random(request):
    entries = util.list_entries()
    entry = choice(entries)
    return redirect('/wiki/%s' %entry)


def create(request):
    # form = CreateForm()
    return render(request, 'encyclopedia/create.html')


def edit(request):
    # form = EditForm()
    return render(request, 'encyclopedia/create.html')