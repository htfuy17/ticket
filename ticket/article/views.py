from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required


from article.models import Article
from article.forms import ArticleForm

@login_required
def article(request):
    '''
    Render the article page
    '''
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'article/article.html', context)

@login_required
def articleCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    template = 'article/articleCreate.html'
    if request.method == 'GET':
        print(ArticleForm())
        return render(request, template, {'articleForm':ArticleForm()})
    
    # POST
    articleForm = ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})

    articleForm.save()
    messages.success(request, '訂單已完成')
    return redirect('article:article')