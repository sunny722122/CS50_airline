from python
copy . /usr/src/app
workdir /usr/src/app
run pip install -r requiremtnts.txt
cmd ["python","manage.py","runserver","0.0.0.0:8000"]