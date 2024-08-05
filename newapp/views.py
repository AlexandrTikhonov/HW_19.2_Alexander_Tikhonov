from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(requect):
    return render(requect, 'contacts.html')