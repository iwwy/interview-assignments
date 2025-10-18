"""SQL Max Value

Select employees with the highest pay in each department. If more than one
employee has the highest pay, include them all.
"""
import sqlite3


def execute_query(conn, c, query):
    for row in c.execute(query).fetchall():
        print(row)


def connect():
    path = "employees.db"
    conn = sqlite3.connect(path)
    c = conn.cursor()
    return conn, c


def setup_db(conn, c):
    try:
        c.execute("SELECT id FROM employee")
    except sqlite3.OperationalError as error:
        if error.args[0] == "no such table: employee":
            c.execute(
                "CREATE TABLE department ("
                "id INTEGER PRIMARY KEY, name TEXT NOT NULL, "
                "UNIQUE(id, name))"
            )
            c.execute(
                "CREATE TABLE employee ("
                "id INTEGER PRIMARY KEY, name TEXT NOT NULL, "
                "pay INTEGER NOT NULL, department_id INTEGER NOT NULL, "
                "FOREIGN KEY(department_id) REFERENCES department(id) "
                "ON DELETE CASCADE)"
            )
            for data in [(1, "Sales"), (2, "Marketing")]:
                c.execute(
                    "INSERT INTO department (id, name) VALUES (?, ?)", data
                )
            for data in [
                (1, "Andrew", 90000, 1),
                (2, "Bennett", 70000, 2),
                (3, "Charlie", 70000, 1),
                (4, "Denis", 80000, 2),
                (5, "Ethan", 90000, 1),
            ]:
                c.execute(
                    "INSERT INTO employee (id, name, pay, department_id) "
                    "VALUES (?, ?, ?, ?)", data
                )
            conn.commit()
            return True
        conn.close()
        return False
    return True


def main():
    conn, c = connect()
    if not setup_db(conn, c):
        return

    try:
        query = (
            "SELECT employee.name, department.name, max_pay_table.max_pay "
            "FROM employee "
            "INNER JOIN department "
            "ON employee.department_id = department.id "
            "INNER JOIN "
            "(SELECT MAX(pay) AS max_pay, department_id "
            "FROM employee GROUP BY department_id) AS max_pay_table "
            "ON employee.pay = max_pay_table.max_pay AND "
            "employee.department_id = max_pay_table.department_id"
        )
        execute_query(conn, c, query)
    finally:
        conn.close()


main()
