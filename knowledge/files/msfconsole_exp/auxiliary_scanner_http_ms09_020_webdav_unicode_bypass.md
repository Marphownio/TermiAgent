**The description of current metasploit exploit**
This module attempts to to bypass authentication using the WebDAV IIS6          Unicode vulnerability discovered by Kingcope. The vulnerability appears          to be exploitable where WebDAV is enabled on the IIS6 server, and any          protected folder requires either Basic, Digest or NTLM authentication.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/ms09_020_webdav_unicode_bypass
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host here>
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