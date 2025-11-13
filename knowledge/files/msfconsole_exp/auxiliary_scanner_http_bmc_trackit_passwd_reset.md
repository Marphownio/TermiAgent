**The description of current metasploit exploit**
This module exploits a flaw in the password reset mechanism in BMC TrackIt! 11.3          and possibly prior versions. If the password reset service is configured to use          a domain administrator (which is the recommended configuration), then domain          credentials can be reset (such as domain Administrator).

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/bmc_trackit_passwd_reset
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your RHOSTS here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.