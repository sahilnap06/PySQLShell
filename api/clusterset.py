from api.main import PySQLShellApp

@PySQLShellApp.get('/clusterset')
async def get_cluster_set():
    # return cluster.get_cluster(cluster_name)
    return {"message": "Not yet implemented"}

