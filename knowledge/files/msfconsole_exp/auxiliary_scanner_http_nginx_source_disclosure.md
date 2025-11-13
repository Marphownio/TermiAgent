**The description of current metasploit exploit**
This module exploits a source code disclosure/download vulnerability in        versions 0.7 and 0.8 of the nginx web server. Versions 0.7.66 and 0.8.40        correct this vulnerability.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/nginx_source_disclosure
```

Then set the required options:

```bash
# Required parameters with no default value
set PATH_SAVE <your path to save the downloaded source code here>
set RHOSTS <your target host(s) here>
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