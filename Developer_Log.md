# Developer Log

##### Project Spec Sheet

[x] Start a new Django project called Blog.
[x] Create an app called blogs in the project, with a model called BlogPost.
[x] The model should have fields like title, text, and date_added.
Create a superuser for the project, and use the admin site to make a couple
of short posts . Make a home page that shows all posts in chronological order.
Create a form for making new posts and another for editing existing posts.
Fill in your forms to make sure they work .

# Developer Instructions

##### Create Project

1. Run virtual environment with `source 11_env/bin/activate`
2. Run termianl command `pip install Django` if Django is not installed.
3. Start project with `django-admin.py startproject Blog .` if project
has not been created yet. Make sure you don't forget the `.` at the end of terminal project creation command.
4. Create the database with `python manage.py migrate` terminal command
if migration has not been applied.
5. Terminal run server with `python manage.py runserver`

##### Create APP

1. Activate virtual environment with `source 11_env/bin/activate`
2. Run the terminal command `python manage.py startapp BlogPost` to
create a new project.
3. Start coding in models.py file



