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
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```
Your app should now be running on [localhost:5000](http://localhost:5000/).

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

