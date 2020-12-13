web: gunicorn Business_Coaching_Platform.Business_Coaching_Platform.wsgi --log-file -
web2: daphne  Business_Coaching_Platform.Business_Coaching_Platform.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python Business_Coaching_Platform/manage.py runworker -v2
