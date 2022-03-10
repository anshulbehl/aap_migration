#!/usr/bin/python

class FilterModule(object):
    def filters(self):
        return {
            'aap1toaap2': self.aap1toaap2
        }
    def aap1toaap2(self, dict_obj):
        """
        Filter plugin to add ansible-2.9 EE to exported objects from AAP 1.2
        """
        k,v=list(dict_obj.keys())[0], dict_obj[list(dict_obj.keys())[0]]
        a_dict = {k:[]}
        obj = []
        for item in v:
            obj_dict={}
            for v_key, v_value in item.items():
                if (v_key == 'custom_virtualenv'):
                    if k == 'projects':
                        obj_dict['default_environment'] = {'name':'Ansible Engine 2.9 execution environment',
                                'type': 'execution_environment'}
                    else:
                        obj_dict['execution_environment'] = {'name':'Ansible Engine 2.9 execution environment',
                                 'type': 'execution_environment'}
                else:
                    obj_dict[v_key] = v_value
            obj.append(obj_dict)
        a_dict[k] = obj
        return a_dict

