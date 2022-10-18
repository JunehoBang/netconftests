# Refered the follwoing git repository
# https://github.com/aristanetworks/openmgmt/blob/main/src/ncclient/EOS_commands_with_NETCONF.py

from ncclient import manager

# snippet = """
# <vlans xmlns="http://pica8.com/xorplus/vlans">
#    <vlan-id>
#       <id>136</id>
#       <vlan-name>testvlan</vlan-name>
#       <l3-interface>vlan136</l3-interface>
#    </vlan-id>
# </vlans>
# """
eos = manager.connect(host="172.31.32.102", port="830",  timeout=500, username="admin", password="password",  hostkey_verify=False, device_params={'name':'default'})

add_snippet = """
<config>
   <vlans xmlns="http://pica8.com/xorplus/vlans">
      <vlan-id>
         <id>136</id>
         <vlan-name>testvlan</vlan-name>
         <l3-interface>vlan136</l3-interface>
      </vlan-id>
   </vlans>
</config>
"""

reply = eos.edit_config(target="running", config=add_snippet, default_operation="merge")
print(reply.xml)


delete_snippet = """
<config>
   <vlans xmlns="http://pica8.com/xorplus/vlans">
      <vlan-id operation="delete">
         <id>136</id>
      </vlan-id>
   </vlans>
</config>
"""

reply = eos.edit_config(target="running", config=delete_snippet, default_operation="merge")
