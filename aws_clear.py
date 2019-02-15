#!/usr/bin/env python3
import os, configparser, sys

def print_help():
    print("wipes the contents of a profile. Designed to be used with saml2aws")
    print(f"usage: {sys.argv[0]} [profile_name]")
    print(f"      default profile name = \"{profile}\"")

try:
    profile = sys.argv[1]
except:
    profile = "saml"

# Define aws credentials file $HOME/.aws/credentials
creds_file = os.path.join(os.environ['HOME'], ".aws", "credentials")

# Create a config parser
config = configparser.ConfigParser()

# read the config file
config.read(creds_file)

# back up the creds file
bak_file = creds_file + ".bak"
print(f"Backing up creds file: {creds_file} to: {bak_file}")
with open(bak_file, 'w') as configfile:
    config.write(configfile)

# wipe out the named profile (saml by default)
config[profile] = {}

# Write the config file
print(f"Removing profile: {profile} from: {creds_file}")
with open(creds_file, 'w') as configfile:
    config.write(configfile)
