from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.http import require_POST
from myswsite.forms import *
from myswsite.models import Idea, DevTool
from django.http import HttpResponseRedirect,HttpResponse

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
            key = Idea.objects.count()
            url = reverse('myswsite:idea_read', args=[key])
            return redirect(to=url)
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
            url = reverse('myswsite:idea_read', args=[idea])
            return redirect(to=url)

    else:
        form = IdeaForm(instance=idea)
        data = {
            "form": form
        }
        return render(request, "myswsite/idea_update.html", data)


def idea_delete(request, pk):
    idea = Idea.objects.get(pk=pk)
    idea.delete()
    ideas = Idea.objects.all()
    data = {
        "ideas": ideas
    }
    return render(request, "myswsite/idea_list.html", data)

@require_POST
def interest_ajax(request):
    pk = request.POST.get("pk")
    status = request.POST.get("status")
    idea = get_object_or_404(Idea, pk=pk)

    if status == "plus":
        idea.interest += 1
    else:
        if idea.interest > 0:
            idea.interest -= 1
        else:
            redirect('idea_list')
    idea.save()
    data = {
        "interest": idea.interest,
    }
    return JsonResponse(data)


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


def devtool_create(request, devtool = None):
    if request.method == "POST":
        form = DevToolForm(request.POST, instance = devtool)
        if form.is_valid():
            devtool = form.save()
            return redirect(devtool)
    else:
        form = DevToolForm(instance = devtool)
    return render(request,'myswsite/devtool_create.html',{"form" : form})    
        
        
        


def devtool_update(request, pk):
    devtool = DevTool.objects.get(pk=pk)

    if request.method == "POST":
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            devtool = form.save()
            url = reverse('myswsite:devtool_read', args=[devtool])
            return redirect(to=url)

    else:
        form = DevToolForm(instance=devtool)
        data = {
            "form": form
        }
        return render(request, "myswsite/devtool_update.html", data)


def devtool_delete(request, pk):
    devtool = DevTool.objects.get(pk=pk)

    devtool.delete()
    devtools = DevTool.objects.all()
    data = {
        "devtools": devtools
    }
    return render(request, "myswsite/devtool_list.html", data)

