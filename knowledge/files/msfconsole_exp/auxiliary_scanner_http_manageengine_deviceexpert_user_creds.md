**The description of current metasploit exploit**
This module extracts usernames and salted MD5 password hashes          from ManageEngine DeviceExpert version 5.9 build 5980 and prior.          This module has been tested successfully on DeviceExpert          version 5.9.7 build 5970.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/manageengine_deviceexpert_user_creds
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 6060 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.