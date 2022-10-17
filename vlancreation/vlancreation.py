from ncclient import manager

eos = manager.connect(
    host="172.31.32.102",
    port="830",
    timeout=30,
    username="admin",
    password="password",
    hostkey_verify=False,
)
vlan = """
<vlans xmlns="http://pica8.com/xorplus/vlans">
   <vlan-id>
      <id>136</id>
      <description/>
      <vlan-name>default</vlan-name>
      <l3-interface>vlan136</l3-interface>
   </vlan-id>
</vlans>
"""

reply = eos.edit_config(target="running", config=vlan, default_operation="merge")
