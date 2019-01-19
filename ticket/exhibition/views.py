from django.shortcuts import render

from exhibition.models import Exhibition
from exhibition.forms import ExhibitionForm
from main.views import admin_required

@admin_required
def exhibition(request):
    '''
    Render the exhibition page
    '''
    exhibitions = Exhibition.objects.all()
    context = {'exhibition':exhibition}
    return render(request, 'exhibition/exhibition.html', context)

@admin_required
def exhibitionCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the exhibition page
    '''
    template = 'exhibition/exhibitionCreate.html'
    if request.method == 'GET':
        return render(request, template, {'exhibitionForm':ExhibitionForm()})