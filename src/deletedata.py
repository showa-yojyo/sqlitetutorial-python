import sys
from connection import create_connection


def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main(database):
    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_task(conn, 2);
        # delete_all_tasks(conn);


if __name__ == '__main__':
    main(sys.argv[1])
