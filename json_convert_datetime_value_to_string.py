import json
import datetime

dd = {'correlation_id': 'vtfy4poj9omcyr3dh866ft5wz4', 'id': 2424, 'uuid': 'si79w0bgz', 'event_action': 'wp_created', 'url': '/wp/create', 'payload': "{'site_name': 'DaddyNeiell', 'site_template': 'wp', 'wp_admin_username': 'DaddyNeiell', 'wp_password': 'admin', 'wp_email': 'DaddyNeiell@email.org', 'domains': '', 'site_datacenter_location': 'azew'}", 'description': '', 'support_caseno': '', 'processed': 0, 'status': 1, 'qa': 0, 'auth_userid': '', 'auth_email': '', 'ipaddress': '10.244.2.0', 'activation_at': None, 'updated_at': datetime.datetime(2020, 3, 26, 6, 6, 30), 'created_at': datetime.datetime(2020, 3, 26, 6, 5, 27), 'executed_at': datetime.datetime(2020, 3, 26, 6, 6, 30)}

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

print(json.dumps(dd, default = myconverter))
