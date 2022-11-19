from manager import Manager
from database import DataBase
from recursos.cinema import Cinema

cinema = Cinema("16/04/2022", 4)
database = DataBase(cinema=cinema)
manager = Manager(database=database, cinema=cinema)

while True:
    manager.home()