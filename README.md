# Creating an Ansible Collection

This blog post will guide you through the process of creating an Ansible collection. We'll cover naming conventions, setting up a repository, initializing the collection structure, adding custom modules and module utilities, and finally, testing the collection in a playbook.

## Naming Your Collection

- Collection names consist of a namespace and a name, separated by a period (`.`).
- Both namespace and name should be valid Python identifiers.
- This means that they should consist of ASCII letters, digits, and underscores.

We will create a collection named as follows:

```
ahmedzbyr.my_gem_apis
```

- Namespace: `ahmedzbyr`
- Name of the collection: `my_gem_apis`

# Before Creating a Collection

Before creating the collection, let's create a repository on GitHub. We will use this location as our repository, which we can then later reference in our playbook to automate.

We will name the repository the same as our collection: `ahmedzbyr.my_gem_apis`.

```
https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis.git
```

# Creating the Collection

We will use the following command to create a directory structure for our collection:

```bash
ansible-galaxy collection init ahmedzbyr.my_gem_apis
```

This will create the following directory structure:

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

Let's go over the directory structure. First, update the `galaxy.yml` file.

Example: [https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/galaxy.yml](https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/galaxy.yml)

Once this is updated, we move all the files into the repository.

Go to the location where we have these files:

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

In this location, we will push all the files to the repository:

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis.git
git push -u origin main
```

Example:

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

Now we have the repository ready to add some code to it.

## Getting Some API Ready - `plugins` Directory

We will be using the `plugins` directory to start adding API integrations.

- This directory can be used to ship various plugins inside an Ansible collection.
- Each plugin is placed in a folder that is named after the type of `plugin` it is.
- It can also include the `module_utils` and `modules` directory that would contain module utils and modules, respectively.

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

## Adding API to `module_utils` Directory

We will currently only be using the `module_utils` directory in the path `plugins/module_utils/gem/gemini_api.py`.
We will be creating an API to Gemini.

Example: [https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/plugins/module_utils/gem/gemini_api.py](https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/plugins/module_utils/gem/gemini_api.py)

This is very simple code that sends a request to the Gemini API endpoint and gets a response.

- `requirements.txt` File should have the below package.

```
google-generativeai
```

Testing this Python code now:

```bash
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][±][main U:1 ?:2 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ python3 -m venv .venv
┌─[ahmedzbyr][ahmedzbyr-VirtualBox][±][main U:1 ?:2 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ source .venv/bin/activate
┌─(.venv)[ahmedzbyr][ahmedzbyr-VirtualBox][±][main U:1 ?:3 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ pip install -r requirements.txt
```

Set the `GEMINI_API_KEY` in the environment:

```bash
export GEMINI_API_KEY="MY_API_KEY"
```

Output:

```bash
┌─(.venv)[ahmedzbyr][ahmedzbyr-VirtualBox][±][main U:1 ?:3 ✗][~/projects/ansible_collections/ahmedzbyr/my_gem_apis]
└─▪ python plugins/module_utils/gem/mygemapi.py
✅ GeminiAPI client initialized successfully.
💬 Sending prompt to Gemini: 'Explain what an Ansible 'modul...'
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1759653660.878214   14244 alts_credentials.cc:93] ALTS creds ignored. Not running on GCP and untrusted ALTS is not enabled.

==================================================
Prompt Sent:
Explain what an Ansible 'module_utils' is in a single sentence.

Gemini's Response:
Ansible's `module_utils` are reusable code snippets that can be shared and imported by multiple modules to avoid code duplication and promote consistency.

==================================================
```

## Adding module to `modules` Directory

This directory will contain the file which will be interfacing with our API above.
This take 2 parameters from the user:

```python
google_api_key=dict(type='str', required=True, no_log=True),
prompt=dict(type='str', required=True)
```

API key and the prompt.

Example: [https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/plugins/modules/query_gemini.py](https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis/blob/main/plugins/modules/query_gemini.py)

## Creating Test Playbook

Requirement.yml file:

```yaml
collections:
  - name: ahmedzbyr.my_gem_apis
    version: main
    type: git
    source: https://github.com/ahmedzbyr/ahmedzbyr.my_gem_apis.git
```

Pull the repo:

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

Optionally, we can do this for development so that we can change the code and test on the node.

- Remove the directory: `cd /home/ahmedzbyr/.ansible/collections/ansible_collections/ahmedzbyr; rm -rf my_gem_apis;`
- Then, create a symlink to your development Directory:

```bash
ln -s ~/projects/ansible_collections/ahmedzbyr/my_gem_apis my_gem_apis
```

### Prerequisites

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

This will be the end of the collection creation. Now we can keep adding API integrations to the `module_utils` directory and use them as required.