import getpass

class Switch:
    def __init__(self):
      self.set_hostname()
      self.set_user_pass()
      self.set_user_privilege()
      self.set_domain_name()
      self.set_name_servers()
      self.set_vlans()
      self.set_interfaces()
      self.set_vlan_interface()
      self.set_default_gateway()
      self.set_logging_server()
      self.set_snmp_community_string()
      self.set_ntp_servers()
      self.set_crypto_key_modulus()

    def set_hostname(self):
      self.hostname = raw_input("Hostname: ")
      return

    def set_user_pass(self):
      self.user = ''
      self.user_secret = ''
      while not self.user:
        self.user = getpass.getuser()
      while not self.user_secret:
        self.user_secret = getpass.getpass("Password: ")
      return
    
    def set_user_privilege(self):
      self.user_privilege  = raw_input("User Privilege Level:  (default: 15)")
      if not self.user_privilege:
        self.user_privilege = 15
      return

    def set_domain_name(self):
      self.domain_name = raw_input("Domain Name: ")
      return

    def set_name_servers(self):
      self.name_server1 = raw_input("Name Server 1: ")
      self.name_server2 = raw_input("Name Server 2: ")

    def set_vlans(self):
      self.vlans = {}
      number_of_vlans = raw_input("How many VLANs on this device: ")
      for vlan in range(int(number_of_vlans), 0, -1):
        vlan_number = raw_input("%s - VLAN Number: " % int(vlan))
        vlan_name = raw_input("%s - VLAN Name: " % int(vlan))
        self.vlans[vlan_number] = vlan_name
      return

    def set_interfaces(self):
      self.interfaces = []
      type_of_interfaces = ""
      interface_types = ['GigabitEthernet','FastEthernet','Ethernet']
      number_of_interfaces = raw_input("How many interfaces on this device: ")
      type_of_interface = raw_input("Type of Interface [default: GigabitEthernet]: ")
      if not type_of_interface:
          type_of_interface = 'GigabitEthernet'
      for interface in range(int(number_of_interfaces), 0, -1):
        self.interfaces.append('%s0/%s' %(type_of_interface, interface))
      return

    def set_vlan_interface(self):
      ip_address = raw_input("IP Address of VLAN1: ")
      netmask = raw_input("Netmask for VLAN1: ")
      self.vlan_interface = "%s %s" %(ip_address, netmask)
      self.shut_noshut = "no shutdown"
      return

    def set_default_gateway(self):
      self.default_gateway = raw_input("Default gateway: ")
      return

    def set_logging_server(self):
      self.logging_server = raw_input("Logging Server  [If none, type None]: ")
      if not self.logging_server:
          self.logging_server = "None"

    def set_snmp_community_string(self):
      self.snmp_community_string = ''
      while not self.snmp_community_string:
        self.snmp_community_string = raw_input("SNMP Community String: ")
      return

    def set_ntp_servers(self):
      self.ntp_server1 = ''
      self.ntp_server2 = ''
      while not self.ntp_server1:
          self.ntp_server1 = raw_input("NTP Server 1: ")
      while not self.ntp_server2:
          self.ntp_server2 = raw_input("NTP Server 2: ")
      return

    def set_crypto_key_modulus(self):
      self.crypto_key_modulus = 1024
      while not self.crypto_key_modulus:
        self.crypto_key_modulus = raw_input("Crypto Key Modulus [default: 1024]: ")
        if not self.crypto_key_modulus:
            self.crypto_key_modulus = 1024
      return




    
