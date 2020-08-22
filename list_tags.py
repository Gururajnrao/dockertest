import os
import json
import re
from datetime import datetime
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient


def run_example():
    """Resource Group management example."""
    #
    # Create the Resource Manager Client with an Application (service principal) token provider
    #
    subscription_id = os.environ.get(
        "AZURE_SUBSCRIPTION_ID", "11111111-1111-1111-1111-111111111111"
    )  # your Azure Subscription Id

    credentials = ServicePrincipalCredentials(
        client_id=os.environ["AZURE_CLIENT_ID"],
        secret=os.environ["AZURE_CLIENT_SECRET"],
        tenant=os.environ["AZURE_TENANT_ID"],
    )

    client = ResourceManagementClient(credentials, subscription_id)

    #
    # Managing resource groups
    #
    resource_group_params = {"location": "westus"}

    # List Resources 
    print("List Resources")
    for item in client.resources.list(filter="tagName eq 'autoscalegroup_name' and tagValue eq 'b109-azure-eastus2-region-asg1'"):
      print("\tName: {}".format(item.name))
      print("\tId: {}".format(item.id))
      print("\tLocation: {}".format(item.location))
      print("\tTags: {}".format(item.tags))
      print_properties(item.properties)
      vm_type = "Microsoft.Compute/virtualMachines"
      match = re.findall("%s" % vm_type, item.id)
      print ("Value of Match {}".format(match))
      if (match !=[]):
        print ("VM name:{}".format(item.name))
        vm_name=item.name
        return vm_name

def print_properties(props):
    """Print a ResourceGroup properties instance."""
    if props and props.provisioning_state:
        print("\tProperties:")
        print("\t\tProvisioning State: {}".format(props.provisioning_state))
    print("\n\n")




if __name__ == "__main__":
    run_example()
