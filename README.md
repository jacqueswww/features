Features - a simplistic feature tracker.
----

Requirements:  
    - MongoDB  
    - Python 3 virtual environment  

Development Setup:  

1) Make a virtual environment for python3, more details regarding virtual environments at http://docs.python-guide.org/en/latest/dev/virtualenvs/.

```
pip install virtualenv
```

```
virtualenv -p /usr/bin/python3 features
```

To enter your virtual environment:

```
source features/bin/activate
```

Then install requirements.
```
pip install -r requirements.txt
```
 
After setup you can run the development server with:
```
./manage.py runserver
```
