#!/usr/bin/env python3

# Security Group  Parameters:
#     id (string) -- The SecurityGroup's id identifier. This must be set.
# resource's available identifiers:
#     id
#
# resource's available attributes:
#
#     description
#     group_id
#     group_name
#     ip_permissions
#     ip_permissions_egress
#     owner_id
#     tags
#     vpc_id
#
# These are the resource's available actions:
#
#     authorize_egress()
#     authorize_ingress()
#     create_tags()
#     delete()
#     get_available_subresources()
#     load()
#     reload()
#     revoke_egress()
#     revoke_ingress()

import boto3

ec2 = boto3.resource("ec2")
security_group = ec2.SecurityGroup("id")
security_group = ec2.SecurityGroup("ssh-inbound")

# look at some attributes for existing SG 'ssh-inbound'
print(security_group.id)
print(security_group.group_id)
print(security_group.meta)

security_group.authorize_ingress(
    IpProtocol="tcp", CidrIp="0.0.0.0/0", FromPort=80, ToPort=80
)

security_group.reload
