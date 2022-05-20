from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import ulid

from openapi_server.models.employee import Employee

def get_session(host):
    cluster = Cluster([host])
    session = cluster.connect()
    session.row_factory = dict_factory
    return session

class CassandraConnector():
    def __init__(self):
        self.host = 'db_employee'
        session = get_session(self.host)
        # create keyspace
        session.execute(
            "CREATE KEYSPACE IF NOT EXISTS employee \
            WITH REPLICATION = { \
            'class' : 'SimpleStrategy', 'replication_factor' : '1' \
            };"
        )
        # create table
        session.execute(
            "CREATE TABLE IF NOT EXISTS employee.info \
            (id text PRIMARY KEY, name text, attr text);"
        )

    def create(self, data):
        id = ulid.new().str
        name = data.name
        attr = data.attr

        session = get_session(self.host)
        session.execute(
            "INSERT INTO employee.info (id, name, attr) \
            VALUES ('{0}', '{1}', '{2}');".format(id, name, attr)
        )
        return Employee(id=id, name=name, attr=attr)
    
    def read(self):
        session = get_session(self.host)
        r = session.execute(
            "SELECT id, name, attr FROM employee.info;"
        )
        return [Employee(**params) for params in r]
    
    def get_by_id(self, id):
        session = get_session(self.host)
        r = session.execute(
            "SELECT id, name, attr FROM employee.info \
            WHERE id = '{}';".format(id)
        )
        return Employee(**r.one())

    def update(self, id, data):
        name = data.name
        attr = data.attr

        session = get_session(self.host)
        r = session.execute(
            "Update employee.info \
            SET name = '{0}', attr = '{1}' \
            WHERE id = '{2}';".format(name, attr, id)
        )
        return Employee(id=id, name=name, attr=attr)

    def delete(self, id):
        session = get_session(self.host)
        r = session.execute(
            "DELETE FROM employee.info \
            WHERE id = '{}';".format(id)
        )
