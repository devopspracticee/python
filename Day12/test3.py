def server_conf_update(file_path, key, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Update the file
    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:  # Che
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


update_file = 'server.conf'
key_to_update = 'MAX_CONNECTIONS'
new_value = '2000'

server_conf_update(update_file, key_to_update, new_value)
