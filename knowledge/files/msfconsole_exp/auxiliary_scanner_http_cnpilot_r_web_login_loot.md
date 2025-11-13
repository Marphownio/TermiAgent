**The description of current metasploit exploit**
This module scans for Cambium cnPilot r200/r201 management login          portal(s), attempts to identify valid credentials, and dump device          configuration.          The device has at least two (2) users - admin and user. Due to an          access control vulnerability, it is possible for 'user' account to access full          device config. All information, including passwords, and keys, is stored          insecurely, in clear-text form, thus allowing unauthorized admin access to any          user.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/cnpilot_r_web_login_loot
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.