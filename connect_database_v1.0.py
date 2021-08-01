#Location of database https://astra.datastax.com/org/e3643ed3-6da6-4252-9d37-1b22eea7d708/database/66964d1a-482d-4b55-a552-a50a2a148924/connect
#Location of key   https://astra.datastax.com/org/e3643ed3-6da6-4252-9d37-1b22eea7d708/settings/tokens
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'D:\ANIL\VSCode\Python\secure-connect-Varanawesomenow.zip'
}
client_id='wJlosGCAeWYGLyZBUIlYEKcv'
client_secret='IsZ8E8C8vHmYLjEEezRdoZIL0ciW1DifpsUH63R,gu3DiypHP47v.3ZkwR3Qd3Hkb4JMZlHALGBUgML5oWaEMfOLGaDRKMNKqlyS+048jHgN+L6_G,QAU9,8rQ78Ati+'
auth_provider = PlainTextAuthProvider(client_id, client_secret)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")