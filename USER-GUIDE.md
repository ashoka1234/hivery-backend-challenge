# Paranuara Challenge - User Guide

### Populate the database
Run `manage.py` script `init` command to initially 
populate the database. Provide the two files that 
contain people and company information in `json` format.

```
python manage.py init --people resources/people.json --companies resources/companies.json
```

### Run the server

For development quick start (if you are on the top level 
directory of the repo):
```
$ export FLASK_APP=challenge/app.py
$ flask run
```

### Endpoints

The people end points are
- `/people/friends/<name1>/<name2>` : Returns the common friends who are
brown eyes and living.
- `/people/fruits_and_vegetables/<name>` : Returns the fruits and vegetables 
the person like.

The single company endpoint is:
- `/companies/<company>` : Returns the employees of the company.