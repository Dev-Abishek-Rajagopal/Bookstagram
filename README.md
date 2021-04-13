<b><h1>|||     DB Structure    |||</b></h1>



 <img src = "https://drive.google.com/uc?id=1JXR5OXjUDstoY1qSuFcDygnDBYRbHUwx&export=download">
 
 
 
<b><h1>|||     Django Configuration     |||</b></h1> 
 

pip3 install Django

pip3 install djangorestframework

pip3 install djangorestframework-jsonapi

pip3 install djongo

pip3 install django-unixtimestampfield

pip3 install django-fernet-fields==0.6

pip3 install -r requirement.txt



<b><h1>|||     Server Configuration     |||</b></h1>



hostnamectl set-hostname Bookstagram //creating Host name

sudo vi /etc/hosts
   server-ip hostname   // entering in hosts 

sudo apt-get install ufw   // uncomplecated firewall

sudo ufw default allow outgoing

sudo ufw allow 80

sudo ufw allow ssh

sudo ufw enable

sudo ufw status

scp -r Bookstagram green@IP:/home/book/Bookstagram (cp local dir to server)

sudo apt-get install python3-pip (pip3)

sudo apt-get install python3-venv (virtual env)

python3 -m venv venv (create venv)

source venv/bin/activate (Activate)

pip3 install django

pip3 install djongo

install MongoDB

pip3 install wheel

pip3 install -r require.txt

pip3 install django-cors-headers

Migrate Django

check code

sudo apt-get install apache2

sudo apt-get install libapache2-mod-wsgi-py3

sudo vi book.conf


<p>

Bookstagram
    │   COMMANDS.md  
    │   manage.py
    │   README.md
    │   requirement.txt
    │   __init__.py
    │
    ├───ACCProject               >>>-----> Project Folder 
    │   │   asgi.py
    │   │   settings.py          >>>-----> Django Server Settings are done Here
    │   │   urls.py              >>>-----> API main Route 
    │   │   wsgi.py              >>>-----> A Web Server Gateway Interface (WSGI) server implements the web server side of the WSGI interface for running Python web applications.
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │           settings.cpython-39.pyc
    │           urls.cpython-39.pyc
    │           wsgi.cpython-39.pyc
    │           __init__.cpython-39.pyc
    │
    │
    ├───DBbackup                 >>>-----> DB backup will be stored here if Background cron task enabled
    ├───logs                     >>>-----> Log Folder
    │       debug.log            >>>-----> Django/python function specific logs Folder available here
    │       system.log           >>>-----> Django/python Server specific logs Folder available here
    │       task.log             >>>-----> Django/python Background Task specific logs Folder available here
    │
    └───SocialBookApp            >>>-----> App Folder (Mentioned in settings.py)
        │   admin.py             >>>-----> Django admin file (Display DB table of Models if specified)
        │   apps.py              >>>-----> Django apps.py is a configuration file common to all Django apps
        │   tests.py             >>>-----> Unit testing Purpose
        │   urls.py              >>>-----> All API route are declared here
        │   __init__.py
        │
        ├───migrations           >>>-----> Database Migrations
        │   │   0001_initial.py
        │   │   0002_auto_20210225_1741.py
        │   │   0003_bookcomments_ratings.py
        │   │   0004_auto_20210310_0058.py
        │   │   0005_booktree.py
        │   │   0006_auto_20210312_0003.py
        │   │   0007_booktree_user.py
        │   │   0008_remove_booktree_book.py
        │   │   0009_auto_20210312_0018.py
        │   │   0010_auto_20210312_0118.py
        │   │   0011_delete_booktree.py
        │   │   0012_booktree.py
        │   │   0013_auto_20210312_0150.py
        │   │   0014_auto_20210312_0227.py
        │   │   0015_auto_20210312_0232.py
        │   │   0016_auto_20210312_0233.py
        │   │   0017_bookusertree_username.py
        │   │   0018_auto_20210312_1806.py
        │   │   0019_booktreeconnect.py
        │   │   0020_booknewsfeed_friendnewsfeed.py
        │   │   0021_auto_20210313_0051.py
        │   │   0022_auto_20210317_1542.py
        │   │   0023_commentsnewsfeed_book.py
        │   │   0024_txtpostcommentsnewsfeed.py
        │   │   0025_auto_20210325_0138.py
        │   │   0026_auto_20210325_0146.py
        │   │   0027_auto_20210325_0201.py
        │   │   0028_auto_20210325_0221.py
        │   │   0029_tickernewsfeed.py
        │   │   0030_auto_20210403_0125.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           0001_initial.cpython-39.pyc
        │           0002_auto_20210225_1741.cpython-39.pyc
        │           0003_bookcomments_ratings.cpython-39.pyc
        │           0004_auto_20210310_0058.cpython-39.pyc
        │           0005_booktree.cpython-39.pyc
        │           0006_auto_20210312_0003.cpython-39.pyc
        │           0007_booktree_user.cpython-39.pyc
        │           0008_remove_booktree_book.cpython-39.pyc
        │           0009_auto_20210312_0018.cpython-39.pyc
        │           0010_auto_20210312_0118.cpython-39.pyc
        │           0011_delete_booktree.cpython-39.pyc
        │           0012_booktree.cpython-39.pyc
        │           0013_auto_20210312_0150.cpython-39.pyc
        │           0014_auto_20210312_0227.cpython-39.pyc
        │           0015_auto_20210312_0232.cpython-39.pyc
        │           0016_auto_20210312_0233.cpython-39.pyc
        │           0017_bookusertree_username.cpython-39.pyc
        │           0018_auto_20210312_1806.cpython-39.pyc
        │           0019_booktreeconnect.cpython-39.pyc
        │           0020_booknewsfeed_friendnewsfeed.cpython-39.pyc
        │           0021_auto_20210313_0051.cpython-39.pyc
        │           0022_auto_20210317_1542.cpython-39.pyc
        │           0023_commentsnewsfeed_book.cpython-39.pyc
        │           0024_txtpostcommentsnewsfeed.cpython-39.pyc
        │           0025_auto_20210325_0138.cpython-39.pyc
        │           0026_auto_20210325_0146.cpython-39.pyc
        │           0027_auto_20210325_0201.cpython-39.pyc
        │           0028_auto_20210325_0221.cpython-39.pyc
        │           0029_tickernewsfeed.cpython-39.pyc
        │           0030_auto_20210403_0125.cpython-39.pyc
        │           __init__.cpython-39.pyc
        │
        ├───models                      >>>-----> models folders is where the models for your app are located
        │   │   bookmodels.py           >>>-----> Models related to Books
        │   │   usermodels.py           >>>-----> Models related to Users
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           bookmodels.cpython-39.pyc
        │           usermodels.cpython-39.pyc
        │           __init__.cpython-39.pyc
        │
        ├───serializers
        │   │   serializers.py          >>>-----> Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then                                                     be easily rendered into JSON, XML or other content types. 
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           serializers.cpython-39.pyc
        │           __init__.cpython-39.pyc
        │
        ├───views                       >>>-----> A view function, or view for short, is a Python function that takes a Web request and returns a Web response.
        │   │   process.py              >>>-----> All view functions without Token Authentications are mentioned here
        │   │   views.py                >>>-----> All view functions with Token Authentications are mentioned here
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           process.cpython-39.pyc
        │           views.cpython-39.pyc
        │           __init__.cpython-39.pyc
        │
        └───__pycache__
                admin.cpython-39.pyc
                urls.cpython-39.pyc
                __init__.cpython-39.pyc

</p>
