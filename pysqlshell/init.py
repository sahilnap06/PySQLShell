"""Plugin registration

This file is automatically loaded by the MySQL Shell at startup time.

It registers the plugin objects and then imports all sub-modules to
register the plugin object member functions.
"""

from mysqlsh.plugin_manager import plugin

# Create a class representing the structure of the plugin and use the
# @register_plugin decorator to register it
@plugin
class pysqlshell:
    """Plugin to manage the Python Connector for MySQL Shell Service.

    This global object exposes a list of shell extensions
    to work with the MySQLShell using Python.
    """

    def __init__(self):
        """Constructor that will import all relevant sub-modules

        The constructor is called by the @plugin decorator to
        automatically register all decorated functions in the sub-modules
        """
        # Import all sub-modules to register the decorated functions there
        import pysqlshell

    class dba():
        """Used to interact with the DBA global-object of MySQL Shell.

        A collection of functions to interact with the DBA object and
        attributes.
        """
