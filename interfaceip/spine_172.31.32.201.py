#               +--------------------------------------------+
#               |          172.31.32.201 switch              |
#               +--------------------------------------------+
#                |                    |                    |
#             ge-1/1/5           ge-1/1/6               ge-1/1/7
# vlan-id:     101                104                    105
# vlan-itf:  vlan-101           vlan-104               vlan-105
# ip-add:    10.10.0.13/30       10.10.0.17/30         10.10.0.21/30
#  


from ncclient import manager

eos = manager.connect(host="172.31.32.201", port="830",  timeout=500, username="admin", password="password",  hostkey_verify=False, device_params={'name':'default'})

# vlan creation and vlan-interface assignment
set_snippet = """
<config>
   <vlans xmlns="http://pica8.com/xorplus/vlans">
      <vlan-id>
         <id>104</id>
         <l3-interface>vlan-101</l3-interface>
      </vlan-id>
      <vlan-id>
         <id>105</id>
         <l3-interface>vlan-105</l3-interface>
      </vlan-id>
   </vlans>
</config>
"""

set_snippet = """
<config>
   <vlans xmlns="http://pica8.com/xorplus/vlans">
      <vlan-id>
         <id>101</id>
         <l3-interface>vlan-101</l3-interface>
      </vlan-id>
      <vlan-id>
         <id>104</id>
         <l3-interface>vlan-104</l3-interface>
      </vlan-id>
      <vlan-id>
         <id>105</id>
         <l3-interface>vlan-105</l3-interface>
      </vlan-id>
   </vlans>
</config>
"""

eos.edit_config(target="running", config=set_snippet, default_operation="merge")


# native vlan assignment to the gigabit interfaces

set_snippet = """
<config>
    <interface xmlns="http://pica8.com/xorplus/interface">
        <gigabit-ethernet>
            <name>ge-1/1/5</name>
            <family>
                <ethernet-switching>
                    <native-vlan-id>101</native-vlan-id>
                </ethernet-switching>
            </family>
        </gigabit-ethernet>
        <gigabit-ethernet>
            <name>ge-1/1/6</name>
            <family>
                <ethernet-switching>
                    <native-vlan-id>104</native-vlan-id>
                </ethernet-switching>
            </family>
        </gigabit-ethernet>
        <gigabit-ethernet>
            <name>ge-1/1/7</name>
            <family>
                <ethernet-switching>
                    <native-vlan-id>105</native-vlan-id>
                </ethernet-switching>
            </family>
        </gigabit-ethernet>
    </interface>
</config>
"""

eos.edit_config(target="running", config=set_snippet, default_operation="merge")

# IP assignment to the vlan-interfaces
set_snippet = """
<config>
    <vlan-interface xmlns="http://pica8.com/xorplus/vlan-interface">
        <interface>
            <name>vlan-101</name>
            <vif>
                <name>vlan-101</name>
                <address>
                    <name>10.10.0.13</name>
                    <prefix-length>30</prefix-length>
                </address>
            </vif>
        </interface>
        <interface>
            <name>vlan-104</name>
            <vif>
                <name>vlan-104</name>
                <address>
                    <name>10.10.0.17</name>
                    <prefix-length>30</prefix-length>
                </address>
            </vif>
        </interface>
        <interface>
            <name>vlan-105</name>
            <vif>
                <name>vlan-105</name>
                <address>
                    <name>10.10.0.21</name>
                    <prefix-length>30</prefix-length>
                </address>
            </vif>
        </interface>
    </vlan-interface>
</config>
"""

eos.edit_config(target="running", config=set_snippet, default_operation="merge")