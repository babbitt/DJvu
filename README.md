# A really bad DJ DB as a proof of concept (DJvu)
## How to install 
1. Clone 
2. create a virtualenv `virtualenv .` (assuming you have python3 installed and set as default)
3. Run `pip install -r requirements.txt`
4. Run `./manage.py runserver`
5. Navigate to `localhost:8000/admin`
6. Sign in with username `whrw` and password `whrwadmin`
7. Play around

I have done literally the bare minimum but everything y'all wanted is implemented.

## How to simulate use
1. Click on add next to Users on the homepage
2. Enter info
3. Click on add another DJ 
4. Fill out info, including slots, clearances, and station service

I've included a few show slots for testing but you can add more. 

5. Click save
6. Profit

We get a nice abstraction interface for accessing the data in python but otherwise it's structs that it auto-gens are pretty nice.

This is running on a sqllite db so it can live with the repo but Django is pretty good about being [DB agnostic](https://docs.djangoproject.com/en/3.1/ref/databases/)

If we want to work on this further I don't currently have the time to do all the web-dev for this but I could help and obviously provide Django pointers since I'm familiar with it.