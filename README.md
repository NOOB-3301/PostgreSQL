# The server is hosted on render not on vercel , please use this link [Render link](https://postgresql-mmqh.onrender.com/)

I have added basic authentication and blog operations like adding, editing system in flask and postgresql . I hosted them on render and make them production ready

# Approach:

## File structure:
```
backend/
┣ app/                                      # entry point of the server
┃ ┣ controllers/                            # coontrollers and routes for the api
┃ ┃ ┣ __init__.py 
┃ ┃ ┣ auth.py                               #auth routes and controllers
┃ ┃ ┗ user.py                               #profile routes and controllers
┃ ┣ models/                                 #models for the db
┃ ┃ ┣ __init__.py
┃ ┃ ┣ base.py                            #defined base model with createdAt and updatedAt
┃ ┃ ┗ user.py                            #defined basic user model
┃ ┣ services/ 
┃ ┣ __init__.py                           #initialize the flask app
┃ ┗ config.py                             #config of the flask app, like db url, pass  
┣ .gitignore
┣ requirements.txt
┣ run.py                                   # main entry point of the application
┗ vercel.json
```
 
## Database:
1. Used Postgresql database hosted on `railway` and for the backend server used flask and  it is hosted on `render` .
2. Used `Gunicorn run:app` for deployment command. As flask's `app.run()` does not used in production based environment instead, have to use wsgi server like gunicorn which acts as a bridge between web servers and Python web applications like Flask.
3. Used Flask-SQLAlchemy orm for intarecting with database

## Hosted Url:
[render link](https://postgresql-mmqh.onrender.com/) <br>
Render pin down with inactivity, which can delay requests 

## Routes:
Auth routes:
```
/auth/login      - for login
/auth/register   - for register
/user/profile    - for user profile
```

```
/addblog                  - for adding a blog
/blogs                    - for getting all blogs
/editblog/<int:blog_id>   - for editing any blog
```
## Testing:
Images can be found in [images](./images/images.md) <br>
Can be tested via postman
### request schema:
```
{
    "username":"sql2",
    "email":"sql2@gmail.com",
    "password":"12345"
}
```
### response schema:
```
{
    "message": "User registered successfully"
}
```

