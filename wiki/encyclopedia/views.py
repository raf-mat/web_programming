import markdown
from django.shortcuts import render
from . import util
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class AddArticle(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':100, 'size':8}), label="Text Area")

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else: 
        return markdowner.convert(content)
     
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
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

def search(request):
    if request.method =="POST":
        # storing the value user input into entry_search variable
        entry_search = request.POST['q']
        # converting entry search md file into html thanks to import markdown functions + storing into html_content variable
        html_content = convert_md_to_html(entry_search)
        # if html_content is known 
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html",{
                "recommendation": recommendation
                })


def create(request):
    if request.method == "GET":
        return render (request, "encyclopedia/create.html", {
            "form" : AddArticle()
    })
    else:
        form = AddArticle(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            titleExist = util.get_entry(title)
            if titleExist is not None:
                return render(request, "encyclopedia/error.html",{
                    "message" : "Entry page already exist"
                })
            else:
                util.save_entry(title, content)
                html_content = convert_md_to_html(title)
                return render(request,"encyclopedia/entry.html", {
                    "title": title,
                    "content": html_content
                })
