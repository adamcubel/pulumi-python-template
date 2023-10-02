import pulumi

from pulumi_azure_native import resources
from pulumi_azure_native import storage

config = pulumi.Config()
subscription = config.require('subscription')
resource_group_id = config.require('resource_group_id')
resource_group_name = config.get('resource_group_name')
storage_account_id = config.require('storage_account_id')
storage_account_name = config.get('storage_account_name')
key_vault_id = config.require('key_vault_id')
key_vault_name = config.get('key_vault_name')

###############################################################################
# Configure your infrastructure below
###############################################################################

# Set up the Resource Group
resource_group = resources.ResourceGroup.get(resource_name=resource_group_name, id=resource_group_id)

# Setup the storage account
storage_account = storage.StorageAccount.get(resource_name=storage_account_name, id=storage_account_id)


# Provide the Resource Group as an output
pulumi.export("Resource Group Name", resource_group.name)

# Provide the Storage Account as an output
pulumi.export("Resource Group Name", storage_account.name)