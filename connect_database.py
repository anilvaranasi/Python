from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'D:\ANIL\VSCode\python_project\secure-connect-Varanawesomenow.zip'
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