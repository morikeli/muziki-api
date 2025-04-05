# 🎵 Music Track API

A simple and efficient RESTful API for managing music tracks, built with [Django](https://www.djangoproject.com/) and [Django Ninja](https://django-ninja.dev/).

## 🚀 Features

- ✅ Create, read, update, and delete (CRUD) music tracks  
- 🔍 Search and filter tracks by title, artist, genre, or release year  
- 📃 API schema and interactive documentation (Swagger & ReDoc)  
- ⚡ Fast and easy to integrate with frontend/mobile clients  
- 🛡️ Input validation with Pydantic models

## 📦 Tech Stack

- **Backend Framework**: Django  
- **API Framework**: Django Ninja  
- **Database**: SQLite (default), but easily swappable (e.g., PostgreSQL)  
- **Documentation**: Swagger UI & ReDoc via Ninja

## 📁 Project Structure

```
music_api/
├── api/               # Django app for music tracks
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── api.py           # API routers using Django-Ninja
│   ├── models.py        # Track model
│   ├── schemas.py       # Pydantic schemas for request/response
│   ├── tests.py
│   ├── views.py         # Optional Django views
│   └── ...
├── src/                 # Main Django project folder (contains core project settings and configuration)
│   ├── __init__.py      # Marks this directory as a Python package
│   ├── asgi.py          # ASGI config for asynchronous support (used for WebSockets, etc.)
│   ├── settings.py      # Main Django settings file (database, apps, middleware, etc.)
│   ├── urls.py          # Root URL configurations (routes incoming requests to app URLs or API)
│   ├── wsgi.py          # WSGI config for deployment (used by traditional servers like Gunicorn)
├── .gitignore           # Specifies intentionally untracked files to ignore in Git
├── manage.py            # Django’s command-line utility for running tasks (e.g., runserver, migrate, etc.)
├── README.md            # Project overview, setup instructions, and documentation
├── requirements.txt     # List of Python packages required to run the project
```

## 📥 Installation

```bash
cd Desktop

# Clone the repo
git clone https://github.com/morikeli/muziki-api.git

# Navigate to the `muziki-api` dir
cd muziki-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

## 🧪 Example API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/tracks/`     | List all music tracks    |
| GET    | `/api/tracks/{id}` | Retrieve a single track  |
| POST   | `/api/tracks/`     | Create a new track       |
| PUT    | `/api/tracks/{id}` | Update an existing track |
| DELETE | `/api/tracks/{id}` | Delete a track           |

## 📚 API Docs

Once the server is running:

- Swagger UI: [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)  
- ReDoc: [http://127.0.0.1:8000/api/redoc](http://127.0.0.1:8000/api/redoc)

## 📝 Example Track Model

```json
{
  "title": "Blinding Lights",
  "artist": "The Weeknd",
  "genre": "Pop",
  "release_year": 2019
}
```

## ✅ To-Do

- Add user authentication
- Add pagination and filtering
- Add support for file uploads (e.g. audio files or cover images)

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## 📄 License

This project is licensed by an MIT License
