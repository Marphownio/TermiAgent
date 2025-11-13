**The description of current metasploit exploit**
This module will test a range of Brocade network devices for a        privileged logins and report successes. The device authentication mode        must be set as 'aaa authentication enable default local'.        Telnet authentication, e.g. 'enable telnet authentication', should not        be enabled in the device configuration.        This module has been tested against the following devices:              ICX6450-24 SWver 07.4.00bT311,              FastIron WS 624 SWver 07.2.02fT7e1

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/telnet/brocade_enable_login
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 23 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.