from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если есть вопросы звоните', '(099) 099-99-99', 'mail@dfx.ru']})
# Create your views here.
