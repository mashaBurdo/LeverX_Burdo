import sys
from db_creators import get_in_db, create_indexes, fill_rooms, fill_students
from db_queries_executors import DbConnector, QueryExecuter, DataFetcher
from db_queries import create_students_table, create_rooms_table, fetch_queries
from files_processors import XmlUploader, JsonUploader, JsonLoader, Parser


if __name__ == "__main__":

    parser = Parser().create_parser()
    namespace = vars(parser.parse_args(sys.argv[1:]))
    file_extention_uploader = {'json': JsonUploader, 'xml': XmlUploader}

    connection = DbConnector(namespace['hostname'], namespace['username'], namespace['userpassword']).create_connection()
    get_in_db(connection)

    QueryExecuter(connection, create_students_table).execute_query()
    fill_students(connection, namespace['students'])

    QueryExecuter(connection, create_rooms_table).execute_query()
    fill_rooms(connection, namespace['rooms'])

    create_indexes(connection)

    for name, query_string, transform_to_dict in fetch_queries:
        query_result = DataFetcher(connection, query_string).fetch_data()
        if transform_to_dict:
            query_result = [{'room': s[0], 'students': s[1]} for s in query_result]
        file_extention_uploader[namespace['format']](query_result, name).create_file()

    connection.close()

# Command example: python task_4.py -s students.json -r rooms.json -f xml -hn localhost -un masha -up S
