Hostsharing-Ansible-InstantPoll
===============================

This Ansible playbook will install the latest InstantPoll release on a server from www.hostsharing.net.

InstantPoll is an open source tool written in Python with Django, that helps speakers to ask the audience for instant feedback. The project lives at https://github.com/ICCM-EU/InstantPoll

To use these modules we have to create a file named ".hsadmin.properties" in the home directory of the package admins. Into that file we have to insert the packagename and password of the package admin. 

Example:

    xyz00@h99:~$ cat .hsadmin.properties 
    xyz00.passWord=insertpkgadminpasswordhere

This file should be protected, else it would be world readable:

    xyz00@h99:~$ chmod 600 .hsadmin.properties

We clone this git-repo to our machine:

    $ git clone https://github.com/tpokorra/Hostsharing-Ansible-InstantPoll.git

Then we change the working directory:

    $ cd Hostsharing-Ansible-InstantPoll

All needed parameters can be set in the inventory file now. Change xyz00 to the name of your package admin. Set the name of a domain, a new user and a password. We can edit the inventory file with:

    $ cp inventory-sample.yml inventory.yml
    $ vim inventory.yml
    
The option -i can be used to read this inventory file instead of the /etc/ansible/hosts file. We want to login with an SSH-Key. We run:

    $ ansible-playbook -i inventory.yml playbook-install.yml

Now we can reach our site via:

    https://poll.example.org

Login with user `admin` and password `admin` and change it at https://poll.example.org/admin/password_change/

--- Open Source Hosting ---
 https://www.hostsharing.net
