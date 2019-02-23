from django import forms
from my_blog.models import Comment
class AddCommenr(forms.ModelForm):
    class Meta :
        model= Comment
        fields= "__all__"
        exclude=["post"]

