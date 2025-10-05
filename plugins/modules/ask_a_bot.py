# In your_custom_module.py
from ansible.module_utils.basic import AnsibleModule
# The import path is relative to the collection's 'plugins' directory
from ansible_collections.ahmedzbyr.my_gem_apis.plugins.module_utils.gem.gemini_api import GeminiAPI

def run_module():
    module_args = dict(
        google_api_key=dict(type='str', required=True, no_log=True),
        prompt=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False,
        original_prompt='',
        response=''
    )

    # Get params from user
    api_key = module.params['google_api_key']
    user_prompt = module.params['prompt']
    result['original_prompt'] = user_prompt

    try:
        client = GeminiAPI(api_key=api_key)
        response_text = client.get_response(user_prompt)
        result['response'] = response_text
        module.exit_json(**result)
    except Exception as e:
        module.fail_json(msg=f'Failed to communicate with Gemini API: {e}', **result)

def main():
    run_module()

if __name__ == '__main__':
    main()