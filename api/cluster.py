from api.main import PySQLShellApp

@PySQLShellApp.get('/cluster/{cluster_name}')
async def get_cluster(cluster_name):
    # return cluster.get_cluster(cluster_name)
    return {"message": "Not yet implemented"}


@PySQLShellApp.post('/cluster/{cluster_name}')
async def create_cluster(cluster_name):
    return {"message": "Not yet implemented"}

@PySQLShellApp.post('/cluster/{cluster_name}/reboot')
async def reboot_cluster_from_complete_failure(cluster_name):
    return {"message": "Not yet implemented"}
