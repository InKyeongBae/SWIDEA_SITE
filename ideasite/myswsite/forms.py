from django import forms
from myswsite.models import *


class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ("title", "image", "content", "interest", "devtool")
        labels = {
            'title': '아이디어명',
            'image' : '대표 사진',
            'content': '아이디어 설명',
            'interest' : '아이디어 관심도',
            'devtool' : '예상 개발툴',
        }

class DevToolForm(forms.ModelForm):

    class Meta:
        model = DevTool
        fields = ("name", "kind", "description")
        labels = {
            'name': '이름',
            'kind': '종류',
            'description': '개발툴 설명'
        }