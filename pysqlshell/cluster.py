"""Sub-Module to work with cluster-level entities"""

from mysqlsh.plugin_manager import plugin_function
from pysqlshell.constants import DB_TYPE_MYSQL

@plugin_function("pysqlshell.dba.get_cluster", web=True, shell=False, cli=False)
def dba_get_cluster(session=None):
    """Returns status information about the current GenAI setup

    Args:
        session (object): The database session to use.

    Returns:
        A dict holding the status information
    """
    if session.database_type != DB_TYPE_MYSQL:
        return {
            "heatwave_support": False,
            "local_model_support": False,
            "language_support": False
        }

    heatwave_support = False
    local_model_support = False
    language_support = False

    