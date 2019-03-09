# Developer Guide

### Design

The software features a Flask web API and a MongoDB backend 
database API. The Web API has two domains, people, and companies
implemented by `Flask blueprints`. The database API has two
interfaces, `QueryAPI` and `WriteAPI` seperating the query
and write concerns. 

### Testing
The testing implementation has the following structure.
```
.
|-- conftest.py - Provides empty and populated database fixtures
      |-- tests - Unit tests
             |-- Unit test files
      |-- integration_tests - Flask integration tests
             |-- conftest.py - Empty Flask client with populated 
                            database fixture 
             |-- Integration test files

```

### Configuration
The database configuration is given by a `challenge.conf` file having
database connection information. This file could be located in the 
current directory, user home directory or the repo directory.

The `Flask API` has a configuration file `settings.env.py` which, at
the moment, can define the database name to be connected and thus
can override the database name given otherwise.

### CI/CD
An initial `travis CI` script is provided which at the moment can 
be used for automated unit and integration testing as you push to 
github.