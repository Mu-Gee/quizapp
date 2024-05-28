#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
#from django.core.management import execute_from_command_line
from django.contrib.auth.models import User

def create_superuser():
    """Create superuser if it doesn't exist."""
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser('admin', 'admin@quizzapp.com', '@dm!n1quiz')
        print('Superuser created successfully')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    create_superuser()  # Create superuser if it doesn't exist
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
