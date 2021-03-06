Features - a simplistic feature tracker.
----

Requirements:  
  - MongoDB  
  - Python 3 interpreter and virtual environment
  - Bower

Development Setup:  

1. Make a virtual environment for python3, more details regarding virtual environments at http://docs.python-guide.org/en/latest/dev/virtualenvs/.

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

2. Then install requirements.
```
pip install -r requirements.txt
```

To change settings the features application should use one uses environment variables, for instance (this can also be set in your virtual environment's bin/activate file, to make setting permanent within the virtual environment):
```
export F_SETTINGS="features_app.settings.DevelopmentConfig"
``` 
Note: If none is set, DevelopmentConfig is used.

3.
To install frontend external libraries bower (http://bower.io/) is required.

```
cd frontend/
bower install
```

4.
To compile the frontend into a single page application install required gulp modules:


```
npm install -g gulp
npm install 
```

And then you can just run gulp and the when a change occures the css and javascript files will recompile.
```
gulp
```

5.
After setup you can run the development server with:
```
./manage.py runserver
```
