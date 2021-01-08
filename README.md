# Flask Blog

To use the application it recommend to use a virtualenv when developing projects

`$ source flask_blog_env/bin/activate`

Than install all the dependency

`$ pip pip install -r requirements.txt`

It also good idea to save the dependency in `requirements.txt`

`$ pip freeze --local > requirements.txt`
### About the project

- Made use of `sqlite` database and self-taught `flask_SQLAlchemy`, a powerful ORM (Object-relational
  mapping), to increase development and for any future upgrades to any relational database management system.
- Understand the concept of splitting code into packages structure for scalability
- User Authentication - Hash with bycrpt module and protecting routes.
- HTML5 Validation - Bootstrap Error Style

DB Relationship
User 1 - M Post
