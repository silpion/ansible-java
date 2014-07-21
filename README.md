# ansible-java

Install Java JRE or JDK with either one of Oracle or OpenJDK
implementation, or both.


## Architecture

The role downloads redistributable packages from the internet
to the hosts local filesystem before it may install those on
any number of managed nodes in the local network.

Downloads are performed with the command module using curl.
It is required to have curl installed on the local host you
are running ansible-playbook on to manage nodes (your workstation).


## ToDos

- Implement support for OpenJDK.


## Role variables

* ``java_default_implementation``: Configure default Java implementation (default: ``oracle``, values: [``oracle``, ``openjdk``])
* ``java_default_distribution``: Configure default Java distribution (default: ``jdk``, values: [``jdk``, ``jre``])

### OpenJDK

* ``java_openjdk_when``: Run OpenJDK specific automation only when set true (default: ``false``)
* ``java_openjdk_version_major``: OpenJDK major version (default: "")
* ``java_openjdk_version_minor``: OpenJDK minor version (default: "")
* ``java_openjdk_version_patch``: OpenJDK patch version (default: "")

### Oracle

* ``java_oracle_when`` Run Oracle specific automation only when set true (default: ``true``)
* ``java_oracle_version_major``: Oracle major version (default: ``1``)
* ``java_oracle_version_minor``: Oracle minor version (default: ``7``)
* ``java_oracle_version_patch``: Oracle patch version (default: ``0``)
* ``java_oracle_version_build``: Oracle build version (default: ``13``)

Default version information generates ``1.7.0_51-b13`` (7u51-b13) as Oracle Java version.

* ``java_oracle_redis_jdk_sha256sum``: SHA256 sum for the downloaded Oracle Java JDK redistributable package (default: ``77367c3ef36e0930bf3089fb41824f4b8cf55dcc8f43cce0868f7687a474f55c``)
* ``java_oracle_redis_jre_sha256sum``: SHA256 sum for the downloaded Oracle Java JRE redistributable package (default: ``a8ef4fd8403398f9c2579bb97b5e6643661dabd510e4c3b79529ede9e1f8584a``)


## Dependencies

None.


## License

Apache Version 2.0


## Author

Mark Kusch @mark.kusch silpion.de


<!-- vim: set ts=4 sw=4 et nofen: -->
