# -*- coding: utf8 -*-

def updateDB(conn, data):
    cur = conn.cursor()
    try:
        with conn:
            sql = """ALTER DATABASE data_data CHARACTER SET utf8 COLLATE utf8_general_ci;"""
            cur.execute(sql)
    except:
        print('Базу data_data не создали')
    try:
        with conn:
            sql = """
                CREATE TABLE IF NOT EXISTS table_one (
                    date NOT NULL DEFAULT NOW(),
                    issue TEXT NOT NULL,
                    isin TEXT NOT NULL,
                    rating_agency TEXT NOT NULL,
                    rating_scale TEXT NOT NULL,
                    rating_value TEXT NOT NULL
                ) ENGINE=InnoDB
              """
            cur.execute(sql)
            cur.executemany("INSERT INTO table_one VALUES(?, ?, ?, ?, ?, ?);", data)
            conn.commit()
    except:
        print('Таблицу table_one не создали')

    try:
        with conn:
            sql = """
            CREATE TABLE IF NOT EXISTS tale_two(
                ID_RATING TIMESTAMP NOT NULL DEFAULT NOW(),
                ID_ISSUE TIMESTAMP NOT NULL DEFAULT NOW(),
                NAME_ISSUE TEXT NOT NULL,
                ISIN_ISSUE TEXT NOT NULL,
                NAME_RATING_AGENCY TEXT NOT NULL,
                NAME_RATING_SCALE TEXT NOT NULL,
                RATING_SYMBOL TEXT NOT NULL,
                DS TIMESTAMP NOT NULL DEFAULT NOW(),
                DE TIMESTAMP NOT NULL DEFAULT NOW()
                ) ENGINE=InnoDB
            """
            cur.execute(sql)
    except:
        print('Таблицу tale_two не создали')
