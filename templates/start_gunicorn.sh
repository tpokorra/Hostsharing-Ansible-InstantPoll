#!/bin/bash

cd /home/pacs/{{pac}}/users/{{user}}/instantpoll
.venv/bin/python .venv/bin/gunicorn -c /home/pacs/{{pac}}/users/{{user}}/etc/gunicorn.conf.py instantpoll.asgi:application &