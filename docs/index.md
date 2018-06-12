# pdf-generator

[![Build Status](https://travis-ci.org/Akus93/pdf-generator.svg?branch=master)](https://travis-ci.org/Akus93/pdf-generator)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Pdf generator for ZPP. Check out the project's [documentation](http://Akus93.github.io/pdf-generator/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)
- [Heroku Toolbelt](https://toolbelt.heroku.com/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```


# Continuous Deployment

Deployment automated via Travis. When builds pass on the master or qa branch, Travis will deploy that branch to Heroku. Enable this by:

Creating the production sever:

```
heroku create pdf-generator-prod --remote prod && \
    heroku addons:create newrelic:wayne --app pdf-generator-prod && \
    heroku addons:create heroku-postgresql:hobby-dev --app pdf-generator-prod && \
    heroku config:set DJANGO_SECRET=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="pdf-generator-prod" \
        --app pdf-generator-prod
```

Creating the qa sever:

```
heroku create `pdf-generator-qa --remote qa && \
    heroku addons:create newrelic:wayne && \
    heroku addons:create heroku-postgresql:hobby-dev && \
    heroku config:set DJANGO_SECRET=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="pdf-generator-qa" \
```

Securely add your heroku credentials to travis so it can automatically deploy your changes.

```bash
travis encrypt HEROKU_AUTH_TOKEN="$(heroku auth:token)" --add
```

Commit your changes and push to master and qa to trigger your first deploys:

```bash
git commit -m "ci(travis): added heroku credentials" && \
git push origin master && \
git checkout -b qa && \
git push -u origin qa
```
You're ready to continuously ship! ✨ 💅 🛳
