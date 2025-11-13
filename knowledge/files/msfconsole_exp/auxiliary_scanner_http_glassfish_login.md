**The description of current metasploit exploit**
This module attempts to login to GlassFish instance using username and password        combinations indicated by the USER_FILE, PASS_FILE, and USERPASS_FILE options.        It will also try to do an authentication bypass against older versions of GlassFish.        Note: by default, GlassFish 4.0 requires HTTPS, which means you must set the SSL option        to true, and SSLVersion to TLS1. It also needs Secure Admin to access the DAS remotely.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/glassfish_login
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 4848 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.