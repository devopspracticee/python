ec2_instances = [
    {
        "id": "instance-1",
        "type": "t2.micro"
    },
    {
        "id": "instance-2",
        "type": "t2.medium"
    },
    {
        "id": "instance-3",
        "type": "t2.large"
    }
]

print(ec2_instances[2]["type"])
