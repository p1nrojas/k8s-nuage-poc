#!/usr/bin/python

from vspk import v4_0 as vspk

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

csp_session = start_csproot_session()
installed_licenses = csp_session.licenses.get()
license = vspk.NULicense(license=u'MDEyOIw4PB0U8ewPgHjB5B/POJyA6d2fTX+IkdUYxRekfjXuOSY/vVDp6CJQdVK1ZRciMT5mP5MkMllEO7ff/ff6bjVT5y8DP0EdiYZQobdTPXY9kfAKb/jAD0eHeH/5K8jHfi9labVPCGpV9X7cTj7yVCAGxy9nqmcDX0J7+QGjYwh0MDE2MjCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAkOyl181q5j2UHPUCD5nzBE5Gz0g3N1n8KAs6aEcNO7ueXvPUeiuNQ//ui0vE9otuo4AnLJkLKuxoIJmVjIKzxXlMEqsAK5zwOJpECOTEMxjZkyWcAujQg/ajVRcUAW+91UPz2nkzs1WkPhKs5ZjJTrksoEvmMt5fhNFXgLY2jCcCAwEAATA2OTJ7InByb3ZpZGVyIjoiTnVhZ2UgTmV0d29ya3MgLSBBbGNhdGVsLUx1Y2VudCBJbmMiLCJwcm9kdWN0VmVyc2lvbiI6IjQuMCIsImxpY2Vuc2VJZCI6MSwibWFqb3JSZWxlYXNlIjoxLCJtaW5vclJlbGVhc2UiOjAsInVzZXJOYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImpsZXRlbGllckByZWR2b2lzcy5uZXQiLCJjb21wYW55IjoiUmVkVm9pc3MiLCJwaG9uZSI6Iis1NiAyIDIyNDA4NTM3Iiwic3RyZWV0IjoiQmFkYWpvejEzMCBQLjE2IExhcyBDb25kZXMiLCJjaXR5IjoiU2FudGlhZ28iLCJzdGF0ZSI6IlJNIiwiemlwIjoiMDAwMDAwIiwiY291bnRyeSI6IkNoaWxlIiwiY3VzdG9tZXJLZXkiOiJmZWZlZmVmZS1mZWZlLWZlZmUtZmVmZSIsImFsbG93ZWRWTXNDb3VudCI6LTEsImFsbG93ZWROSUNzQ291bnQiOi0xLCJhbGxvd2VkVlJTc0NvdW50IjoxMCwiYWxsb3dlZFZSU0dzQ291bnQiOjIsImFsbG93ZWRDUEVzQ291bnQiOjEwLCJpc0NsdXN0ZXJMaWNlbnNlIjpmYWxzZSwiZXhwaXJhdGlvbkRhdGUiOiI0LzQvMjAxNyAxMjowMDowMCBBTSIsImVuY3J5cHRpb25Nb2RlIjpmYWxzZSwibGljZW5zZUVudGl0aWVzIjoie1wiZGVwbG95bWVudFR5cGVcIjpcIkN1c3RvbWVyIExBQlwiLFwibGljZW5zZVJlcXVlc3RJRFwiOlwicmVxdWVzdC0yMDUyLnJlcVwifSIsImFkZGl0aW9uYWxTdXBwb3J0ZWRWZXJzaW9ucyI6IjAifQ==')

try:
#   self._log_vsd_status('initializing',
#                        'Adding a new license to VSD')

#   csp_session.create_child(license)
    print installed_licenses[0].expiration_date
    print installed_licenses[0].state
    print installed_licenses[0].allowed_vrss_count

except Exception as e:

   msg = "Exception is:\n %s \n" % e
   print msg

#   print "not working"

#   if e.connection.response.status_code == 409:
#       self._log_vsd_status('initializing',
#                            'License already installed')
#   else:
#       raise (WorkerException
#              .LabDeploymentError('Unable to add new ' +
#                                  'VSD license'))
