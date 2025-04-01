from api.main import PySQLShellApp


@PySQLShellApp.get('/replica_set/{replica_set_name}')
def dba_get_replica_set():
    """Used to obtain the information about the replica set.
    """
    pass

@PySQLShellApp.post('/replica_set/{replica_set_name}')
def dba_create_replica_set(name: str, **kwargs):
    pass


@PySQLShellApp.post('/replica_set/{replica_set_name}/configure')
def dba_configure_replica_set_instance():
    """Used to configure a MySQL instance with the settings to
        use it in a Replica Set
    """
    pass
