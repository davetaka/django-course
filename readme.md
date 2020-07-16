# What is it?
this is the my studying content when i was following the Udemy course  
[Python 3 na web com django básico e intermediário](https://www.udemy.com/course/python-3-na-web-com-django-basico-intermediario)  

### goal
#### make an app called SimpleMooc
* it's a simple online platform for teaching  
* focused on open courses and massives
* developed in python 3 and django 1.6 (i think this course is old, maybe i'll try with updated django)
* make a really useful app
* we will put something in production weekly
* make some exercises
* a practically content

#### functionalities
1. class system
* creation, edition and deleting lessons and modules
* lessons composed by: video, donwloads, quiz
* associated with courses

2. questions forum
* open forum
* topics organized by categories
* users must be logged in

3. submit exercises
* students can send their solutions files
* could have something like automatic validation
* submitted files will generate grade for students

4. bulletin system
* bulletin board
* notices will be sending to students via e-mail
* they will have a page where they can receive comments

5. users account system
* users can register themselves and log in system
* users can change their profiles
* users will have a public profile


### how to setup and run
0. it needs python 3
1. activate virtualenv
2. install django 3.0.8
3. run manage.py migrate
4. run manage.py runserver


### notes
* uses purecss
* django in 3.0.8