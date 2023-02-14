from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):
    if request.method == 'POST':
        title = request.POST['q']
        
    else:
        return render(request, "encyclopedia/content.html", {
            "title": title,
            "entry": util.get_entry(title),
        })
