from python3
copy . /usr/src/app
workdir /usr/src/app
run pip install -r requiremtnts.txt
cmd ["python3","manage.py","runserver","0.0.0.0:8000"]