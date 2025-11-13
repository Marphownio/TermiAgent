**The description of current metasploit exploit**
Uses information disclosure to determine if MS17-010 has been patched or not.          Specifically, it connects to the IPC$ tree and attempts a transaction on FID 0.          If the status returned is "STATUS_INSUFF_SERVER_RESOURCES", the machine does          not have the MS17-010 patch.          If the machine is missing the MS17-010 patch, the module will check for an          existing DoublePulsar (ring 0 shellcode/malware) infection.          This module does not require valid SMB credentials in default server          configurations. It can log on as the user "\" and connect to IPC$.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/smb/smb_ms17_010
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 445 - The SMB service port (TCP)

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.