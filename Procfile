web: daphne chat.asgi:application --port $port --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=chat.settings -v2