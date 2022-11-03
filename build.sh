set -o errexit


poetry install
pip install --upgrade pip
pip install --force-reinstall -U setuptools

python manage.py collectstatic --noinput
python manage.py migrate 
