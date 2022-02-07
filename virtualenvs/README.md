# DEPRECATED
this role has now moved to https://github.com/redhat-cop/ee_utilities/tree/main/roles.

# virtualenv migration

Running the playbook
```
ansible-playbook custom_reqs.yml -i inventory
```

## What this folder holds
This repo currently holds a role called virtualenv_migrate, that can go to your 1.2 AAP/tower instance and look at all the custom virtualenvs present on that machine, then compare the list of those requirements with the list in Default EE, then builds up a list of requirements that are extra in the custom virtualenvs.

This might be helpful for someone trying to migrate to EEs from virtualenvs when they have more than 3-5 virtualenvs they want to gather requirements from.


## Sample output
As a test I created two custom virtualenvironments in my cluster, one has netapp requirement(solidfire-sdk-python) and another one has zabbix(zabbix-api), both of which are not in Default EE, the output of the comparison looks like below

```
TASK [Show the packages that are extra from default EEs in custom venvs combined.] ***********************************************************************************************************************************************************
ok: [3.228.23.40 -> localhost] => {
    "msg": [
        "charset-normalizer",
        "enum34",
        "future",
        "solidfire-sdk-python",
        "zabbix-api"
    ]
}
```
