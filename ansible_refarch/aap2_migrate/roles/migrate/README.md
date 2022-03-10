ansible\_refarch.aap2\_migrate.migrate
================================================

Use this role to export the objects from your running AAP1.2 cluster on to a git repository. Below features are provided by this role in order to aid in the migration from AAP 1.2 to AAP 2.1
- Exports all the objects supported by the export module in the ansible.controller collection
- Convert all the exported objects as AAP 2 objects (e.g Convert virtualenv keys to execution environment ones)
- Push the exported objects and converted objects to a git repo
- Use a git repo to do an import to the new AAP 2 cluster aiding in a side-by-side migration, by first taking backup to the same repo and then doing an import from the same repo

Sample inventory file looks like this
```
[localhost]
localhost migrate_default_user_location=~  #the default for this variable is set to /home/runner which enables this role to run inside an EE, if you are not running inside an EE please use the default location as this line suggests
```

Requirements
------------
Depends on ansible.controller certified collection available through Ansible Automation hub
```
---
collections: ansible.controller
```

Role variables
--------------
|Variable Name|Default Value|Required|Description|Example|
|:---:|:---:|:---:|:---:|:---:|
|`gh_repo`|None|yes|"GH repo to take backup and import objects from"|`https://github.com/anshulbehl/aap-migration-backups/`
|`migrate_default_user_location`|`/home/runner`|No(will fail if ran outside an EE)|Default home fir to save GH creds file in order to push backups|`~`|

Example Playbook
----------------

```yaml
# playbook to gather requirements from custom virtualenvs
---
- name: Export Objects
  hosts: localhost
  connection: local
  gather_facts: true
  collections:
    - ansible_refarch.aap2_migrate
  tasks:
  - name: Import backup role
    import_role:
      name: migrate
```
License
-------
MIT

Author Information
------------------
Anshul Behl (abehl@redhat.com)
