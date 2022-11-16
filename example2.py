import kopf
import datetime
from kubernetes import client, config

config.load_kube_config()

@kopf.on.login()
def login_fn(**kwargs):
    return kopf.login_via_client(**kwargs)

@kopf.on.create('kopfexamples')
def create_fn(spec, **kwargs):
    print(f"And here we are! Creating: {spec}")
    return {'message': 'hello world 1'}  # will be the new status