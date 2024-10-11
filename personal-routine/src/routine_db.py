import sqlite3

def get_all_activities():
    conn = sqlite3.connect("routine.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activities")
    all_activities = cursor.fetchall()
    conn.close()

    return all_activities

def get_new_id():
    pass

def get_name_with_id(name_activity):
    pass

def check_done(id):
    conn = sqlite3.connect("routine.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE activities SET check = ? WHERE id = ?", (True, id))
    conn.commit()
    conn.close()

def remove_activity(id):
    conn = sqlite3.connect("routine.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM activities WHERE id = ?", (id,))
    conn.commit()
    conn.close()