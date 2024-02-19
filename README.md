# Django Email Account Activation

This repository contains a simple Django project that demonstrates how to implement account activation via email. It is
designed as a basic example for those who are learning how to integrate email functionalities into their Django
applications to manage user account activations.

Go to `email_activation` app !

## Features

- User Registration
- Account Activation via Email
- Login/Logout

## Prerequisites

- virtual environment
- settings : 

```
# Emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = "your password"
DEFAULT_FROM_EMAIL = 'verification<your email>'
```

## And... run !
```
python manage.py migrate
python manage.py runserver
```