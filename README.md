# KCC - Krishna Cables & Conductors

A Django web application for Krishna Cables & Conductors business website.

## Features

- Modern responsive design
- Bootstrap 5 integration
- Static file handling
- Admin panel with Jazzmin theme
- User authentication with Django Allauth
- Contact forms with Crispy Forms
- Cloud storage support (Cloudinary)

## Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd KCC
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment variables:**
   - Copy `.env.example` to `.env`
   - Update the values in `.env` file

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Production Deployment

### Heroku Deployment

1. **Install Heroku CLI and login:**
   ```bash
   heroku login
   ```

2. **Create a new Heroku app:**
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY="your-secret-key"
   heroku config:set DEBUG=False
   heroku config:set DJANGO_SETTINGS_MODULE=KCC.settings_production
   ```

4. **Add PostgreSQL addon:**
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

5. **Deploy:**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

6. **Run migrations:**
   ```bash
   heroku run python manage.py migrate
   ```

7. **Create superuser:**
   ```bash
   heroku run python manage.py createsuperuser
   ```

### Railway Deployment

1. **Connect your GitHub repository to Railway**
2. **Set environment variables in Railway dashboard:**
   - `SECRET_KEY`
   - `DEBUG=False`
   - `DJANGO_SETTINGS_MODULE=KCC.settings_production`
3. **Railway will automatically deploy from your repository**

### Vercel Deployment

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Login and deploy:**
   ```bash
   vercel login
   vercel
   ```

3. **Configure environment variables in Vercel dashboard**

## Environment Variables

Required environment variables for production:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` for production
- `DATABASE_URL`: PostgreSQL connection string
- `EMAIL_HOST_USER`: SMTP email username
- `EMAIL_HOST_PASSWORD`: SMTP email password
- `CLOUDINARY_URL`: Cloudinary connection string (optional)

## Project Structure

```
KCC/
├── KCC/                    # Project settings
│   ├── settings.py         # Development settings
│   ├── settings_production.py # Production settings
│   ├── urls.py
│   └── wsgi.py
├── core/                   # Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/              # HTML templates
│   ├── base.html
│   └── core/
├── static/                 # Static files (CSS, JS, Images)
├── media/                  # User uploaded files
├── requirements.txt        # Python dependencies
├── Procfile               # Heroku deployment
├── runtime.txt            # Python version
└── manage.py
```

## Static Files

- Static files are handled by WhiteNoise in production
- Use `python manage.py collectstatic` to collect all static files
- Media files can be stored locally or in cloud storage (Cloudinary)

## Database

- SQLite for local development
- PostgreSQL for production (recommended)
- Use `DATABASE_URL` environment variable for production database

## Security

The production settings include:
- SSL/HTTPS enforcement
- Secure cookies
- HSTS headers
- XSS protection
- Content type sniffing protection

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is proprietary software for Krishna Cables & Conductors.
