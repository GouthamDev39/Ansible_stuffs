import multiprocessing


wsgi_app = "App.wsgi:application"

bind = "127.0.0.1:8000"   

workers = multiprocessing.cpu_count() * 2 + 1
timeout=30


reload = False


loglevel = "debug"
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
capture_output = True


pidfile = "/var/run/gunicorn/prod.pid"