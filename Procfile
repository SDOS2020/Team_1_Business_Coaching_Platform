release: python manage.py makemigrations && python manage.py migrate
web: daphne Business_Coaching_Platform.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=Business_Coaching_Platform.settings -v2