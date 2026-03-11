# TaskFlow 🚀

A modern, beautiful task management application built with Django and Tailwind CSS. Organize your daily tasks with an intuitive interface and stunning dark gradient design.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-darkgreen?logo=django&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.4-blue?logo=tailwindcss&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## Features ✨

- **User Authentication**: Secure login and registration system
- **Task Management**: Create, read, update, and delete tasks
- **Task Status**: Mark tasks as complete or incomplete
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Modern UI**: Dark gradient theme with glassmorphism effects
- **Sticky Navigation**: Always accessible navigation bar
- **Smooth Animations**: Beautiful transitions and hover effects

## Tech Stack 🛠️

- **Backend**: Django 6.0.3
- **Frontend**: HTML5, Tailwind CSS 3.4.19
- **Database**: SQLite
- **Python**: 3.12.3

## Installation 🔧

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/sabin3122/taskflow.git
cd taskflow
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Start the development server**
```bash
python manage.py runserver
```

6. **Start Tailwind CSS compiler (in another terminal)**
```bash
python manage.py tailwind start
```

The app will be available at `http://127.0.0.1:8000/`

## Usage 💡

### Creating an Account
1. Click "Sign Up" on the homepage
2. Enter your email, username, and password
3. Submit the form to create your account

### Managing Tasks
1. **View Tasks**: Navigate to "Todos" in the navigation bar
2. **Create Task**: Click "Create Todo" button
   - Enter task title and description
   - Click "Create" to save
3. **Edit Task**: Click the edit icon next to a task
   - Modify details as needed
   - Click "Update" to save
4. **Complete Task**: Click the checkbox to mark as complete
5. **Delete Task**: Click the delete icon and confirm

### Dashboard
- View quick statistics
- Access all features from one place
- Quick links to create new tasks

## Project Structure 📁

```
taskflow/
├── accounts/              # Authentication & todo management
├── theme/                 # Tailwind CSS configuration
├── templates/             # HTML templates
├── mysite/                # Django project settings
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
└── requirements.txt       # Python dependencies
```

## API Endpoints 🔌

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Dashboard |
| GET | `/login/` | Login page |
| GET | `/register/` | Registration page |
| GET | `/logout/` | Logout user |
| GET | `/todos/` | View all todos |
| POST | `/todos/create/` | Create new todo |
| GET\|POST | `/todos/<id>/edit/` | Edit todo |
| GET\|POST | `/todos/<id>/delete/` | Delete todo |
| POST | `/todos/<id>/toggle/` | Toggle todo status |

## Deployment 🚀

### Deploy to PythonAnywhere (Recommended)
1. Create account at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your code via Git
3. Configure WSGI file pointing to `mysite/wsgi.py`
4. Set up virtual environment
5. Configure static files
6. Reload the web app

### Deploy to Render.com
```bash
# Connect your GitHub repo to Render
# Build command: pip install -r requirements.txt && python manage.py collectstatic
# Start command: gunicorn mysite.wsgi:application
```

## Models 🗄️

### Todo Model
```python
class Todo(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=255)
    description = TextField(blank=True)
    completed = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
```

## Troubleshooting 🔧

| Issue | Solution |
|-------|----------|
| Tailwind CSS not compiling | `python manage.py tailwind build` |
| Database errors | `python manage.py migrate` |
| Static files not loading | `python manage.py collectstatic` |
| Port already in use | `python manage.py runserver 8001` |

## Dependencies 📦

- django==6.0.3
- django-tailwind==3.8.0
- Pillow==10.1.0

See `requirements.txt` for complete list.

## Contributing 🤝

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements 🌟

- [ ] Task categories/labels
- [ ] Due dates and reminders
- [ ] Task priority levels
- [ ] Dark/Light theme toggle
- [ ] Task search and filtering
- [ ] Email notifications

## License 📄

MIT License - see LICENSE file for details

## Author ✍️

**Sabin** - [GitHub](https://github.com/sabin3122)

---

**Made with ❤️ using Django and Tailwind CSS**