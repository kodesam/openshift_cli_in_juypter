To run all the OpenShift CLI `oc get` status commands to fetch the status of various resources, you can use the OpenShift client library like `openshift` in Python. Here's an example code snippet:

```python
from openshift.dynamic import DynamicClient
from kubernetes import client, config

# Load OpenShift cluster configuration
config.load_kube_config()

# Create a dynamic OpenShift client
oc_client = DynamicClient(client.ApiClient())

def run_get_status_cmds():
    # Define the list of resources to check
    resources = [
        "pods",
        "deployments",
        "services",
        # Add more resources as needed...
    ]

    for resource in resources:
        run_get_status_cmd(resource)

def run_get_status_cmd(resource):
    print(f"Fetching {resource} status...\n")

    # Execute 'oc get' command using dynamic client
    cmd = oc_client.resources.get(api_version='v1', kind=resource).get()
    items = cmd.items
    if not items:
        print("No resources found")
    else:
        for item in items:
            print(f"Name: {item.metadata.name}")
            print(f"Status: {item.status.phase}")
            print("\n")
            
    print("\n")

# Call the function
run_get_status_cmds()
```

This code creates a dynamic OpenShift client using the `openshift.dynamic` library and loads the cluster configuration using the `kubernetes` library. It defines a function `run_get_status_cmds()` that iterates over a list of resources and calls the `run_get_status_cmd()` function for each resource.

The `run_get_status_cmd()` function executes an `oc get` command for the specified resource using the dynamic client and prints the name and status of each resource found.

To run this code, make sure you have the necessary Python libraries installed (`openshift`, `kubernetes`) and the correct cluster configuration. Then, copy the code into a Jupyter notebook cell and execute the cell. The status of the specified resources will be displayed in the notebook's output. You can add more resources to the `resources` list as needed.