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
* ``java_oracle_version_major``: Oracle major version (default: ``1``)
* ``java_oracle_version_minor``: Oracle minor version (default: ``7``)
* ``java_oracle_version_patch``: Oracle patch version (default: ``0``)
* ``java_oracle_version_update``: Oracle major version (default: ``51``)
* ``java_oracle_version_build``: Oracle build version (default: ``13``)

Default version information generates ``1.7.0_51-b13`` (7u51-b13) as Oracle Java version.

### Versioned variables

SHA sums and version specific configuration may get found in vars/versions
directory. Default version configuration from this role lives in

* vars/versions/default.yml

and defaults to the following values:

* ``java_oracle_redis_jdk_sha256sum``: SHA256 sum for the downloaded Oracle Java JDK redistributable package (default: ``77367c3ef36e0930bf3089fb41824f4b8cf55dcc8f43cce0868f7687a474f55c``)
* ``java_oracle_redis_jre_sha256sum``: SHA256 sum for the downloaded Oracle Java JRE redistributable package (default: ``a8ef4fd8403398f9c2579bb97b5e6643661dabd510e4c3b79529ede9e1f8584a``)

### Supported versions

* 7u51
* 8u20

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
