# Creating an Ansible Collection: A Comprehensive Guide

This blog post provides a detailed, step-by-step guide to creating Ansible collections. We'll delve into the essential aspects, including naming conventions, repository setup, collection structure initialization, custom module and module utility development, and rigorous testing within a playbook environment. By the end of this guide, you'll have a solid foundation for building and distributing your own Ansible collections.

## Understanding Ansible Collections

Ansible Collections are a distribution format for Ansible content. They allow you to package and share playbooks, roles, modules, and other plugins in a structured and reusable way. This promotes modularity, code reuse, and easier management of your automation code.

## Naming Your Collection - A Crucial First Step

The naming convention for Ansible collections is critical for proper identification and organization within the Ansible Galaxy ecosystem. Adhering to these rules ensures your collection is easily discoverable and avoids naming conflicts.

- **Format:** Collection names follow the pattern `namespace.collection_name`.
- **Namespace:** The namespace typically represents your organization, username, or a group identifier.
- **Collection Name:** The collection name should be descriptive of the functionality it provides.
- **Character Restrictions:** Both namespace and collection name **must** be valid Python identifiers. This means they can only contain ASCII letters (a-z, A-Z), digits (0-9), and underscores (_). They **cannot** start with a digit.

For this guide, we'll create a collection named:

```
ahmedzbyr.my_gem_apis
```

- **Namespace:** `ahmedzbyr`
- **Collection Name:** `my_gem_apis`

## Before You Begin: Setting Up a GitHub Repository

Before initializing your collection structure, creating a dedicated repository on GitHub (or a similar Git hosting service) is highly recommended. This repository will serve as the central location for your collection's code, allowing for version control, collaboration, and easy distribution.

We'll name our repository the same as our collection: `ahmedzbyr.my_gem_apis`.  This consistency simplifies management and improves clarity.

The repository URL will be:

```
https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis.git
```

**Important:** Ensure the repository is initialized (even if it's empty) before proceeding to the next step.

## Creating the Collection Structure: The `ansible-galaxy collection init` Command

The `ansible-galaxy` command-line tool is your primary interface for managing Ansible collections. To create the basic directory structure for your collection, use the `collection init` subcommand:

```bash
ansible-galaxy collection init ahmedzbyr.my_gem_apis
```

This command will generate the following directory structure:

```
┌─(.venv)[ahmedzbyr][ahmedzbyr-VirtualBox][~/projects/ansible_collections]
└─▪ tree
.
|____ahmedzbyr
| |____my_gem_apis
| | |____meta
| | | |____runtime.yml
| | |____roles
| | |____docs
| | |____plugins
| | | |____README.md
| | |____galaxy.yml
| | |____README.md
```

Let's break down each directory and file:

*   **`meta/runtime.yml`**: This file contains metadata about the collection's runtime environment, such as supported Ansible versions and Python requirements.
*   **`roles/`**: This directory is where you'll store any Ansible roles included in your collection. Roles are reusable units of automation code that perform specific tasks.
*   **`docs/`**:  This directory should contain documentation for your collection.  This is critical for usability. Consider using a tool like Sphinx for generating comprehensive documentation.
*   **`plugins/`**:  This is the core directory for custom Ansible plugins. It's where you'll place modules, module utilities, lookup plugins, and other custom code.
*   **`galaxy.yml`**: This is the most important file in your collection. It contains metadata about the collection itself, including its name, version, author, license, and dependencies.  We'll cover this in detail below.
*   **`README.md`**: A basic README file describing the purpose and usage of the collection.  Expand upon this significantly to provide users with helpful information.

### Updating `galaxy.yml`: Essential Collection Metadata

The `galaxy.yml` file is crucial for defining your collection's identity and dependencies. You'll need to edit this file to provide accurate and informative metadata.

Here's an example of a `galaxy.yml` file (also available at [https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/galaxy.yml](https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/galaxy.yml)):

```yaml
---
namespace: ahmedzbyr
name: my_gem_apis
version: 1.0.0
readme: README.md
authors:
  - Ahmed Zbyr <ahmed.zbyr@example.com>  # Replace with your actual email
description: Ansible collection for interacting with Gemini APIs.  # Provide a clear and concise description
license: MIT  # Choose an appropriate license
license_file: ''
dependencies: {}  # Add any collection dependencies here
galaxy_tags:
  - automation
  - api
  - gemini
  - google
  - generativeai  # Add relevant tags for discoverability
platforms:
  - name: Any
    versions:
      - All
```

**Key Fields:**

*   **`namespace`**:  Your collection's namespace (e.g., `ahmedzbyr`).
*   **`name`**: The name of your collection (e.g., `my_gem_apis`).
*   **`version`**:  The initial version of your collection (following semantic versioning).
*   **`readme`**:  The path to your README file.
*   **`authors`**:  A list of authors and their contact information.
*   **`description`**: A short description of the collection's purpose.  Make this descriptive!
*   **`license`**:  The license under which the collection is distributed (e.g., MIT, Apache-2.0, GPL-3.0).
*   **`dependencies`**:  A dictionary of collection dependencies.  If your collection requires other collections, specify them here.
*   **`galaxy_tags`**:  Keywords that help users find your collection on Ansible Galaxy.
*   **`platforms`**:  Specifies the platforms that the collection is compatible with.

### Moving Files to the Repository and Initial Commit

After updating the `galaxy.yml` file, it's time to move all the files into your Git repository and make your initial commit.

Navigate to the collection directory:

```bash
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ pwd
/home/ahmedzbyr/projects/ansible_collections/ahmedzbyr/my_gem_apis
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ ls -l
total 24
drwxrwxr-x 2 ahmedzbyr ahmedzbyr 4096 Oct  5 09:10 docs
-rw-rw-r-- 1 ahmedzbyr ahmedzbyr 3103 Oct  5 09:10 galaxy.yml
drwxrwxr-x 2 ahmedzbyr ahmedzbyr 4096 Oct  5 09:10 meta
drwxrwxr-x 2 ahmedzbyr ahmedzbyr 4096 Oct  5 09:10 plugins
-rw-rw-r-- 1 ahmedzbyr ahmedzbyr   80 Oct  5 09:10 README.md
drwxrwxr-x 2 ahmedzbyr ahmedzbyr 4096 Oct  5 09:10 roles
```

Then, execute the following Git commands:

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis.git
git push -u origin main
```

**Explanation:**

*   **`git init`**: Initializes a new Git repository in the current directory.
*   **`git add .`**: Stages all files in the current directory for commit.
*   **`git commit -m "first commit"`**: Creates a new commit with the message "first commit."
*   **`git branch -M main`**: Renames the default branch from `master` to `main`.  This is a common practice for new repositories.
*   **`git remote add origin https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis.git`**:  Adds a remote repository named `origin` pointing to your GitHub repository URL.
*   **`git push -u origin main`**: Pushes the local `main` branch to the `origin` remote and sets up tracking, so future pushes can be done with just `git push`.

Example Output:

```bash
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][±][master ?:4 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/ahmedzbyr/projects/ansible_collections/ahmedzbyr/my_gem_apis/.git/
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][±][master S:4 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ git add .
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][±][master ✓][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ git commit -m "first commit"
[master (root-commit) 463e2de] first commit
 4 files changed, 157 insertions(+)
 create mode 100644 README.md
 create mode 100644 galaxy.yml
 create mode 100644 meta/runtime.yml
 create mode 100644 plugins/README.md
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][±][main ✓][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ git branch -M main
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][±][main ✓][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ git remote add origin https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis.git
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][±][main ✓][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ git push -u origin main
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (8/8), 2.80 KiB | 1.40 MiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

Your repository is now set up and ready to receive your collection's code!

## Developing API Integrations: The `plugins` Directory

The `plugins` directory is the heart of your Ansible collection, where you'll implement custom functionality through various plugin types.

*   This directory can be used to ship various plugins inside an Ansible collection.
*   Each plugin is placed in a folder that is named after the type of `plugin` it is.
*   It can also include the `module_utils` and `modules` directory that would contain module utils and modules, respectively.

Here is an example directory structure of the majority of plugins currently supported by Ansible:

```
└── plugins
    ├── action
    ├── become
    ├── cache
    ├── callback
    ├── cliconf
    ├── connection
    ├── filter
    ├── httpapi
    ├── inventory
    ├── lookup
    ├── module_utils
    ├── modules
    ├── netconf
    ├── shell
    ├── strategy
    ├── terminal
    ├── test
    └── vars
```

### The `module_utils` Directory: Reusable Code for Your Modules

The `module_utils` directory is specifically designed for storing reusable code that can be shared across multiple Ansible modules within your collection. This promotes code reuse, reduces redundancy, and improves maintainability.

For our Gemini API integration, we'll create a file named `plugins/module_utils/gem/gemini_api.py` to house the API interaction logic.

Example: [https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/plugins/module_utils/gem/gemini_api.py](https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/plugins/module_utils/gem/gemini_api.py)

```python
# plugins/module_utils/gem/gemini_api.py
import google.generativeai as genai
import os

class GeminiAPI:
    def __init__(self, api_key):
        """Initializes the Gemini API client."""
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            print("✅ GeminiAPI client initialized successfully.")
        except Exception as e:
            raise Exception(f"❌ Error initializing Gemini API client: {e}")

    def query(self, prompt):
        """Sends a prompt to the Gemini API and returns the response."""
        try:
            print(f"💬 Sending prompt to Gemini: '{prompt[:50]}...'") # Truncate for logging
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"❌ Error querying Gemini API: {e}")

if __name__ == '__main__':
    # Example Usage (for testing)
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Please set the GEMINI_API_KEY environment variable.")
        exit(1)

    try:
        gemini = GeminiAPI(api_key)
        prompt = "Explain what an Ansible 'module_utils' is in a single sentence."
        print("\n==================================================")
        print("Prompt Sent:")
        print(prompt)
        print("\nGemini's Response:")
        response = gemini.query(prompt)
        print(response)
        print("==================================================\n")

    except Exception as e:
        print(f"An error occurred: {e}")
```

This code defines a `GeminiAPI` class that handles the communication with the Gemini API.  It includes:

*   **Initialization:**  The `__init__` method initializes the Gemini API client using the provided API key.
*   **Querying:** The `query` method sends a prompt to the Gemini API and returns the response.
*   **Error Handling:** Includes `try...except` blocks for robust error handling.
*   **Example Usage (if \_\_name\_\_ == '\_\_main\_\_' ):**  This allows you to test the code directly from the command line.

**Important:**

*   Replace `"YOUR_API_KEY"` with your actual Gemini API key.
*   Ensure you have the `google-generativeai` library installed.

### Creating a `requirements.txt` File

To ensure that all necessary Python packages are installed when your collection is used, create a `requirements.txt` file in the root of your collection. This file lists the required packages and their versions.

```
google-generativeai
```

This tells Ansible to install the `google-generativeai` library when the collection is installed.

### Testing the `module_utils` Code

Before integrating the `module_utils` code into an Ansible module, it's essential to test it independently.  This helps identify any issues early on.

1.  **Create a Virtual Environment:** Create a virtual environment to isolate the project dependencies.

    ```bash
    python3 -m venv .venv
    ```

2.  **Activate the Virtual Environment:** Activate the virtual environment.

    ```bash
    source .venv/bin/activate
    ```

3.  **Install Dependencies:** Install the packages listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set the API Key:** Set the `GEMINI_API_KEY` environment variable.

    ```bash
    export GEMINI_API_KEY="MY_API_KEY"  # Replace with your actual API key
    ```

5.  **Run the Script:** Execute the Python script directly.

    ```bash
    python plugins/module_utils/gem/gemini_api.py
    ```

Expected Output:

```bash
┌─(.venv)[ahmedzbyr][ahmedzbyr-VirtualBox][±][main U:1 ?:3 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ python plugins/module_utils/gem/gemini_api.py
✅ GeminiAPI client initialized successfully.
💬 Sending prompt to Gemini: 'Explain what an Ansible 'module...'
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1759653660.878214   14244 alts_credentials.cc:93] ALTS creds ignored. Not running on GCP and untrusted ALTS is not enabled.

==================================================
Prompt Sent:
Explain what an Ansible 'module_utils' is in a single sentence.

Gemini's Response:
Ansible's `module_utils` are reusable code snippets that can be shared and imported by multiple modules to avoid code duplication and promote consistency.

==================================================
```

## Creating an Ansible Module: The `modules` Directory

The `modules` directory is where you'll create custom Ansible modules that leverage the code in your `module_utils` directory to perform specific automation tasks.

For our Gemini API integration, we'll create a module named `plugins/modules/query_gemini.py`. This module will take a prompt as input and use the `GeminiAPI` class from `module_utils` to query the Gemini API.

Example: [https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/plugins/modules/query_gemini.py](https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/plugins/modules/query_gemini.py)

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ahmedzbyr.my_gem_apis.plugins.module_utils.gem.gemini_api import GeminiAPI  # Import from module_utils

def run_module():
    module_args = dict(
        google_api_key=dict(type='str', required=True, no_log=True),
        prompt=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        response='',
        original_prompt=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    api_key = module.params['google_api_key']
    prompt = module.params['prompt']

    result['original_prompt'] = prompt  # Store the original prompt

    try:
        gemini = GeminiAPI(api_key)
        response = gemini.query(prompt)
        result['response'] = response
        result['changed'] = True  # Indicate that the module has made a change (even if it's just querying)

    except Exception as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
```

**Explanation:**

*   **Imports:**  Imports necessary modules, including `AnsibleModule` and the `GeminiAPI` class from `module_utils`.  Note the specific import path:  `ansible_collections.ahmedzbyr.my_gem_apis.plugins.module_utils.gem.gemini_api`.
*   **`module_args`**: Defines the arguments that the module accepts:
    *   `google_api_key`: The Gemini API key (required, type string, do not log).
    *   `prompt`: The prompt to send to the Gemini API (required, type string).
*   **`AnsibleModule`**:  Creates an `AnsibleModule` object, which handles argument parsing, result formatting, and error handling.
*   **API Interaction:**
    *   Retrieves the API key and prompt from the module parameters.
    *   Initializes the `GeminiAPI` class.
    *   Calls the `query` method to send the prompt to the Gemini API.
    *   Stores the response in the `result` dictionary.
*   **Error Handling:** Uses a `try...except` block to catch any exceptions and fail the module if an error occurs.
*   **Result Reporting:**  Exits the module using `module.exit_json`, returning the `result` dictionary to Ansible.
*   **`changed` flag**: Sets the `changed` flag to `True` to indicate that the module has performed an action (even if it's just querying the API).

## Testing the Collection: Creating a Playbook

To test your newly created collection, you'll need to write an Ansible playbook that uses the custom module.

### Installing the Collection

Before running the playbook, you need to make the collection available to Ansible. There are two primary ways to do this:

1.  **Using `ansible-galaxy collection install`:** This method installs the collection from a Git repository or Ansible Galaxy.

    Create a `requirements.yml` file:

    ```yaml
    collections:
      - name: ahmedzbyr.my_gem_apis
        version: main
        type: git
        source: https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis.git
    ```

    Then, run the following command:

    ```bash
    ansible-galaxy collection install -r requirements.yml
    ```

    Output:

    ```bash
    ┌─(.venv)[ahmedzbyr][ahmedzbyr-VirtualBox][±][main ?:1 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
    └─▪ ansible-galaxy collection  install -r requirements.yml
    Starting galaxy collection install process
    Process install dependency map
    Cloning into '/home/ahmedzbyr/.ansible/tmp/ansible-local-19722b4a8l9m9/tmpmyt0udan/ahmedzbyr.my_gem_apisehy4gqzw'...
    remote: Enumerating objects: 25, done.
    remote: Counting objects: 100% (25/25), done.
    remote: Compressing objects: 100% (14/14), done.
    remote: Total 25 (delta 5), reused 24 (delta 4), pack-reused 0 (from 0)
    Receiving objects: 100% (25/25), 5.76 KiB | 5.76 MiB/s, done.
    Resolving deltas: 100% (5/5), done.
    Already on 'main'
    Your branch is up to date with 'origin/main'.
    Starting collection install process
    Installing 'ahmedzbyr.my_gem_apis:1.0.0' to '/home/ahmedzbyr/.ansible/collections/ansible_collections/ahmedzbyr/my_gem_apis'
    Created collection for ahmedzbyr.my_gem_apis:1.0.0 at /home/ahmedzbyr/.ansible/collections/ansible_collections/ahmedzbyr/my_gem_apis
    ahmedzbyr.my_gem_apis:1.0.0 was installed successfully
    ```

2.  **Using a Symbolic Link (for development):** This method creates a symbolic link from the Ansible collections directory to your development directory. This allows you to make changes to the code and test them directly without having to reinstall the collection.

    *   Remove the existing collection directory (if it exists):

        ```bash
        cd /home/ahmedzbyr/.ansible/collections/ansible_collections/ahmedzbyr; rm -rf my_gem_apis;
        ```

    *   Create the symbolic link:

        ```bash
        ln -s ~/projects/ansible_collections/ahmedzbyr/my_gem_apis my_gem_apis
        ```

### Prerequisites for Running the Playbook

Before executing the playbook, ensure that the following prerequisites are met:

1.  **Collection Installed**: Your collection `ahmedzbyr.my_gem_apis` must be installed in a location where Ansible can find it (e.g., `ansible-galaxy collection install -r requirement.yml`).
2.  **Python Library**: The `google-generativeai` library must be installed in the Python environment that your Ansible controller is using.

    ```bash
    pip install google-generativeai
    ```
3.  **API Key**: You need your Google Gemini API key. We will handle this securely using Ansible Vault.

#### Setting up the virtual environment for testing

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install ansible
pip install google-generativeai
```

Testing the setup:

```bash
┌─(.venv)[ahmedzbyr][ahmedzbyr-VirtualBox][±][main U:1 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ which ansible
/home/ahmedzbyr/projects/ansible_collections/ahmedzbyr/my_gem_apis/.venv/bin/ansible
```

We are now ready to move on.

### 1. Securely Store Your API Key

First, never hardcode secrets in your playbook. We'll use **Ansible Vault** to encrypt the API key.

1.  Create an encrypted YAML file to store your secret:

    ```bash
    ansible-vault create _secrets.yml
    ```

2.  You will be prompted to create a password for the vault. After setting it, the file will open in your default editor. Add your API key like this:

    ```yaml
    # secrets.yml
    GEMINI_API_KEY: 'YOUR_REAL_API_KEY_HERE'
    ```

3.  Save and close the file. It is now encrypted.

### 2. The Ansible Playbook

Let's assume your custom module is named `query_gemini.py`. The playbook below will use the fully qualified collection name (FQCN) `ahmedzbyr.my_gem_apis.query_gemini` to call it.

Save this code as `playbook_ask_gemini.yml`:

```yaml
---
- name: Query the Gemini API using a custom module
  hosts: localhost
  connection: local
  gather_facts: false

  # Load the encrypted API key from the vault file
  vars_files:
    - secrets.yml

  tasks:
    - name: "Call the Gemini module from the 'ahmedzbyr.my_gem_apis' collection"
      # Using the Fully Qualified Collection Name (FQCN)
      ahmedzbyr.my_gem_apis.query_gemini:
        # Pass the API key securely from the loaded vault variable
        google_api_key: "{{ GEMINI_API_KEY }}"
        prompt: "In the style of a pirate, explain what CI/CD is in two sentences."

      # Register the output of the module into a variable
      register: gemini_result

    - name: "Display the response from Gemini"
      debug:
        msg: |
          Prompt Sent: "{{ gemini_result.original_prompt }}"

          Gemini's Answer:
          "{{ gemini_result.response }}"
```

**Key Points:**

*   **`hosts: localhost`**:  Specifies that the playbook will run on the local machine.
*   **`connection: local`**:  Uses the local connection plugin.
*   **`gather_facts: false`**: Disables fact gathering for faster execution.
*   **`vars_files`**:  Loads variables from the `secrets.yml` file, which contains the encrypted API key.
*   **`ahmedzbyr.my_gem_apis.query_gemini`**:  This is the Fully Qualified Collection Name (FQCN) of your custom module. It tells Ansible where to find the module within the collection.
*   **`google_api_key: "{{ GEMINI_API_KEY }}"`**:  Passes the API key from the `secrets.yml` file to the module.
*   **`register: gemini_result`**:  Registers the output of the module in a variable named `gemini_result`.
*   **`debug: msg: ...`**:  Displays the prompt and the response from the Gemini API.

### 3. Directory Structure

For this to work, your project directory should look something like this:

```
/your_project_folder/
├── requirement.yml           # Requirement File we create above
├── playbook_ask_gemini.yml   # The playbook we just created
└── secrets.yml               # The encrypted vault file
```

*(This assumes the `ahmedzbyr.my_gem_apis` collection is installed globally or in a known `collections` path.)*

### 4. How to Run the Playbook

Execute the playbook from your terminal. You will be prompted for the vault password you created earlier.

```bash
ansible-playbook --ask-vault-pass _test_playbook_ask_gemini.yml
```

### Expected Output

If everything is configured correctly, the output will look similar to this:

```
┌─(.venv)[ahmedzbyr][ahmedzbyr-VirtualBox][±][main U:1 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ ansible-playbook --ask-vault-pass _test_playbook_ask_gemini.yml
Vault password:
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Query the Gemini API using a custom module] *****************************************************************************************************************************************************************************************************************************************************************************

TASK [Call the Gemini module from the 'ahmedzbyr.my_gem_apis' collection] *****************************************************************************************************************************************************************************************************************************************************
ok: [localhost]

TASK [Display the response from Gemini] ***************************************************************************************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "Prompt Sent: \"In the style of a pirate, explain what CI/CD is in two sentences.\"\n\nGemini's Answer:\n\"Ahoy, matey! CI/CD be like buildin' a ship, see? Continuous Integration be testin' each plank as ye nail it on, and Continuous Delivery be launchin' that vessel as soon as she's seaworthy, instead o' waitin' for the whole fleet!\n\"\n"
}

PLAY RECAP ********************************************************************************************************************************************************************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

This indicates that the playbook ran successfully, and the response from the Gemini API was displayed.

## Conclusion

Congratulations! You've successfully created an Ansible collection, integrated it with the Gemini API, and tested it with a playbook. This is the end of the collection creation. Now we can keep adding API integrations to the `module_utils` directory and use them as required. Remember to document your collection thoroughly and share it with the community on Ansible Galaxy!