import boto3

# Initialize an instance of boto3 for access to AWS SSM Parameter Store.
ssm_client = boto3.client("ssm", region_name="us-east-1")


# Define a function for recover the values of AWS SSM Parameter Store.
def get_parameter(parameter_name):
    response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
    return response["Parameter"]["Value"]
