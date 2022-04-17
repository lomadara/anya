from os import environ
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class DbConnectionSingleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwds):
        host = environ.get("HOST")
        if host not in cls._instances:
            cls._instances[host] = super(DbConnection, cls).__call__(*args, **kwds)
        
        return cls._instances[host]
    
class DbConnection(metaclass=DbConnectionSingleton):
    def __init__(self) -> None:
        self._host = environ.get("HOST")
        self._user = environ.get("USER")
        self._password = environ.get("PASSWORD")
        self._db = environ.get("DB")
        self.con = None
    
    def connect(self):
        connection_url = "mysql+pymysql://{}:{}@{}/{}".format(
            self._user,
            self._password,
            self._host,
            self._db
        )
        
        mysql_engine = create_engine(connection_url)
        mysql_session = sessionmaker(bind=mysql_engine)
        self.con = mysql_session()
    
    def disconnect(self):
        self.con.close()
    
    def rollback(self):
        self.con.rollback()
    
    def commit(self):
        self.con.commit()
