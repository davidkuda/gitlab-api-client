from typing import List


def transform_vars_data_structure(vars: List[dict]):
    """Transforms the data structure of the dict.
    
    Transforms this:
        [{
            'environment_scope': '*',
            'key': 'DATA',
            'masked': False,
            'protected': True,
            'value': 'Dave',
            'variable_type': 'env_var'},
            {'environment_scope': '*',
            'key': 'DATER',
            'masked': False,
            'protected': True,
            'value': 'Daver',
            'variable_type': 'env_var'},
            {'environment_scope': '*',
            'key': 'DATERR',
            'masked': False,
            'protected': True,
            'value': 'Daverr',
            'variable_type': 'env_var'
        }]
    
    To this data structure:
        {
            'DATA': 'Dave',
            'DATER': 'Daver',
            'DATERR': 'Daverr'
        }

    """
    transformed_vars = {}
    for var in vars:
        key = var['key']
        value = var['value']
        transformed_vars.update({key: value})
    return transformed_vars
