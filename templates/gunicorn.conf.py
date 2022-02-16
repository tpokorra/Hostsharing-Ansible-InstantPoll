# see https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py

bind = '127.0.0.1:{{gunicorn_port}}'
backlog = 2048
workers = 1
worker_class = 'uvicorn.workers.UvicornWorker'
worker_connections = 1000
timeout = 30
keepalive = 2

pidfile = '/home/pacs/{{pac}}/users/{{user}}/var/run/gunicorn.pid'
errorlog = '/home/pacs/{{pac}}/users/{{user}}/var/log/gunicorn.log'