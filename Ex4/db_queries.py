import pymysql


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
        except pymysql.Error as e:
            return ("Could not close connection error pymysql %d: %s" % (e.args[0], e.args[1]))

        return connection


class Executer():
    '''Base class for query execution'''
    def __init__(self, connection, query):
        self.connection = connection
        self.query = query


class QueryExecuter(Executer):
    '''Class for one query executiov'''
    def execute_query(self):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(self.query)
                self.connection.commit()
            except pymysql.Error as e:
                print("The error %d occurred: %s" % (e.args[0], e.args[1]))


class QueriesExecuter(Executer):
    '''Class for many query executions'''
    def execute_queries(self, val):
        with self.connection.cursor() as cursor:
            try:
                cursor.executemany(self.query, val)
                self.connection.commit()
            except pymysql.Error as e:
                print("The error %d occurred: %s" % (e.args[0], e.args[1]))


class DataFetcher(Executer):
    '''Class for data fetching'''
    def fetch_data(self):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(self.query)
                data = cursor.fetchall()
                return data
            except pymysql.Error as e:
                print("The error %d occurred: %s" % (e.args[0], e.args[1]))
