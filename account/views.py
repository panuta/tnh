from django.shortcuts import render


def view_user_login(request):
    return render(request, 'pages/weaving_table.html', {})
