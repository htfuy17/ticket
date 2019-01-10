from django import forms
from article.models import Article

class ArticleForm(forms.ModelForm):
    SADRESS=(
        ('動畫手稿展覽','動畫手稿展覽'),
        ('花卉博覽會','花卉博覽會'),
        ('卡通運動會','卡通運動會'),
        ('宇宙人特展','宇宙人特展'),
    )

    SETYPE=(
        ('早鳥票 $200元','早鳥票 $200元'),
        ('預售票 $220元','預售票 $220元'),
        ('全票 $320元','全票 $320元'),
    )

    name = forms.CharField(label='姓名', max_length=10)
    phone = forms.CharField(label='連絡電話', max_length=10)
    title = forms.CharField(label='展覽名稱', widget=forms.widgets.Select(choices=SADRESS))
    ticket = forms.CharField(label='票種', widget=forms.widgets.Select(choices=SETYPE))
    number = forms.CharField(label='票數', max_length=10)
    

    class Meta:
        model = Article
        fields = ['name','phone','title','ticket','number']