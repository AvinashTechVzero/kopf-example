
import kopf
import datetime
from kubernetes import client, config

# @kopf.on.login()
# def login_fn(**kwargs):
#     return kopf.ConnectionInfo(
#         server='https://F92E6829B6B317B5EA4BAFC1EE0D4472.gr7.ap-south-1.eks.amazonaws.com',
#         # ca_path='~/.kube/config',
#         # ca_data=b'...',
#         # insecure=True,
#         # username='...',
#         # password='...',
#         # scheme='Bearer',
#         # token='...',
#         certificate_path='~/.kube/config',
#         private_key_path='~/.kube/client.key',
#         # certificate_data=b'...',
#         # private_key_data=b'...',
#         expiration=datetime.datetime(2099, 12, 31, 23, 59, 59),
#     )


# import kopf
config.load_kube_config()

@kopf.on.login()
def login_fn(**kwargs):
    return kopf.login_with_service_account(**kwargs) or kopf.login_with_kubeconfig(**kwargs)

@kopf.on.create('kopfexamples')
def create_fn(spec, **kwargs):
    print(f"And here we are! Creating: {spec}")
    return {'message': 'hello world'}  # will be the new status