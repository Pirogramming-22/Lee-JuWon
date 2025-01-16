from django import forms
from .models import Idea, Tool

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'image', 'description', 'interest', 'dev_tool']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'cols': 50}),
        }

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['title', 'type', 'explain']  # 필요한 필드만 나열