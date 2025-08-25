Week 1 – Foundations (YAML + Ansible Basics)

Goal: Get comfortable with YAML and writing very small playbooks.

Day 1 → Learn YAML basics (lists, dictionaries, indentation). Write a sample YAML file.

Day 2 → Write your first playbook: create a file with copy module.

Day 3 → Install a package (nginx or apache2) with apt/yum.

Day 4 → Manage services (start, stop, restart).

Day 5 → Create users & groups with Ansible.

Day 6 → Write a playbook with multiple tasks (install + configure + start service).

Day 7 → Revise: Run all your playbooks on a test VM.

Week 2 – Variables, Loops, Conditionals

Goal: Learn to make playbooks dynamic.

Day 8 → Use variables (vars: and vars_files).

Day 9 → Write a playbook that installs packages from a variable list.

Day 10 → Use when (conditionals) → e.g., different tasks for Ubuntu vs CentOS.

Day 11 → Use with_items loop → create multiple users.

Day 12 → Use register to capture command outputs.

Day 13 → Create templates with Jinja2 (templates/hello.j2).

Day 14 → Revise: Build a playbook to install + configure + start Nginx with custom index.html.

Week 3 – Handlers, Roles, Reusability

Goal: Write structured, production-like playbooks.

Day 15 → Learn handlers (e.g., restart service after config change).

Day 16 → Tag your tasks and run selective tasks with --tags.

Day 17 → Break playbook into roles (roles/webserver/tasks/main.yml).

Day 18 → Create a role for user management.

Day 19 → Create a role for webserver installation.

Day 20 → Use both roles in a single playbook.

Day 21 → Revise: Full stack playbook (user creation + nginx + handler).

Week 4 – Advanced (Vault, Inventory, AWS Integration)

Goal: Learn secure, real-world practices.

Day 22 → Use Ansible Vault to store passwords.

Day 23 → Write playbook with a dynamic inventory (AWS EC2 plugin).

Day 24 → Create an S3 bucket using community.aws.s3_bucket.

Day 25 → Create an EC2 instance using Ansible.

Day 26 → Write playbook to deploy code from GitHub to EC2.

Day 27 → Combine everything into an end-to-end playbook.

Day 28 → Final revision: run through all examples, fix mistakes, and document learnings.