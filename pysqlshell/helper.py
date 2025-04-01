import re
import socket
from pysqlshell.exceptions import UserIncorrectlyFormattedException, InvalidConfigurationException

USER_INPUT_VALIDATION = r"^([a-zA-Z0-9._%+-]+):([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9._%+-]+):([0-9]{1,5})$"

def is_valid_host(address: str) -> bool:
    """
    Validates whether the given address is a valid IP/hostname and checks if it is reachable.
    
    :param address: The IP address or hostname to validate.
    :return: True if the address is valid and reachable, False otherwise.
    """
    try:
        # Try to resolve the hostname/IP address
        socket.gethostbyname(address)
        
        # Try to establish a connection on port 80 (HTTP) to check reachability
        with socket.create_connection((address, 80), timeout=2):
            return True
    except (socket.gaierror, socket.timeout, OSError):
        return False
    
    return False

def validate_user_input_str(input_str: str) -> None:
    """Helper function to validate if the input string is in valid format.
    
    Valid format: `user:password@host:port`

    :return: True if the string is in a valid format.
    """
    try:
        match = re.match(USER_INPUT_VALIDATION, input_str)
        if match:
            port = int(match.group(4))
            return 0 <= port <= 65535
        return False
    except Exception as ex:
        raise ex
