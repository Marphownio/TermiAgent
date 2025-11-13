**The description of current metasploit exploit**
This module identifies NTP servers which permit mode 6 REQ_NONCE requests that        can be used to conduct DRDoS attacks. In some configurations, NTP servers will        respond to REQ_NONCE requests with a response larger than the request,        allowing remote attackers to cause a distributed, reflected        denial of service (aka, "DRDoS" or traffic amplification) via spoofed        requests.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ntp/ntp_req_nonce_dos
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 123 - The target port (UDP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.