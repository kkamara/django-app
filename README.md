# django-app

With docker support.

## Setup

```bash
cp .env.example .env
touch db.sqlite3
pip3 install virtualenv && \
  virtualenv env && \
  source env/bin/activate
alias compose='docker-compose -f local.yml'
compose build
compose up
```

The django-app runs at `http://localhost` and `http://localhost:80`.

## Mail Server

![docker-mailhog.png](https://raw.githubusercontent.com/kkamara/useful/main/docker-mailhog.png)

Mail environment credentials are at [.env](https://raw.githubusercontent.com/kkamara/django-app/develop/.env.example).

The [mailhog](https://github.com/mailhog/MailHog) docker image runs at `http://localhost:8025`.

## Admin

Admin creds are set in [./compose/local/django/start](https://raw.githubusercontent.com/kkamara/django-app/develop/compose/local/django/start)

```bash
export DJANGO_SUPERUSER_PASSWORD=secret

python manage.py createsuperuser \
  --username admin_user \
  --email admin@django-app.com \
  --no-input \
  --first_name Admin \
  --last_name User
```

## API Docs

View the api collection [here](https://documenter.getpostman.com/view/17125932/UVyn1ycU).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
