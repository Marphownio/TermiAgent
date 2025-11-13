**The description of current metasploit exploit**
This module attempts to authenticate to different D-Link HTTP management        services. It has been tested on D-Link DIR-300 Hardware revision A, D-Link DIR-615        Hardware revision D and D-Link DIR-320 devices. It is possible that this module        also works with other models.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/dlink_dir_300_615_http_login
```

Then set the required options:

```bash
# Required parameters with no default value
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