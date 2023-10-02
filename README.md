# pulumi-python-template

This is presently a repository utilized for simplifying the process for
developers to quickly get to what they do best - developing.
[Pulumi](https://www.pulumi.com/docs/) is a framework that
allows developers to use infrastructure as code (IaC) to version control
their cloud infrastructure deployments. There are so many great things about
pulumi, and we will get into those further on. I would argue its main selling
points are that it is open source under the Apache 2.0 License and that users
can write their infrastructure as code in the language of their choosing.
Languages currently offered include 
[node.js](https://www.pulumi.com/docs/languages-sdks/javascript/), 
[python](https://www.pulumi.com/docs/languages-sdks/python/), 
[Go](https://www.pulumi.com/docs/languages-sdks/go/), 
[.NET](https://www.pulumi.com/docs/languages-sdks/dotnet/), 
[Java](https://www.pulumi.com/docs/languages-sdks/java/), and 
[YAML](https://www.pulumi.com/docs/languages-sdks/yaml/).
The intent of this repository is to flesh out scripts and pulumi
[projects](https://www.pulumi.com/docs/concepts/projects/)/[stacks](https://www.pulumi.com/docs/concepts/stack/)
that create the basic infrastructure so that developers can develop on
containers within the cloud that come preconfigured to be able to deploy
their own infrastructure in the language that they choose.

This repository only supports the deployment based on the 
[docker.io/pulumi-python](https://hub.docker.com/r/pulumi/pulumi-python) 
image. This image supports pulumi via python. It is very simple to create a
repository in GitHub or elsewhere using this as a starting point for all of 
your infrastructure as code needs and running it from a dedicated pulumi-python
container in your environment

## Structure

[setup.py](./setup.py) is the script to use to deploy all of the infrastructure
necessary in your environment. This script relies on a YAML configuration file 
that is supplied by either the `-y` or `--yaml_file` argument. This YAML 
configuration file details information about the environment that the Azure 
resources will be deployed in. Examples of YAML configuration files can be 
found in the [config](../config/) directory.

The resources necessary for deployment include:
- Azure Resource Group (Already created)
- Azure Key Vault
  - Azure Encryption Key (for use in encrpyting pulumi secrets)
- Azure Storage Account 
  - Azure Storage Container (for use in housing state of resources deployed via pulumi)
  - Azure SAS Token (for use in authenticating to Storage Container for state management)

The Azure Key Vault, Azure Storage Account, Azure Storage Container, and Azure 
SAS Token need to be created before running pulumi. Pulumi is dependent on 
these resources for safe state management and safe-keeping of sensitive 
information. These resources, if not exist within the subscription are 
automatically deployed and referenced for use with pulumi.

## Development

Development can be done on your local machine through the use of a python 
virtual environment. To develop within a virtual environment, you will first 
need to ensure you have Python 3.9 or later installed as well as pip3. Once 
this is done, make sure you have python's virtual environment module installed.

```
$ pip3 install --upgrate virtualenv
```

Once this is complete, you can create a new python virtual environment by 
issuing the following command.

```
$ cd <repo root>
$ python3 -m venv <virtual-environment-name>
```

After the virtual environment is created, you can enable or activate the 
virtual environment by issuing the following command on linux:

```
$ source <virtual-environment-name>/bin/activate
```

And on windows:

```
> env/Scripts/Activate.ps1 // In Powershell
```

Once the virtual environment is up and running, you can install the 
[requirements](./requirements.txt) via the following command:

```
pip3 install -r ./requirements.txt
```

## YAML Configuration

The YAML configuration is used as the basis for deploying the resources 
necessary to support an Azure Container Instance running our custom pulumi 
deployment image. Basic templates for YAML configuration files can be found 
within the [config](./config/) directory. This YAML configuration has some 
rules to smoothly configure resources accordingly. The following lays out the 
structure of the overall YAML configuration file.

- environment
  - (required) The name of the environment (one of sandbox, zonec, zoneb, 
  zonea, or prod)
- stack_name
  - (required) The name of the stack to deploy. Anything you want 
- project_location
  - (required) The path to the directory of the pulumi project.
  - If this is not a full path, the `repo_root` must be passed to the 
  `PulumiConfig` class at creation time
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