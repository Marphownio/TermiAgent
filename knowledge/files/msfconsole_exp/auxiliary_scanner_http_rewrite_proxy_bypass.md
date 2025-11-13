**The description of current metasploit exploit**
Scan for poorly configured reverse proxy servers.        By default, this module attempts to force the server to make        a request with an invalid domain name. Then, if the bypass        is successful, the server will look it up and of course fail,        then responding with a status code 502. A baseline status code        is always established and if that baseline matches your test        status code, the injection attempt does not occur.        "set VERBOSE true" if you are paranoid and want to catch potential        false negatives. Works best against Apache and mod_rewrite

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/rewrite_proxy_bypass
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.