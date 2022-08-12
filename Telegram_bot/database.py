import sqlite3 as sq

async def database_connect():
    global db, cur
    db = sq.connect('to_do.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS to_do_list(
        id INTEGER PRIMARY KEY,
        date TEXT,
        term TEXT,
        task_name TEXT,
        priority TEXT,
        status TEXT
    )""")
    db.commit()

async def get_all_tasks():
    tasks = cur.execute("SELECT * FROM to_do_list").fetchall()
    return tasks

async def find_tasks(samp):
    all = cur.execute("SELECT * FROM to_do_list").fetchall()
    tasks = []
    for line in all:
        if any(list(map(lambda elem: samp in elem, line))):
            tasks.append(line)
    return tasks

async def add_new_task(state):
    async with state.proxy() as data:
        task = cur.execute("INSERT INTO to_do_list (date, term, task_name, priority, status) VALUES (?, ?, ?, ?, ?)", (data['date'], data['term'], data['task_name'], data['priority'], data['status']))
        db.commit()
    return task

async def delete_task(task_id: int):
    cur.execute("DELETE FROM to_do_list WHERE id = ?", (task_id, ))
    db.commit()

async def edit_task(task_id: int, title: str):
    cur.execute("UPDATE to_do_list SET task_name = ? WHERE id = ?", (title, task_id, ))
    db.commit()