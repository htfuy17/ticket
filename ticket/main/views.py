from django.shortcuts import render

def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')

def flower(request):
    '''
    Render the about page
    '''
    return render(request, 'main/flower.html')

def booking(request):
    '''
    Render the about page
    '''
    return render(request, 'main/booking.html')