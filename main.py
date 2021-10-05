# -*- coding: utf-8 -*-
import sqlite3
from data_frames import megadda

conn = sqlite3.connect('table.db')
cur = conn.cursor()


def create_table_one(data, conn, cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS general_table(
        date,
        issue,
        isin,
        rating_agency,
        rating_scale,
        rating_value
        );
        """)
    cur.executemany("INSERT INTO general_table VALUES(?, ?, ?, ?, ?, ?);", data)
    conn.commit()

def scrap_data(conn, cur):
    cur.execute("SELECT * FROM general_table;")
    a = cur.fetchall()
    conn.commit()
    return a
data = megadda
create_table_one(data, conn, cur)
a=scrap_data(conn, cur)
print(a)
# cur.execute(
#     """
#     CREATE TABLE IF NOT EXISTS tale_two(
#     ID_RATING,
#     ID_ISSUE,
#     NAME_ISSUE,
#     ISIN_ISSUE,
#     NAME_RATING_AGENCY,
#     NAME_RATING_SCALE
#     );
#     """)
# conn.commit()
#
# cur.executemany("INSERT INTO tale_two VALUES(?, ?, ?, ?, ?, ?);", a)
# a = cur.fetchall()
# print(a)
# conn.commit()
