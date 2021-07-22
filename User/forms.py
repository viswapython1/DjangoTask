from django import forms
from User.models import User,Post


class user_Form(forms.ModelForm):

    class Meta:
        model = User
        fields = "__all__"

class post_Form(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
