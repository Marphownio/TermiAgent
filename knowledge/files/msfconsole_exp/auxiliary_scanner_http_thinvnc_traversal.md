**The description of current metasploit exploit**
This module exploits a directory traversal vulnerability in ThinVNC          versions 1.0b1 and prior which allows unauthenticated users to retrieve          arbitrary files, including the ThinVNC configuration file.          This module has been tested successfully on ThinVNC versions 1.0b1          and "ThinVNC_Latest" (2018-12-07).

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/thinvnc_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8080 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.