import sqlite3

class Connect(object):
    def __init__(self, db_name):
        try:
            # connect
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print("Banco:", db_name)
            # Read SQLite version
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Error to open database.")
            return False

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Close connection.")


class RoutineDb(object):
    def __init__(self):
        self.db = Connect('routine.db')

    def create_schema(self, table_name, schema_name='sql/activities_schema.sql'):
        print("Crieating table %s ..." % table_name)

        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print("The table %s already exist." % table_name)
            return False

        print("Success to create %s table." % table_name)

    def insert_activities(self):
        try:
            self.db.cursor.execute("""
            INSERT INTO activities (activity_id, activity_name, activity_freq, activity_check)
            VALUES (?, ?, ?, ?)""", (1 ,'Leitura', '2', False))
            
            self.db.commit_db()
            print("An activity was iserted successfully.")
        except sqlite3.IntegrityError:
            print("Invalid.")
            return False
        except sqlite3.OperationalError:
            print("no such table: activities")

    def close_connection(self):
        self.db.close_db()

if __name__ == '__main__':
    routine = RoutineDb()
    routine.create_schema("activities")
    routine.insert_activities()
    routine.close_connection()


