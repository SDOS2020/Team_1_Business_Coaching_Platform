web: gunicorn Business_Coaching_Platform.wsgi --log-file -
web2: daphne Business_Coaching_Platform.routing:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2