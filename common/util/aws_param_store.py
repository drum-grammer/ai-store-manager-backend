import boto3


def get_config_from_param_store(param_name: str, with_description: bool = True) -> str:
    region = boto3.session.Session().region_name
    ssm = boto3.client('ssm', region)
    parameter = ssm.get_parameter(
        Name=param_name,
        WithDecryption=with_description,
    )

    return parameter['Parameter']['Value']
