"""Sub-Module to work with instance-level entities"""

from api.main import PySQLShellApp

@PySQLShellApp.post('/instance/{instance_id}/check_config')
def check_instance_configuration(instance_id):
    """
    """
    pass

@PySQLShellApp.post('/instance/{instance_id}/configure')
def configure_instance():
    """Used to configure a MySQL instance with the settings required to per use in an InnoDB cluster
    
    Args:
        session (object): The database session to use.
    """
    pass

@PySQLShellApp.post('/instance/{instance_id}/local/configure')
def configure_local_instance():
    """
    """
    pass

@PySQLShellApp.post('/instance/{instance_id}/sandbox/deploy')
def deploy_sandbox_instance():
    """
    """
    pass

@PySQLShellApp.post('/instance/{instance_id}/sandbox/start')
def start_sandbox_instance():
    """
    """
    pass

@PySQLShellApp.post('/instance/{instance_id}/sandbox/delete')
def delete_sandbox_instance():
    """
    """
    pass

@PySQLShellApp.post('/instance/{instance_id}/sandbox/stop')
def stop_sandbox_instance():
    """
    """
    pass

@PySQLShellApp.delete('/instance/{instance_id}/sandbox/stop')
def kill_sandbox_instance():
    """
    """
    pass
