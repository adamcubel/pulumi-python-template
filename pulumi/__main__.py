import pulumi

from pulumi_azure import core
from pulumi_azure_native import keyvault
from pulumi_azure_native import network
from pulumi_azure_native import resources
from pulumi_azure_native import storage

# Client configuration params
client_config = core.get_client_config()
tenant_id = client_config.tenant_id
current_principal = client_config.object_id

config = pulumi.Config()

# Default configuration that is provided to pulumi
environment = config.require('environment')
subscription = config.require('subscription')
resource_group_id = config.require('resource_group_id')
resource_group_name = config.require('resource_group_name')
storage_account_id = config.require('storage_account_id')
storage_account_name = config.require('storage_account_name')
storage_account_resource_group_name = config.require('storage_account_resource_group_name') or resource_group_name
key_vault_id = config.require('key_vault_id')
key_vault_name = config.require('key_vault_name')
key_vault_resource_group_name = config.require('key_vault_resource_group_name') or resource_group_name

# Application Specific configuration below

###############################################################################
# Configure your infrastructure below
###############################################################################

# Set up the Resource Group
resource_group = resources.ResourceGroup.get(resource_name=resource_group_name, id=resource_group_id)

# Setup the storage account
storage_account = storage.StorageAccount.get(resource_name=storage_account_name, id=storage_account_id)

# Setup the Azure Key Vault
key_vault = keyvault.Vault.get(resource_name=key_vault_name, id=key_vault_id)

# Provide the Resource Group as an output
pulumi.export("Resource Group Name", resource_group.name)

# Provide the Storage Account as an output
pulumi.export("Storage Account Name", storage_account.name)