**The description of current metasploit exploit**
This module logs in to SNMP devices using common community names.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/snmp/snmp_login
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 161 - The target port
* PROTOCOL – default: udp - The SNMP protocol to use

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.