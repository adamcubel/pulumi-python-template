# pulumi

This folder includes all of the files necessary to create infrastructure
in your subscription via pulumi. While it is possible to deploy the resources 
in this pulumi project directly, it is recommended to call the 
[setup.py](../setup.py) script from within the deployment container.

A complete list of resources used/created in the subscription can be seen by 
running the `pulumi plan` command. This will also be shown when executing the 
[setup.py](../setup.py) script. This script sets up all of the infrastructure 
necessary to run pulumi with a self-hosted backend in an Azure Storage Account 
Container and secrets encrypted via an Azure Key Vault Key. From there, the 
setup.py script sets up the pulumi stack, configures the stack, and creates the 
stack upon user confirmation. The pulumi operations to deploy the resources 
declared within [__main__.py](./__main__.py) are executed from the 
[setup.py](../setup.py) script an the 
[pulumi-automation-utils](https://pypi.org/project/pulumi-automation-utils/) 
module. 

To learn more about how these scripts work together, please see this 
[README](../README.md).