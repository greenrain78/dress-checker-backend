import os
from py_env.database import DB_INFO

db_info = DB_INFO[os.environ["DB_NAME"]]

DB_URL=f"postgresql://{db_info['USER']}:{db_info['PASSWORD']}@{db_info['IP']}:{db_info['PORT']}/{db_info['DATABASE']}"