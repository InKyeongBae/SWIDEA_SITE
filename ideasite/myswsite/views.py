from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myswsite.forms import *
from myswsite.models import Idea, DevTool

# Create your views here.

def idea_list(request):
    ideas = Idea.objects.all()
    data={
        'ideas':ideas
    }
    return render(request,'myswsite/idea_list.html',data)


def idea_read(request, pk):
    idea = Idea.objects.get(pk=pk)
    data = {
        "idea": idea
    }
    return render(request, "myswsite/idea_read.html", data)


def idea_create(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect("idea_read", idea.pk)
    else:
        form = IdeaForm()
        data = {
            "form": form
        }
        return render(request, "myswsite/idea_create.html", data)



def idea_update(request, pk):
    idea = Idea.objects.get(pk=pk)

    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
        return redirect("idea_read", idea.pk)

    else:
        form = IdeaForm(instance=idea)
        data = {
            "form": form
        }
        return render(request, "myswsite/idea_update.html", data)


def idea_delete(request, pk):
    idea = Idea.objects.get(pk=pk)

    if request.method == "POST":
        idea.delete()
        return redirect("idea_list")

    return redirect("idea_read", idea.pk)


# ==========거래처===============

def devtool_list(request):
    devtools = DevTool.objects.all()
    data = {
        "devtools": devtools
    }
    return render(request, "myswsite/devtool_list.html", data)


def devtool_read(request, pk):
    devtool = DevTool.objects.get(pk=pk)
    data = {
        "devtool": devtool
    }
    return render(request, "myswsite/devtool_read.html", data)


def devtool_create(request):
    if request.method == "POST":
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect("devtool_read", devtool.pk)
    else:
        form = DevToolForm()
        data = {
            "form": form
        }
        return render(request, "myswsite/devtool_create.html", data)


def devtool_update(request, pk):
    devtool = DevTool.objects.get(pk=pk)

    if request.method == "POST":
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            devtool = form.save()
        return redirect("devtool_read", devtool.pk)

    else:
        form = DevToolForm(instance=devtool)
        data = {
            "form": form
        }
        return render(request, "myswsite/devtool_update.html", data)


def devtool_delete(request, pk):
    devtool = DevTool.objects.get(pk=pk)

    if request.method == "POST":
        devtool.delete()
        return redirect("devtool_list")

    return redirect("devtool_read", devtool.pk)
