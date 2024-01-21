def updateserverconf(filepath, key, value):
    with open(filepath, 'r') as file:
        readlines = file.readlines()

# Update the file
    with open(filepath, 'w') as file:
        for line in readlines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


file_location = "server.conf"
key_to_update = "MAX_CONNECTIONS"
value_to_update = "5000"

updateserverconf(file_location, key_to_update, value_to_update)
