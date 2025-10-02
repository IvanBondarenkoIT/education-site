web: python manage.py migrate && python manage.py create_initial_data && python manage.py loaddata all_data && python manage.py collectstatic --noinput && gunicorn education_site.wsgi --log-file -
