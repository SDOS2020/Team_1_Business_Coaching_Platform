web: gunicorn --pythonpath Business_Coaching_Platform Business_Coaching_Platform.wsgi --log-file -
web2: daphne --pythonpath Business_Coaching_Platform Business_Coaching_Platform.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python Business_Coaching_Platform/manage.py runworker channel_layer -v2