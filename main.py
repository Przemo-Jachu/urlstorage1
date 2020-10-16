from database import Database
from sys import argv
from os import getenv
from dotenv import load_dotenv
import click
load_dotenv()


#python main.py setup - tworzy baze danych
#python main.py add podstawy http://bastion.e-sys.eu - dodajemy rekord do bazy

@click.group()
def cli():
    pass

@click.command()
def setup():
    print('Tworze tabele w bazie danych')
    db = Database(getenv('DB_NAME'))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')

@click.command()
def add(category: str, url: str):
    print('Dodaje nowy adres url')
    db = Database(getenv('DB_NAME'))
    db.insert('urls', None, category, url)


@click.command()
def fetch_categories():
    print('Lista kategorii:')
    db = Database(getenv('DB_NAME'))
    categories = db.fetch_distinct('urls', 'category')

    for name in categories:
        print(name)

@click.command()
def index(category: str):
    print(f'Lista linkow z kategorii {category}:')
    category = argv[2]
    db = Database(getenv('DB_NAME'))
    links = db.fetch_all('urls',category=category)
    for link in links:
        print(link)

if len(argv) ==2 and argv[1] == 'setup':
    '''
    Initialize database 
    python main.py setup - tworzy baze danych
    '''
    setup()

if __name__ == '__main__':
    cli()


if len(argv) == 2 and argv[1] == 'categories':
    fetch_categories()

if len(argv) == 4 and argv[1] == 'add':
    '''
    python main.py add podstawy http://bastion.e-sys.eu

    '''
    add(category=argv[2], url=argv[3])

if len(argv) == 3 and argv[1] == 'list':

    '''
    python main.py list podstawy
    listing resources in category
    '''
    index(category=argv[2])
