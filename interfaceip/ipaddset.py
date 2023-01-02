from ncclient import manager

eos = manager.connect(host="172.31.32.101", port="830",  timeout=500, username="admin", password="password",  hostkey_verify=False, device_params={'name':'default'})

set_snippet = """
<config>
    <interface xmlns="http://pica8.com/xorplus/interface">
        <gigabit-ethernet>
            <name>ge-1/1/6</name>
            <family>
                <ethernet-switching>
                    <vlan>
                        <members>
                            <id>2</id>
                        </members>
                        <members>
                            <id>3</id>
                        </members>      
                    </vlan>
                </ethernet-switching>
            </family>
        </gigabit-ethernet>
    </interface>
</config>
"""

eos.edit_config(target="running", config=set_snippet, default_operation="merge")


set_snippet = """
<config>
    <vlan-interface xmlns="http://pica8.com/xorplus/vlan-interface">
        <interface>
            <name>vlan-3</name>
            <vif>
                <name>vlan-3</name>
                <address>
                    <name>12.0.0.22</name>
                    <prefix-length>24</prefix-length>
                </address>
            </vif>
        </interface>
    </vlan-interface>
</config>
"""

eos.edit_config(target="running", config=set_snippet, default_operation="merge")



set_snippet="""
<config>
    <vlans xmlns="http://pica8.com/xorplus/vlans">
        <vlan-id>
            <id>3</id>
            <l3-interface>vlan-3</l3-interface>
        </vlan-id>
    </vlans>
</config>
"""

eos.edit_config(target="running", config=set_snippet, default_operation="merge")