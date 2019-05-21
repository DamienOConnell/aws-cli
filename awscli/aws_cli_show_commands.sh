#!/usr/bin/env bash

# Authentication should be already setup using `aws configure`:


echo "listing all current instances ..... "
aws ec2 describe-instances --filters "Name=instance-state-code,Values=16" --query "Reservations[].Instances[].InstanceId"


echo "listing all current instances, json format ..... "
aws ec2 describe-instances --filters "Name=instance-state-code,Values=16" --query "Reservations[].Instances[].InstanceId" --output text

