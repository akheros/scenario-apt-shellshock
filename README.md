This scenario presents a web server being attacked by three attackers. The first 
attacker conducts a full attack campaign while the other two are more 
opportunistic.


## Installation

This scenario requires a webserver vulnerable to `shellshock`. By default we use 
`apache 2.4.10` on `Fedora 20`. The software necessary for the first attacker 
and the victim can be installed using `ansible`. The playbooks are in the 
`install` folder. Remember to check that the `inventory` points to the right 
VMs. Vagrant inserts ssh keys; to use them call ansible like so:

```shell
$ ansible-playbook -i inventory site.yml --private-key ../../.vagrant/machines/attacker1/virtualbox/private_key
```


## Running the scenario.

This scenario is fully automated. Simply run it using `moirai play`.

