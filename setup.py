#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
import yaml

from pulumi_automation_utils import common
from pulumi_automation_utils.login_config import LoginConfig
from pulumi_automation_utils.pulumi_config import PulumiConfig

REPO_DIRECTORY = os.path.abspath(os.getcwd())

def main(args : dict):
    if "yaml_file" in args.keys():
        # Get the configuration stored within the YAML file
        yaml_vars = common.parse_yaml_file(args['yaml_file'])
        
        # Write out the configuration to the console
        print("")
        yaml.dump(yaml_vars, sys.stdout)
        print("")

        # Setup the login config and the pulumi config
        login_config = LoginConfig(yaml_vars)
        pulumi_config = PulumiConfig(
                            login_config=login_config, 
                            yaml_vars=yaml_vars,
                            repo_root=REPO_DIRECTORY)
        
        # If not already logged into Azure CLI, login
        if not login_config.is_logged_in():
            login_config.login_to_azure()
        
        # Configure and deploy pulumi IaC
        try:
            pulumi_config.configure_pulumi()
            pulumi_config.deploy_pulumi()        
        except subprocess.CalledProcessError as e:
            print("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
            exit()
    else:
        exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--yaml_file", required=True, help = "Location of the YAML file for deployment")
    args = parser.parse_args()
    main(vars(args))