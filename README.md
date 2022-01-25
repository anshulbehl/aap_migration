# aap_migration

Running the playbook
```
ansible-playbook -i inventory -e @sample_vars.yml
```

## What this repo holds
This repo currently holds a playbook called custom_reqs.yml, that can go to your 1.2 AAP/tower instance and look at all the custom virtualenvs present on that machine, then compare the list of those requirements with the list in Default EE, then builds up a list of requirements that are extra in the custom virtualenvs.

This might be helpful for someone trying to migrate to EEs from virtualenvs when they have more than 3-5 virtualenvs they want to gather requirements from.


