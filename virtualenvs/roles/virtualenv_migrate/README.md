redhat_cop.tower_utilities.virtualenv_migrate
=========

Use this role to create a list of python requirements from custom virtualenvs present in your AAP 1.2 cluster, after comparing those with requirements in Default Execution Environment.
This role is based on the `awx-manage` utility and needs an AAP1.2 tower node to gather requirements from and localhost to pull EE and compare those requirements.
This role sets the python requirements to `ee_python` variable, which can then be used by the ee_utilities role to create a new EE.

Sample inventory file looks like this
```
[tower]
TOWER_HOST ansible_ssh_private_key=<>

[local]
localhost ansible_become_password=<>
```

Requirements
------------
podman on localhost

Role variables
----------------
|Variable Name|Default Value|Required|Description|Example|
|:---:|:---:|:---:|:---:|:---:|
|`default_ee_url`|`registry.redhat.io/ansible-automation-platform-21/ee-supported-rhel8:latest`|no|"Registry link of the EE you want to compare requirements with"|`localhost/ee:latest`
|`registry_username`|None|yes(for default EE value)|username to sign in to the registry|`admin`|
|`registry_password`|None|yes(for default EE value)|password to sign in to the registry|`pass`|

Example Playbook
----------------

```yaml
# playbook to gather requirements from custom virtualenvs
---
- name: Review custom virtualenvs and pull requirements
  hosts: "!localhost"
  become: true
  tasks:
    - name: Include venv role
      include_role: 
        name: roles/virtualenv_migrate
```
License
-------
MIT

Author Information
------------------
Anshul Behl (abehl@redhat.com)
