# Books REST API

A Django REST Framework application for managing books and authors with JWT authentication.

## Features

-  Complete CRUD operations for books and authors
-  JWT authentication using `djangorestframework-simplejwt`
-  User-based book ownership
-  Permission-based access control (authenticated users can create/update, everyone can read)
-  RESTful API design with class-based views and ViewSets

## Tech Stack

- **Django** - Web framework
- **Django REST Framework** - REST API toolkit
- **djangorestframework-simplejwt** - JWT authentication
- **SQLite** - Database (default)

## Project Structure

```
rest_app/
├── books/                      # Books app
│   ├── models.py              # Book and Author models
│   ├── serializers.py         # API serializers
│   ├── views.py               # API views
│   └── urls.py                # App URL routing
├── rest_app/                  # Project settings
│   ├── settings.py
│   └── urls.py                # Base URL routing
└── manage.py
```

## Installation

1. **Clone the repository**

```bash
git clone <your-repository-url>
cd Django-playground
```

2. **Create and activate virtual environment**

```bash
python3 -m venv rest_env
source rest_env/bin/activate  # On Windows: rest_env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

4. **Run migrations**

```bash
cd rest_app
python manage.py migrate
```

5. **Create a superuser**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Obtain JWT access and refresh tokens |
| POST | `/api/token/refresh/` | Refresh access token |

**Obtain Token Example:**
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

### Books

| Method | Endpoint | Description | Authentication Required |
|--------|----------|-------------|------------------------|
| GET | `/api/books/` | List all books | No |
| POST | `/api/books/` | Create a new book | Yes |
| GET | `/api/books/<id>/` | Get book details | No |
| PUT | `/api/books/<id>/` | Update a book | Yes |
| DELETE | `/api/books/<id>/` | Delete a book | Yes |

**Create Book Example:**
```bash
curl -X POST http://127.0.0.1:8000/api/books/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_access_token>" \
  -d '{
    "title": "Sample Book",
    "published_date": "2024-01-01",
    "author_id": 1,
    "price": "29.99"
  }'
```

### Authors

| Method | Endpoint | Description | Authentication Required |
|--------|----------|-------------|------------------------|
| GET | `/api/authors/` | List all authors | No |
| POST | `/api/authors/` | Create a new author | Yes |
| GET | `/api/authors/<id>/` | Get author details | No |
| PUT | `/api/authors/<id>/` | Update an author | Yes |
| DELETE | `/api/authors/<id>/` | Delete an author | Yes |

## Models

### Book
- `title` - Book title
- `published_date` - Publication date
- `author` - Foreign key to Author
- `price` - Book price
- `owner` - Foreign key to User (auto-assigned on creation)

### Author
- Defined in [`books/models.py`](rest_app/books/models.py)
- Used by [`AuthorSerializer`](rest_app/books/serializers.py)

## Views

The API uses two different approaches:

1. **Class-Based Views** ([`BookList`](rest_app/books/views.py) and [`BookDetail`](rest_app/books/views.py))
   - Custom APIView classes for books
   - Manual implementation of GET, POST, PUT, DELETE methods

2. **ViewSets** ([`AuthorViewSet`](rest_app/books/views.py))
   - ModelViewSet for authors
   - Automatic CRUD operations

## Authentication

This API uses JWT (JSON Web Tokens) for authentication via [`JWTAuthentication`](rest_app/books/views.py).

**To authenticate requests:**
1. Obtain a token from `/api/token/`
2. Include the token in the Authorization header:
   ```
   Authorization: Bearer <your_access_token>
   ```


## URL Configuration

The base URL configuration routes all API endpoints under the `/api/` prefix:
- Admin panel: `/admin/`
- Books API: `/api/` (includes books and authors endpoints)

## Development


### Access Django Admin

Visit `http://127.0.0.1:8000/admin/` and login with your superuser credentials.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.