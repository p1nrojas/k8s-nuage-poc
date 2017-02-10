#!/usr/bin/python

from vspk import v4_0 as vspk
#from ansible.module_utils.basic import *

def setup_logging():
    import logging
    from vspk.utils import set_log_level
    set_log_level(logging.DEBUG, logging.StreamHandler())

def start_csproot_session():
    session = vspk.NUVSDSession(
        username='csproot',
        password='csproot',
        enterprise='csp',
        api_url="https://10.10.10.10:8443")
    try:
        session.start()
    except:
        logging.error('Failed to start the session')
    return session.user

fields = {
    "key": {"required": True, "type": "str"},
    "user": {"required": True, "type": "str" },
    "passwd": {"required": True, "type": "str" },
    "org": {"required": True, "type": "str" },
    "vsd_ip": {"required": False, "type": "str"},
    },

try:
   csp_session = start_csproot_session()
   installed_licenses = csp_session.licenses.get()

except Exception as e:
   msg = "Exception is:\n %s \n" % e
   print msg
#module = AnsibleModule(argument_spec=fields)
#module.exit_json(changed=False, meta=module.params)

