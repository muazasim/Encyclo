from django.shortcuts import render
from random import choice
from . import util
from django import forms
import markdown2
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewPage(forms.Form):
    Title = forms.CharField(label="Title")
    Discription = forms.CharField(
        widget=forms.Textarea, label="Content")
    #  = forms.TextInput()


def search(request):
    if request.method == 'POST':
        title = request.POST.get('q')
        titles = util.list_entries()

        if title in titles:
            entryData = util.get_entry(title)
            entry = markdown2.markdown(entryData)
            return render(request, "encyclopedia/displayentry.html",
                          {
                              "EntryData": entry,
                              'Title': title
                          }
                          )
        else:
            return render(request, "encyclopedia/search.html", {
                "entries": util.list_entries(),
                'title': title
            })


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def displayentry(request, title):

    entryData = util.get_entry(title)
    entry = markdown2.markdown(entryData)
    return render(request, "encyclopedia/displayentry.html",
                  {
                      "EntryData": entry,
                      'Title': title
                  }
                  )


def updateentry(request, title):
    entryData = util.get_entry(title)
    entry = markdown2.markdown(entryData)
    if request.method == "POST":
        updatedcontent = request.POST.get('textarea')
        util.save_entry(title, updatedcontent)
        return HttpResponseRedirect(reverse("wiki:index"))
    return render(request, "encyclopedia/Updateentry.html",
                  {
                      'Title': title,
                      'EntryData': entry,
                      #   'form': NewPage(title, entryData)
                  })


def createnewpage(request):
    if request.method == "POST":
        form = NewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data['Title']
            content = form.cleaned_data['Discription']
            print(title)
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
    return render(request, "encyclopedia/newpage.html", {
        "form": NewPage()
    })


def randomentry(request):
    entries = util.list_entries()
    content = choice(entries)
    entry = util.get_entry(content)
    entry = markdown2.markdown(entry)
    return render(request, "encyclopedia/randompage.html",  {'content': entry, 'Title': content})
