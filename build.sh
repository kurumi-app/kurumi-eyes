set -o errexit

pip install --upgrade pippip install --force-reinstall -U setuptools

poetry install

python manage.py collectstatic --noinput
python manage.py migrate 
