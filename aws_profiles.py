#!/usr/bin/env python3
"""
Creates a new shell with AWS environment varibles set to chosen profile/region
"""

import configparser, os, pty
from pick import pick

# Define aws credentials file $HOME/.aws/credentials
creds_file = os.path.join(os.environ['HOME'], ".aws", "credentials")

# Parse the credentials file
config = configparser.ConfigParser()
config.read(creds_file)
# have the user select an aws profile
aws_profile, index = pick(config.sections(), "Select an AWS profile")
# Have the user select an aws region
aws_region, index = pick(["us-east-1", "us-east-2", "us-west-1", "us-west-2"], "Select an AWS region")
# Set the required env variables
os.environ["AWS_PROFILE"] = aws_profile
os.environ["AWS_DEFAULT_REGION"] = aws_region
#os.environ["PS1"] = f"({aws_profile}){os.environ['PS1']}"
# Spawn a new bash shell
pty.spawn("/bin/bash")
