#!/usr/bin/env python3


import boto3


# Resource is a higher level wrapper
ec2 = boto3.resource("ec2")

# Client is a low level wrapper
client = boto3.client("ec2")

response = client.describe_instances()
# print (response)


for r in response["Reservations"]:
    print("-" * 80)
    print(type(r["Instances"]))
    print(len(r["Instances"]['ImageId'))
