# Just some notes on getting up and running with mysql

## How do?

Pretty much the relevant install...

See http://text-analytics101.rxnlp.com/2013/11/how-to-install-mysql-on-amazon-ec2.html for the linux AMI option.

I hadn't bothered with the last part.

## Django

```sh
sudo yum install mysql-devel
virtualenv venv
source venv/bin/active
pip install django mysqlclient
```

And that gives us Django with mysql!

The project is already set up, so to get mysql ready, Django needs:
```sh
mysql -u root -p
#you'll be prompted for a password
```

And in mysql:

```
create database cs4AllDB character set utf8
#I'm told Django expects utf8. The name is for convenience.
exit
```

Back to bash...

```sh
cd #the cs4all root you git cloned into
python manage.py makemigrations
python manage.py migrate
```
