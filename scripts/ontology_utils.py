import requests
import json
import os

# local file with token

def _load_token(environment):
    with open(os.path.dirname(__file__) + f'/../{str(environment).upper()}_TOKEN') as f:
        t = f.read()
    return t.strip()


def _get_ontology_api(sw_url):
    payload = {
        "method": "ServiceWizard.get_service_status",
        "id": '',
        "params": [{"module_name":"OntologyAPI", "version":"dev"}],  # TODO: change to beta/release
        "version": "1.1"
    }
    sw_resp  = requests.post(url=sw_url, data=json.dumps(payload))
    wiz_resp = sw_resp.json()
    if wiz_resp.get('error'):
        raise RuntimeError(f"ServiceWizard Error - {wiz_resp['error']}")
    return wiz_resp['result'][0]['url']


def _get_ontology_namespaces(environment):
    sw_url = f"https://{environment}.kbase.us/services/service_wizard"
    onto_url = _get_ontology_api(sw_url)
    headers = {
        "Authorization": _load_token(environment),
        "Content-Type": "application/json"
    }
    payload = {
        "method": "OntologyAPI.get_namespaces",
        "id": "",
        "params": [],
        "version": "1.1"
    }

    resp = requests.post(url=onto_url, data=json.dumps(payload), headers=headers)
    if not resp.ok:
        raise RuntimeError(f"text: {resp.text}")
    resp_json = resp.json()
    if resp_json.get('error'):
        try:
            resp_mess = resp_json['error']['message']
        except:
            resp_mess = resp_json['error']
        raise RuntimeError(f"{resp_mess} - with data {json.dumps(payload)}")
    return resp_json['result'][0]['namespaces']


def create_ontology_mapping(environment):
    namespaces = _get_ontology_namespaces(environment)
    mapping = {}
    for ns in namespaces:
        if ns == "default": continue
        if '@onto_terms' in namespaces[ns]:
            mapping[ns] = namespaces[ns]['@onto_terms']
        else:
            # idk doood
            pass
    return mapping
