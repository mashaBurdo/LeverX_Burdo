import pymysql
import logging


class DbConnector:
    '''Class for data base connection'''
    def __init__(self, host_name, user_name, user_password):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password

    def create_connection(self):
        connection = None
        try:
            connection = pymysql.connect(
                host=self.host_name,
                user=self.user_name,
                password=self.user_password
            )
        except Exception:
            logging.exception('Connection failed')

        return connection


class Executer():
    '''Base class for query execution'''
    def __init__(self, connection, query, val=None):
        self.connection = connection
        self.query = query
        self.val = val


class QueryExecuter(Executer):
    '''Class for query execution'''
    def execute_query(self):
        with self.connection.cursor() as cursor:
            try:
                if self.val is not None:
                    cursor.executemany(self.query, self.val)
                else:
                    cursor.execute(self.query)
                self.connection.commit()
            except Exception:
                logging.exception('Query execution failed')


class DataFetcher(Executer):
    '''Class for data fetching'''
    def fetch_data(self):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(self.query)
                data = cursor.fetchall()
                return data
            except Exception:
                logging.exception('Data fetching failed')
