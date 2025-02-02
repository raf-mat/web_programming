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
            "title": title,
            "content": html_content
        })

def search(request):
    if request.method =="POST":
        # storing the value user input into entry_search variable
        entry_search = request.POST['q']
        # converting entry search md file into html thanks to import markdown functions + storing into html_content variable
        html_content = convert_md_to_html(entry_search)
        # if html_content is known/True render the entry page concerned with the the title and content 
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
        # else store all the entries thanks to the util function into allEntries variable
        else:
            allEntries = util.list_entries()
            # creating an empty array to store the future recommendation
            recommendation = []
            # looping around allEntries
            for entry in allEntries:
                # putting everything in lower case and if user input (entry_search) is part of one of allEntries then append(add) into the empty array reccommendation 
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
                # then render search.html and display the reccommendation
            return render(request, "encyclopedia/search.html",{
                "recommendation": recommendation
                })


def create(request):
    # if request method is get when going to create a new page it should display the django form AddArticle
    if request.method == "GET":
        return render (request, "encyclopedia/create.html", {
            "form" : AddArticle()
    })
    # if request method is post then 
    else:
        # store the data the user submited into the 'form' variable
        form = AddArticle(request.POST)
        if form.is_valid():
            # store seperatly the data of eacch form input (title and content) "title" and "content" are comming from the django form class AddArticle
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            # store the title of all our entry that already exist into variable titleExist
            titleExist = util.get_entry(title)
            # if titleExist is know / true then render a error message : entry already exist
            if titleExist is not None:
                return render(request, "encyclopedia/error.html",{
                    "message" : "Entry page already exist"
                })
            # else we are using the util function util.save_entry to add the title and the content we have stored earlier into those variable
            else:
                util.save_entry(title, content)
                # converting MD content into html
                html_content = convert_md_to_html(title)
                # then return the entry page we have just registered 
                return render(request,"encyclopedia/entry.html", {
                    "title": title,
                    "content": html_content
                })

def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title": title,
            "content": content
        })

def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content
        })
