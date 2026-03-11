from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Todo


def register_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate required fields
        if not username or not password:
            return render(request, "register.html", {"error": "Username and password are required"})

        # Validate password length
        if len(password) < 8:
            return render(request, "register.html", {"error": "Password must be at least 8 characters"})

        # Check password confirmation
        if password != confirm_password:
            return render(request, "register.html", {"error": "Passwords do not match"})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already taken"})

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, "register.html")

def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate required fields
        if not username or not password:
            return render(request, "login.html", {"error": "Username and password are required"})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def todo_list_view(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, "todo_list.html", {"todos": todos})

@login_required
def create_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        
        if title:
            Todo.objects.create(user=request.user, title=title, description=description)
            return redirect('todo_list')
    
    return render(request, "create_todo.html")

@login_required
def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    
    if request.method == "POST":
        todo.title = request.POST.get('title', todo.title)
        todo.description = request.POST.get('description', todo.description)
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        return redirect('todo_list')
    
    return render(request, "edit_todo.html", {"todo": todo})

@login_required
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    
    if request.method == "POST":
        todo.delete()
        return redirect('todo_list')
    
    return render(request, "delete_todo.html", {"todo": todo})

@login_required
def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')
