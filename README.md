# My readme for the benmore interview project

This project was written in django with the frontend written as templates incorporating tailwindcss and jquery.
To setup,

1. Clone repo, then activate a venv.

```
git clone https://github.com/Olamidipupo-favour/benmore-interview
cd benmore-interview
python -m venv benmore
"benmore/Scripts/activate"
```

2.  Install python dependencies

```
pip install -r requirements.txt
```

3. Run migrations

```
cd benmore
python manage.py makemigrations
python manage.py migrate
```

4. Start the development server

```
python manage.py runserver
```

The URL for deployed version of this interview is located at [tasky](https://benmore-interview.onrender.com/)
