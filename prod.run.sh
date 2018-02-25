# Runner in Production
gunicorn prod:my_app -b 127.0.0.1:8000 -D --workers 3 --reload
echo "gunicorn in background"
#rm -f /etc/nginx/sites-enabled/default
nginx -g "daemon off;"
