# Refered the follwoing git repository
# https://github.com/aristanetworks/openmgmt/blob/main/src/ncclient/EOS_commands_with_NETCONF.py

from ncclient import manager

snippet = """
<vlans xmlns="http://pica8.com/xorplus/vlans">
   <vlan-id>
      <id>136</id>
      <vlan-name>testvlan</vlan-name>
      <l3-interface>vlan136</l3-interface>
   </vlan-id>
</vlans>
"""

with manager.connect(host="172.31.32.102", port="830",  timeout=30, username="admin", password="password",  hostkey_verify=False, device_params={'name':'default'}) as m:
   reply = m.edit_config(target="running", config=snippet, default_operation="merge")
   print(reply.xml)
