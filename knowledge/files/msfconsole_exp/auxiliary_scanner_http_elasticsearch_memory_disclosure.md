**The description of current metasploit exploit**
This module exploits a memory disclosure vulnerability in Elasticsearch          7.10.0 to 7.13.3 (inclusive). A user with the ability to submit arbitrary          queries to Elasticsearch can generate an error message containing previously          used portions of a data buffer.          This buffer could contain sensitive information such as Elasticsearch          documents or authentication details. This vulnerability's output is similar          to heartbleed.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/elasticsearch_memory_disclosure
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 9200 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.