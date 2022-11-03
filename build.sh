set -o errexit

poetry install

python manage.py collectstatic --noinput
python manage.py migrate 
