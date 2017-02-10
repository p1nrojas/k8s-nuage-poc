#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    from vspk import v4_0 as vspk

    arg_spec = dict(
        key=dict(required=True),
        user=dict(required=True),
        passwd=dict(required=True),
        org=dict(required=True),
        vsd_ip=dict(required=True),
    )
    
    module = AnsibleModule(argument_spec=arg_spec, supports_check_mode=True)
    license_key = module.params['key']
    csp_user = module.params['user']
    csp_passwd = module.params['passwd']
    csp_org = module.params['org']
    vsd_url = "https://%s:8443" % module.params['vsd_ip']

    MONIT = module.get_bin_path('monit', True)

    def start_csproot_session():
        session = vspk.NUVSDSession(
           username=csp_user,
           password=csp_passwd,
           enterprise=csp_org,
           api_url=vsd_url)
        try:
           session.start()
        except:
           logging.error('Failed to start the session')
        return session.user

    csp_session = start_csproot_session()
    license = vspk.NULicense(license=license_key)

    try:
       csp_session.create_child(license)
       module.exit_json(changed=True, name=u"license installed" % e, state='success')

    except Exception as e:
       module.exit_json(changed=False, name=u"Exception is:\n %s \n" % e, state='exception')

main()
