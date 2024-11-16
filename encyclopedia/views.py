from django.shortcuts import render
from . import util
import markdown2

def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown2.markdown(content)
    })

def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()
    results = [entry for entry in entries if query.lower() in entry.lower()]

    # If a matching entry is found, show that entry's page
    if util.get_entry(query):
        return entry(request, query)
    
    # If no matching entry, render the search results page
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })





