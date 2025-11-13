**The description of current metasploit exploit**
This module checks a range of hosts for the CVE-2019-0708 vulnerability          by binding the MS_T120 channel outside of its normal slot and sending          non-DoS packets which respond differently on patched and vulnerable hosts.          It can optionally trigger the DoS vulnerability.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/rdp/cve_2019_0708_bluekeep
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RDP_CLIENT_IP – default: 192.168.0.100 - The client IPv4 address to report during connect
* RPORT – default: 3389 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.