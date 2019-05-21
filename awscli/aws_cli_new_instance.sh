#!/usr/bin/env bash

# Script to create new EC2 instance.
# See "Create Instance using script.md", parameter details.
# Authentication should be already setup using `aws configure`:


# Create new t2.micro instance


aws ec2 run-instances \
    --image-id ami-0b76c3b150c6b1423 \
    --count 1 \
    --instance-type t2.micro \
    --key-name MyKeyPair \
    --security-group-ids sg-0b11cc1753a0723a9 \
    --subnet-id subnet-0f661b84374cebe04


# display the Instance, IDs only
#
aws ec2 describe-instances --filters "Name=instance-state-code,Values=16" --query "Reservations[].Instances[].InstanceId"

# Attach an Elastic IP (EIP) to the instance.
# 
aws ec2 associate-address --instance-id "i-0f39b985b09561e4b" --public-ip 3.105.166.32

