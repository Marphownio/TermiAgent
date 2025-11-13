**The description of current metasploit exploit**
This module enumerates files from target domain controllers and connects to them via SMB. It then looks for Group Policy Preference XML files containing local/domain user accounts and passwords and decrypts them using Microsoft's public AES key. This module has been tested successfully on a Win2k8 R2 Domain Controller.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/smb/smb_enum_gpp
```

Then set the required options:

```bash
# Required parameters with no default value
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 445 - The Target port (TCP)

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.