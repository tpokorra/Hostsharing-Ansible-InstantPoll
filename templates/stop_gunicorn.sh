#!/bin/bash

pidfile=/home/pacs/{{pac}}/users/{{user}}/var/run/gunicorn.pid
if [ -f $pidfile ]; then
    /bin/kill $( cat $pidfile ) && rm -f $pidfile
fi
