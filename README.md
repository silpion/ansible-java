# ansible-java

Install Oracle Java.

## Compatibility

### ansible-java 0.7.0

Starting with this role version, inventory configuration for pinned
versions of Java to be installed has changed.
To pin a version it is enough to configure ``java_oracle_version``
which requires ``vars/versions/{{ java_oracle_version }}.yml`` to be
configured.

Starting with this role version the variable to choose between JDK or
JRE has been renamed to ``java_oracle_distribution`` for consistency
reasons.

Starting with this role version the default Java version has been
updated to Java8.

## Architecture

The role downloads redistributable packages from the internet
to the hosts local filesystem before it may install those on
any number of managed nodes in the local network.

Downloads are performed with the command module using curl.
It is required to have curl installed on the local host you
are running ansible-playbook on to manage nodes (your workstation).

## Role variables

* ``java_oracle_distribution``: Configure the Java distribution to be installed (default: ``jdk``, values: [``jdk``, ``jre``])
* ``java_oracle_version``: Configure Java version to be installed (string, default: ``8u25``)
* ``java_install_dir``: Base installation directory for any Java implementation/distribution (string, default: ``/opt/java``)

### Versioned variables

Predefined SHA sums and further version specific configuration may get found in
the *vars/versions* directory. When configuring a version, that is not predefined
(so far), the following variables must also be defined in the playbook:

* ``java_oracle_version_major``: Oracle major version
* ``java_oracle_version_minor``: Oracle minor version
* ``java_oracle_version_patch``: Oracle patch version
* ``java_oracle_version_update``: Oracle major version
* ``java_oracle_version_build``: Oracle build version
* ``java_oracle_redis_jdk_sha256sum``: SHA256 sum for the downloaded Oracle Java JDK redistributable package - mandatory when ``java_oracle_distribution`` is ``jdk``
* ``java_oracle_redis_jre_sha256sum``: SHA256 sum for the downloaded Oracle Java JRE redistributable package - mandatory when ``java_oracle_distribution`` is ``jre``
* ``java_oracle_redis_jce_sha256sum``: SHA256 sum for the downloaded Oracle Java JCE policies package
* ``java_oracle_mirror_jce``: Mirror URL for the download of the Oracle Java JCE policies package
* ``java_oracle_redis_jce_filename``:  File name of the Oracle Java JCE policies package
* ``java_oracle_redis_jce_archive_dirname``: Name of the base directory in the Oracle Java JCE policies package

### Supported versions

* 7u51
* 7u71
* 8u20
* 8u25
* 8u31
* 8u45

## Role facts

This role sets persistent facts for other roles to use via

* facts.d ``ansible_local.java.general.java_home``

This variable contains the path to the default JVM configured with this role.

## Dependencies

This role depends on ``groover.util`` role. This is configured
for ``ansible-galaxy install`` in **requirements.yml**.

**NOTE**: Requirements are installed as virtual user ``silpion``
(``silpion.util``)

Be sure to install required roles with

    ansible-galaxy install --role-file requirements.yml

* [groover.util](https://github.com/silpion/ansible-util)

## License

Apache Version 2.0

## Author

Mark Kusch @mark.kusch silpion.de
Marc Rohlfs @marc.rohlfs silpion.de

### Contributors

* Lars Maehlmann @lars.maehlmann silpion.de
* Sebastian Davids @sebastian.davids silpion.de
* [ludovicc](https://github.com/ludovicc)
* [nixlike](https://github.com/nixlike)
* [trumant](https://github.com/trumant)


<!-- vim: set ts=4 sw=4 et nofen: -->
