from django.shortcuts import render, redirect
from guestbook.models import Comment
from guestbook.forms import CommentForm


def index(request):
    comments = Comment.objects.order_by("-date_created")
    context = {
        "comments": comments,
    }
    return render(request, "guestbook/index.html", context)


def sign(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        print("Post after form instantiation")
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect("home")
        else:
            print("form is invalid")
            print(form.errors)
    else:
        print("GET request - rendering empty form")
        form = CommentForm()

    context = {
        "form": form,
    }
    print("Rendering sign.html with context:", context)
    return render(request, "guestbook/sign.html", context)
