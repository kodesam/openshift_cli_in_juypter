To use Ansible to get pods in OpenShift, you can use the `oc` command line tool and run it through the `ansible.builtin.command` module. Here's an example playbook:

```yaml
- name: Get pods in OpenShift
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Run oc command to get pods
      ansible.builtin.command: oc get pods -o json
      register: oc_output
    - name: Parse json output
      ansible.builtin.set_fact:
        pod_list: "{{ oc_output.stdout | from_json }}"
    - name: Print pod names
      ansible.builtin.debug:
        msg: "{{ item.metadata.name }}"
      with_items: "{{ pod_list.items }}"
```

In this playbook, we first run the `oc get pods -o json` command using the `ansible.builtin.command` module and register the output in the `oc_output` variable. We then use the `set_fact` module to parse the JSON output into the `pod_list` variable.

Finally, we iterate over the `pod_list.items` and print the names of each pod using the `debug` module.

You can run this playbook using the `ansible-playbook` command:

```
ansible-playbook get_pods.yaml
```