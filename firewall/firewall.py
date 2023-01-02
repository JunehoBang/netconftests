from ncclient import manager

eos = manager.connect(host="172.31.32.101", port="830",  timeout=500, username="admin", password="password",  hostkey_verify=False, device_params={'name':'default'})

# add_snippet = """
# <config>
#    <vxlans xmlns="http://pica8.com/xorplus/vxlans">
#         <source-interface>
#             <name>loopback</name>
#             <address>5.5.5.5</address>
#         </source-interface>
#         <udp-port>6000</udp-port>
#    </vxlans>
# </config>
# """

add_snippet="""
<config>
    <firewall xmlns="http://pica8.com/xorplus/firewall">
        <filter>
            <name>MyFilter</name>
        </filter>
    </firewall>
</config>
"""

eos.edit_config(target="running", config=add_snippet, default_operation="merge")
