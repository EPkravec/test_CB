# -*- coding: utf8 -*-
import sqlite3
from go import updateDB
from data_frames import megadda


conn = sqlite3.connect('data_data.db')
updateDB(conn, megadda)