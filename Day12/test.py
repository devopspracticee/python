def server_configuation(file_path, key, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

# Update the configuration of the file
    with open(file_path, 'w') as file:
        for line in lines:
            if key in lines:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '1000'  # New maximum connections allowed

# Update the server configuration file
server_configuation(server_config_file, key_to_update, new_value)
