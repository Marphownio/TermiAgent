**The description of current metasploit exploit**
This module exploits a directory traversal vulnerability in Cisco's Adaptive Security Appliance (ASA) software and Firepower Threat Defense (FTD) software.          It lists the contents of Cisco's VPN web service which includes directories, files, and currently logged in users.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/cisco_directory_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 443 - The target port (TCP)

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.