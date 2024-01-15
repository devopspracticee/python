def update_server_conf(file_path, key, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

# Updating the file
    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


file_location = "server.conf"
key_to_update = "MAX_CONNECTIONS"
max_value = "1200"

update_server_conf(file_location, key_to_update, max_value)
