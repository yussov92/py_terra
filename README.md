## Description
Python wrapper for Terraform client. Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently.
terraform is a tool made by Hashicorp, https://terraform.io/

## Dependences
* python 3.6.8
* asyncio

## Examples
```
# option -auto-approve is true by default
tf = Terraform('/path/to/terraform_config')
# initialize terraform directory
tf.init()
# create an execution plan
tf.plan()
# apply the changes required to reach the desired state of the configuration
tf.apply()
# return output info (json format or text format), 
# if you don't specify a resource it outputs everything from output
tf.output(frmt='json', resource=instance_1)
# destroy all
tf.destroy()
```
