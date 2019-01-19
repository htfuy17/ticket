from django import forms
from exhibition.models import Exhibition


class ExhibitionForm(forms.ModelForm):
    photo = forms.CharField(label='照片', max_length=10)
    news  = forms.CharField(label='詳細內容',max_length=10)

    class Meta:
        model = Exhibition
        fields = ['photo', 'news']