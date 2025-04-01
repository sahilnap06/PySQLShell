"""Sub-Module to work with instance-level entities"""

from api.main import PySQLShellApp

@PySQLShellApp.delete('/metadata/{meta_id}/check_config')
def dba_check_instance_configuration(instance_id):
    """
    """
    pass

@PySQLShellApp.post('/metadata/{meta_id}/upgrade')
def dba_configure_instance():
    """Used to configure a MySQL instance with the settings required to per use in an InnoDB cluster
    
    Args:
        session (object): The database session to use.
    """
    pass
