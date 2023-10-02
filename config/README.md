# config

This directory houses the YAML configuration files to be used as the basis for 
deploying in your subscription. These YAML files are input to the 
[setup.py](../../initialize/setup.py) script and contain the configuration 
necessary to set up the resources for deploying an Azure Container Instance 
capable of running pulumi in your subscription. 

There are numerous directories in this folder that can be referenced for 
your deployment into different areas, but the important information regarding 
the format of the YAML configuration files can be found below. The YAML 
configuration is used as the basis for deploying the resources necessary to 
support an Azure Container Instance running our custom pulumi deployment image.
Basic templates for YAML configuration files can be found within this 
directory. This YAML configuration has some rules to smoothly configure 
resources accordingly. The following lays out the structure of the overall YAML
configuration file.

- environment
  - (required) The name of the environment (one of sandbox, zonec, zoneb, 
  zonea, or prod)
- stack_name
  - (required) The name of the stack to deploy. Anything you want 
- project_location
  - (required) The full filepath to the directory of the pulumi project.
- storage_account
  - (required) The configuration object that specifies information about the 
  storage account used with pulumi
  - resource_group
    - (optional) The name of the resource group that the Azure Key Vault 
    resides in
  - storage_container
    - (required) The configuration block of the Storage Account Blob Container 
    that is used with pulumi
    - name
      - (required) The name of the Storage Account Blob Container
  - sas_token
    - (optional) The configuration block of the SAS token to be created/used 
    with pulumi to access Storage Account Blob Container
    - name 
      - (required) If this block is declared, the name of the SAS token must be
      declared
- key_vault
  - (required) The configuration object that specifies information about the 
  Azure Key Vault used with pulumi
  - resource_group
    - (optional) The name of the resource group that the Azure Key Vault 
    resides in
- pulumi
  - (required) Configuration block that contains a dictionary of all the 
  configuration parameters required by your pulumi scripts
  - If no resource_group_name is specified, the first resource group returned 
  in the list from the subscription will be used for resource_group_name and 
  resource_group_id config items
  - If no storage_account_name is specified, the storage account from the 
  config above will be used for the storage_account_name and storage_account_id
  config items
  - If no key_vault_name is specified, the key vault name and ID from the 
  config above will be used for the key_vault_name and key_vault_id config 
  items
- pulumi-secrets
  - (optional) Configuration block that contains key/value pairs of all the 
  secret configuration parameters required by your pulumi scripts
  