from ncclient import manager

eos = manager.connect(host="172.31.32.102", port="830",  timeout=500, username="admin", password="password",  hostkey_verify=False, device_params={'name':'default'})

add_snippet="""
<config>
    <static xmlns="http://pica8.com/xorplus/static-routes">
        <route>
            <name>10.1.0.0/16</name>
            <next-hop>10.10.0.21</next-hop>
        </route>
    </static>
</config>
"""

eos.edit_config(target="running", config=add_snippet, default_operation="merge")

get_snippet="""
<static xmlns="http://pica8.com/xorplus/static-routes">
    <route>
    </route>
</static>
"""

eos.get (filter=("subtree", get_snippet))
