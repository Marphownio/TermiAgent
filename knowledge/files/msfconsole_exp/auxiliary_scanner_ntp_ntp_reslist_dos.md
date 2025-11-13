**The description of current metasploit exploit**
This module identifies NTP servers which permit "reslist" queries and        obtains the list of restrictions placed on various network interfaces,        networks or hosts. The reslist feature allows remote        attackers to cause a distributed, reflected denial of service (aka, "DRDoS" or        traffic amplification) via spoofed requests. The more interfaces, networks        or hosts with specific restrictions, the greater the amplification.        requests.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ntp/ntp_reslist_dos
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