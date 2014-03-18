# ansible-java

Install Java JRE or JDK with either one of Oracle or OpenJDK
implementation, or both.


# Architecture

The role downloads redistributable packages from the internet
to the hosts local filesystem before it may install those on
any number of managed nodes in the local network.

Downloads are performed with the command module using curl.
It is required to have curl installed on the local host you
are running ansible-playbook on to manage nodes (your workstation).

This dependency is not managed within this role as it feels
that there is no way to install packages with local_action
based on ansible_os_family/ansible_distribution when conditionals.
These facts have values suitable to the managed node but to
the host running ansible-playbook on.

Please: Proove me wrong!


# ToDos

- Implement support for OpenJDK.
- (Allow local installation of cURL IF possible.)


# Role variables

## java_default_implementation

Configure default Java implementation.
Choices:
- oracle
- openjdk
Default: oracle


## java_default_distribution

Configure default Java distribution.
Choices:
- jre
- jdk
Default: jdk


## java_openjdk_when


## java_openjdk_version_*

### java_openjdk_version_major

### java_openjdk_version_minor

### java_openjdk_version_patch


## java_oracle_when

Set "true" when Oracle Java implementation should get installed.
Default: true


## java_oracle_version_*

Default: 1.7.0_51-b13 (7u51-b13)

### java_oracle_version_major

Default: 1

### java_oracle_version_minor

Default: 7

### java_oracle_version_patch

Default: 0

### java_oracle_version_build

Default: 13


## java_oracle_redis_jdk_sha256sum

SHA256 sum for the downloaded Oracle Java JDK redistributable package.
Default: 77367c3ef36e0930bf3089fb41824f4b8cf55dcc8f43cce0868f7687a474f55c

## java_oracle_redis_jre_sha256sum

SHA256 sum for the downloaded Oracle Java JRE redistributable package.
Default:


# Dependencies

None.


# License

Apache Version 2.0


# Author

Mark Kusch @mark.kusch silpion.de


<!-- vim: set ts=4 sw=4 et nofen: -->
