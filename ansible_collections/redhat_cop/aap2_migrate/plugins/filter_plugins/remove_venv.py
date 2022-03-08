#!/usr/bin/python

class FilterModule(object):

    def filters(self):
        return {
            'aap1toaap2': self.aap1toaap2
        }

    def aap1toaap2(self, dict_obj):
        k,v=list(dict_obj.keys())[0], dict_obj[list(dict_obj.keys())[0]]
        a_dict = {k:[]}
        print(a_dict)
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

