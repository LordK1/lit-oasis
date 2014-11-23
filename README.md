# Lit-Oasis

This is my first enjoyable  experience of a combination of several different things like Django, Heroku and Bootstrap also .

you can see all the requirements that you need to install on the local and heroku app with PIP in requirements.txt .
For database used sqlite3 , also used Django admin default template for manage admin panel .
use Bootstrap for Html , CSS , and Javascript on the templates ,

## Running Locally
Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone https://github.com/LordK1/lit-oasis.git
$ cd lit-oasis
$ pip install -r requirements.txt --allow-all-external
$ python manage.py syncdb
$ foreman start web
```
Your app should now be running on [localhost:5000](http://localhost:5000/).

I've [found](https://github.com/memcachier/examples-django2) the way for create and test local database with sqlite3 , for that in settings.py used these below lines :

```sh
curdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sqlite_db = 'sqlite://localhost/' + curdir + '/../queue.sqlite'
DATABASES = {'default': dj_database_url.config(default=sqlite_db)}
```
these lines help to use sqlite database when local develoment and use PostgerSQL for running on Heroku .

Tanks [David Terei](https://github.com/dterei)

and then you can run these command :

```sh
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py runserver
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

