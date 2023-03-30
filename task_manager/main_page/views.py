from django.shortcuts import render, redirect, HttpResponse
from registration.models import *
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

@login_required
def index(request):
    #return render(request, 'main_page/home.html' )
    user = request.user
    tasks = Task.objects.filter(player=user, habit__isnull = True, is_daily = False)
    habits = Habit.objects.filter(player=user)
    dailies = Task.objects.filter(player=user, habit__isnull = True, is_daily = True)
    return render(request, 'main_page/home.html', {'tasks': tasks, 'habits':habits, 'dailies': dailies, 'pfp': user.profile_pic.url })

@login_required
def logout_view(request):
    logout(request)
    return redirect('registration:start_page')

@login_required
def categories_view(request):
    user = request.user
    categories = Category.objects.filter(player=user)
    return render(request, 'main_page/categories.html', { 'categories': categories })

@login_required
def achievements_view(request):
    return HttpResponse("achievements")

@login_required
def profile_view(request):
    return HttpResponse("profile")

class ShowTask(DetailView):
    model = Task
    template_name = 'main_page/show_task.html'
    slug_url_kwarg = 'task_slug'
    context_object_name = 'task'

class ShowHabit(DetailView):
    model = Habit
    template_name = 'main_page/show_habit.html'
    slug_url_kwarg = 'habit_slug'
    context_object_name = 'habit'