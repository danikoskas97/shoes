import psycopg2


def connect():
  return psycopg2.connect(user='solal', password='root', database='learning1', host='localhost')
