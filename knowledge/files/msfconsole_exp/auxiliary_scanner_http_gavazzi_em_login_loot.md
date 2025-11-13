**The description of current metasploit exploit**
This module scans for Carlo Gavazzi Energy Meters login portals, performs a login brute force attack, enumerates device firmware version, and attempt to extract the SMTP configuration. A valid, admin privileged user is required to extract the SMTP password. In some older firmware versions, the SMTP config can be retrieved without any authentication. The module also exploits an access control vulnerability which allows an unauthenticated user to remotely dump the database file EWplant.db. This db file contains information such as power/energy utilization data, tariffs, and revenue statistics. Vulnerable firmware versions include - VMU-C EM prior to firmware Version A11_U05 and VMU-C PV prior to firmware Version A17.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/gavazzi_em_login_loot
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.