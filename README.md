# django-app

With docker support.

# Setup

```bash
touch db.sqlite3
pip3 install virtualenv
virtualenv env
source env/bin/activate
alias compose='docker-compose -f local.yml'
compose build
compose up
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
