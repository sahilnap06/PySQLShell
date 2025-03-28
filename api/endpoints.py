from fastapi import FastAPI
# from pysqlshell.lib import cluster

PySQLShellApp = FastAPI()

@PySQLShellApp.get('/clusters/{cluster_name}')
async def get_clusters(cluster_name):
    # return cluster.get_cluster(cluster_name)
    return {"message": "Not yet implemented"}


@PySQLShellApp.post('/clusters/{cluster_name}')
async def get_clusters(cluster_name):
    # return cluster.get_cluster(cluster_name)
    return {"message": "Not yet implemented"}


@PySQLShellApp.post("/instance/{instance_name}/configure")
async def get_clusters(cluster_name):
    # return cluster.get_cluster(cluster_name)
    return {"message": "Not yet implemented"}

# @PySQLShellApp.post("/instance/{}")