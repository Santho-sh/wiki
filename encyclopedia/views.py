from django.shortcuts import render, redirect

from . import util


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
        q = request.POST['q']
        return redirect('/wiki/%s' %q)
    else:
        return redirect('/')