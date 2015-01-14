# ansible-java

Install Oracle Java.

## Architecture

The role downloads redistributable packages from the internet
to the hosts local filesystem before it may install those on
any number of managed nodes in the local network.

Downloads are performed with the command module using curl.
It is required to have curl installed on the local host you
are running ansible-playbook on to manage nodes (your workstation).

## Role variables

* ``java_default_distribution``: Configure default Java distribution (default: ``jdk``, values: [``jdk``, ``jre``])
* ``java_oracle_version``: Configure Java version to be installed (string, default: ``8u25``)

### Versioned variables

Predefined SHA sums and further version specific configuration may get found in
the *vars/versions* directory. When configuring a version, that is not predefined
(so far), the following variables must also be defined in the playbook:

* ``java_oracle_version_major``: Oracle major version
* ``java_oracle_version_minor``: Oracle minor version
* ``java_oracle_version_patch``: Oracle patch version
* ``java_oracle_version_update``: Oracle major version
* ``java_oracle_version_build``: Oracle build version
* ``java_oracle_redis_jdk_sha256sum``: SHA256 sum for the downloaded Oracle Java JDK redistributable package - mandatory when ``java_default_distribution`` is ``jdk``
* ``java_oracle_redis_jre_sha256sum``: SHA256 sum for the downloaded Oracle Java JRE redistributable package - mandatory when ``java_default_distribution`` is ``jre``
* ``java_oracle_redis_jce_sha256sum``: SHA256 sum for the downloaded Oracle Java JCE policies package
* ``java_oracle_mirror_jce``: Mirror URL for the download of the Oracle Java JCE policies package
* ``java_oracle_redis_jce_filename``:  File name of the Oracle Java JCE policies package
* ``java_oracle_redis_jce_archive_dirname``: Name of the base directory in the Oracle Java JCE policies package

### Supported versions

* 7u51
* 7u71
* 8u20
* 8u25

## Role facts

This role sets persistent facts for other roles to use via

* facts.d ``ansible_local.java.general.java_home``

This variable contains the path to the default JVM configured with this role.

## Dependencies

None.

## License

Apache Version 2.0

## Author

Mark Kusch @mark.kusch silpion.de


<!-- vim: set ts=4 sw=4 et nofen: -->
