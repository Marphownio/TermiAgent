**The description of current metasploit exploit**
Versions of Apache Log4j2 impacted by CVE-2021-44228 which allow JNDI features used in configuration,        log messages, and parameters, do not protect against attacker controlled LDAP and other JNDI related endpoints.        This module will scan an HTTP end point for the Log4Shell vulnerability by injecting a format message that will        trigger an LDAP connection to Metasploit. This module is a generic scanner and is only capable of identifying        instances that are vulnerable via one of the pre-determined HTTP request injection points. These points include        HTTP headers and the HTTP request path.        Known impacted software includes Apache Struts 2, VMWare VCenter, Apache James, Apache Solr, Apache Druid,        Apache JSPWiki, Apache OFBiz.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/log4shell_scanner
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
set SRVHOST <your local host or network interface here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)
* SRVPORT – default: 389 - The local port to listen on

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.