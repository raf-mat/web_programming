import markdown
from django.shortcuts import render
from . import util
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class Search(forms.Form):
    query = forms.CharField(label="Search Bar")

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else: 
        return markdowner.convert(content)
     
def index(request):
    if request.method == "POST":

        form = Search(request.POST)
        if query.is_valid():
            q = form.cleaned_data["q"]

            return HttpResponseRedirect(reverse("encyclopedia/index.html"))
        
        else:
            return render(request, "encyclopedia/error.html")
        
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": Search()
    })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "content": html_content
        })
