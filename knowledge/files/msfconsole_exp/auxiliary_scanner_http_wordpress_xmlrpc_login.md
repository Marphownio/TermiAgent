**The description of current metasploit exploit**
This module attempts to authenticate against a Wordpress-site          (via XMLRPC) using username and password combinations indicated          by the USER_FILE, PASS_FILE, and USERPASS_FILE options.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wordpress_xmlrpc_login
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html here>
```

Carefully review the following network-related parameters. These have default values but may need to be changed depending on your environment:

* RPORT – default: 80 - The target port (TCP)

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.