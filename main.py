from app.config.connection import drop_database, initiate_database
from app.sorter import sort_log
from web import app

if __name__ == '__main__':
    drop_database()
    initiate_database()
    sort_log('out')
    app.run(debug=True)
