**The description of current metasploit exploit**
This module will download a file of your choice against Symantec Messaging          Gateway.  This is possible by exploiting a directory traversal vulnerability          when handling the 'logFile' parameter, which will load an arbitrary file as          an attachment.  Note that authentication is required in order to successfully          download your file.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/symantec_brightmail_logfile
```

Then set the required options:

```bash
# Required parameters with no default value
set PASSWORD <your password here>
set RHOSTS <your target host(s) here>
set USERNAME <your username here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 41080 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.