# Ansible Collection for AAP2 Migration support

The Ansible Collection for AAP2 Migration support includes roles and plugins to support migration from AAP1 to AAP2

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

For collections that support Ansible 2.9, please ensure you update your `network_os` to use the
fully qualified collection name (for example, `cisco.ios.ios`). 
Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

## Python version compatibility

This collection requires Python 2.7 or greater.

## Included content

<!--start collection content-->
### Filter plugins
Name | Description
--- | ---
[ansible_refarch.aap2_migrate.aap1toaap2]()|Filter plugin to convert AAP1.2 objects to AAP2 compatible ones

### Roles
Name | Description
--- | ---
[ansible_refarch.aap2_migrate.migrate]()| Role to help in migration using git as source control from AAP1.2 to AAP2


<!--end collection content-->

## Installing this collection

You can install the aap2_migrate collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install ansible_refarch.aap2_migrate

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: ansible_refarch.aap2_migrate
```

## Using this collection

You can either call plugins by their Fully Qualified Collection Namespace (FQCN), such as `ansible_refarch.aap2_migrate.aap1toaap2`, or you can call roles by their short name if you list the `ansible_refarch.aap2_migrate` collection in the playbook's `collections` keyword:



### See Also:

* [Migration Reference Architecture]()


## More information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
