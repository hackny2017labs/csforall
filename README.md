# CSFORALL Summit Commitments Project

## Upon committing changes, don't forget to update required packages
```sh
pip freeze > requirements.txt
```
# Setting up the project

## Clone the repo 

As of right now, the web url is https://github.com/hackny2017labs/csforall.git
```sh
git clone https://github.com/hackny2017labs/csforall.git
cd csforall/
```

## MySQL installation

Check here for the relevant install for your OS
https://dev.mysql.com/downloads/mysql/

Go through installation and !! TAKE NOTE OF PASSWORD !!


## Set up virtual environment & requirements

If you don't already have virtualenv then install it before setting it up
```sh
sudo pip install virtualenv
```
While inside csforall directory, activate virtual environment to install relevant packages:
```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt # install the necessary requirements
```

## MySQL Setup

If this is the first time setting up mysql, there's some overhead to get it working. You need to start the mysql server, and you can use this link to do so for relevant OS: 
https://dev.mysql.com/doc/refman/5.7/en/installing.html

On OS X, I was able to go to systems preferences, search mysql and manually turn on the server

Add mysql to path (optional)
```sh
export PATH=${PATH}:/usr/local/mysql/bin/
# this is for mac osx
```

Now you have to set up the password and database that corresponds to our settings in csforall/cs4all/settings.py
```sh
mysql
mysql -u root -p
# You'll be prompted for the password from installation (the one you took note of hopefully)
```

And in mysql:
```sh
ALTER USER 'root'@'localhost' IDENTIFIED BY 'cs4JustAboutEverybody!' # change to relevant password
CREATE DATABASE cs4AllDB character set utf8 # I'm told Django expects utf8. The name is for convenience.
exit
```
## Run the server

```sh
cd csforall/ # the root file you cloned originally
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
If this doesn't get everything set up, add relevant info to this doc
