import yampy

import ConfigParser

my_ini_path = 'authentication.ini'

with open(my_ini_path) as f:
    client_id = ConfigParser.ConfigParser(my_ini_path)
    
print client_id
