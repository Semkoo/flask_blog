# Flask Blog

To use the application it recommend to use a virtualenv when developing projects

`$ source flask_blog_env/bin/activate`

Install all the dependency and run the app

`$ pip pip install -r requirements.txt`
`$ python run.py`

It also good idea to save the dependency in `requirements.txt` if there are updates

`$ pip freeze --local > requirements.txt`
### About the project

- Made use of `sqlite` database and self-taught `flask_SQLAlchemy`, a powerful ORM (Object-relational
  mapping), to increase development and for any future upgrades to any relational database management system.
- Understand the concept of splitting code into packages structure for scalability as well as utilizing Blueprints.
- User Authentication - Hash with bycrpt module as well as protecting routes
- HTML5 Validation - Bootstrap Error Style
- Able to perform [CRUD Action](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) on posts as well as authorizing which user can perform.  
- Understanding Pagination with optional query params, as well as relationship database
- Added Email Validation and Password Reset with JWT Serializer to reset account 
- Storing credentials into environment variable 
