from django.shortcuts import render, redirect
from . import util
from random import choice
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):
    content = util.get_entry(title)
    if content != None:
        content = markdown2.markdown(content)
    return render(request,"encyclopedia/content.html", {
        "title": title,
        "content": content,
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
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        entries = util.list_entries()
        entries_lower = [i.lower() for i in entries]
        if title.lower() in entries_lower:
            message = 'Title already exists.'
            return render(request, 'encyclopedia/error.html', {'message':message})
        
        util.save_entry(title, content)
        return redirect('/')
        
    return render(request, 'encyclopedia/create.html')


def edit(request, title):
    if request.method == 'POST':
        
        new_content = request.POST['new_content']  
        
        util.save_entry(title, new_content)
        return redirect('/')
    
    else:
        return render(request, 'encyclopedia/edit.html', {'title':title, 'old_content': util.get_entry(title),
        })