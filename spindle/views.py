from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html')


def character_detail_page(request):
    return render(request, 'character_detail_page.html')


def character_create_page(request):
    return render(request, 'character_form_page.html')


def character_update_page(request):
    return render(request, 'character_form_page.html')


def character_list_page(request):
    return render(request, 'character_list_page.html')


def post_detail_page(request):
    return render(request, 'character_detail_page.html')


def post_form_page(request):
    return render(request, 'post_form_page.html')


def post_list_page(request):
    return render(request, 'post_list_page.html')
