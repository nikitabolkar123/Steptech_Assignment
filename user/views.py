from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


def hello(request):
    return HttpResponse("Hello, World!")


def users_details(request):
    try:
        all_users = User.objects.all()
        return render(request, 'users.html', {'users': all_users})
    except Exception as e:
        return HttpResponse("Error fetching users from the database.")


def new_user(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            role = request.POST.get('role')
            user = User(name=name, email=email, role=role)
            user.save()
            return redirect('users')
        except Exception as e:
            return HttpResponse("An error occurred while saving the user.")
    return render(request, 'new_user.html')


def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return render(request, 'user_detail.html', {'user': user})
    except User.DoesNotExist:
        return render(request, 'user_not_found.html')
