**The description of current metasploit exploit**
This module checks the provided hosts for the CVE-2023-21554 vulnerability by sending          a MSMQ message with an altered DataLength field within the SRMPEnvelopeHeader that          overflows the given buffer. On patched systems, the error is caught and no response          is sent back. On vulnerable systems, the integer wraps around and depending on the length          could cause an out-of-bounds write. In the context of this module a response is sent back,          which indicates that the system is vulnerable.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/msmq/cve_2023_21554_queuejumper
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 1801 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.