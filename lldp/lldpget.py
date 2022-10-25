from ncclient import manager

eos = manager.connect(host="172.31.32.102", port="830",  timeout=500, username="admin", password="password",  hostkey_verify=False, device_params={'name':'default'})


get_snippet = """
<lldp>
</lldp>
"""

eos.get (filter=("subtree", get_snippet))

