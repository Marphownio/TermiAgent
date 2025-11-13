**The description of current metasploit exploit**
Cambium devices (ePMP, PMP, Force, & others) can be administered using SNMP. The device configuration contains IP addresses, keys, and passwords, amongst other information. This module uses SNMP to extract Cambium ePMP device configuration. On certain software versions, specific device configuration values can be accessed using SNMP RO string, even though only SNMP RW string should be able to access them, according to MIB documentation. The module also triggers full configuration backup, and retrieves the backup url. The configuration file can then be downloaded without authentication. The module has been tested on Cambium ePMP versions 3.5 & prior.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/snmp/epmp1000_snmp_loot
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 161 - The target port (UDP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.