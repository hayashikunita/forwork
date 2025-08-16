# test_database.py
import pytest
import sqlite3

@pytest.fixture
def db_connection():
  conn = sqlite3.connect(':memory:')
  yield conn
  # 終わったらクローズ   
  conn.close()

def test_db_operation(db_connection):
  c = db_connection.cursor()
  c.execute('''CREATE TABLE users (id int, name text)''')
  c.execute("INSERT INTO users VALUES (1, 'John')")
  db_connection.commit()

  c.execute('SELECT * FROM users WHERE id=1')
  row = c.fetchone()
  assert row == (1, 'John')
