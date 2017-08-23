from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config('mysql://b43e9fb686d9c3:979c6f2b@eu-cdbr-west-01.cleardb.com/heroku_34a0eee9a408153')
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_skWYpLAsIvHYQZq5JizLocrW')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_1SOfreX572PCJQa5GK6GKJZo')