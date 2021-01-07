from django import forms
from myswsite.models import *


class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ("title", "image", "content", "interest", "devtool")


class DevToolForm(forms.ModelForm):

    class Meta:
        model = DevTool
        fields = ("name", "kind", "description")