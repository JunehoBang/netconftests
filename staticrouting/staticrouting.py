from ncclient import manager

eos = manager.connect(host="172.31.32.102", port="830",  timeout=500, username="admin", password="password",  hostkey_verify=False, device_params={'name':'default'})

add_snippet="""
<config>
    <static xmlns="http://pica8.com/xorplus/static-routes">
        <route>
            <name>10.1.0.1</name>
            <>
        </route>
    </static>
</config>
"""

get_snippet="""
<static xmlns="http://pica8.com/xorplus/static-routes">
    <route>
    </route>
</static>
"""

eos.get (filter=("subtree", get_snippet))
