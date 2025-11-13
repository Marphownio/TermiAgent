**The description of current metasploit exploit**
Grafana versions 8.0.0-beta1 through 8.3.0 prior to 8.0.7, 8.1.8, 8.2.7, or 8.3.1 are vulnerable to directory traversal          through the plugin URL.  A valid plugin ID is required, but many are installed by default.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/grafana_plugin_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 3000 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.