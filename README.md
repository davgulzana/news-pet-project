# Test project for DevelopToday
Heroku: https://test-develop-today.herokuapp.com/admin

Documentation: https://documenter.getpostman.com/view/14709805/TWDcFuN8


## Quick Start
Prerequisites:
* Git
* Docker
* Docker Compose

Download the project code into a new directory:

```
$ git clone https://github.com/davgulzana/test-developtoday.git  
$ cd test-developtoday
```
Create `.env` file for environment variables:
* SECRET_KEY
* DEBUG
* DATABASE_URL

Run `docker-compose up -d --build` to download the Docker images and bring up the development environment in Docker Compose. This will take a while the first time, but on subsequent runs will be much quicker as the Docker images will be cached.

Assuming the above step succeeded, you should now have a Django app running in a Docker container service named web, connected to other container services running Postgres, and a separate background task runner.

However, the Postgres database will be empty. Populate it by running:

```
$ docker-compose run web python3 manage.py migrate
```
Run this command to add all the defined `CRONJOBS` to `crontab`(*nix cron utility).

```
$ docker-compose run web python3 manage.py crontab add
```

All going well you should now be able to open the Django app at http://localhost:8000/.

You can create super user:

```
$ docker-compose run web python3 manage.py createsuperuser
```
And login as super user at http://localhost:8000/admin/.
