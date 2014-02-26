# ansible-java

Install Java JDK either with Oracle or OpenJDK implementation, or both.
Does nothing if neither java\_openjdk\_when nor java\_oracle\_when set
true.


# ToDos

- Automatically set java_default_implementation when only one
  implementation gets installed.
- Allow to configure the default implemantation based on a single
  template.
- Implement support for OpenJDK.
- Implement support to install a JRE only.


# Role variables

Set "true" when OpenJDK Java should get installed.
- java_openjdk_when [false]

Configure OpenJDK version to use.
- java_openjdk_version

Set "true" when Oracle Java JDK should get installed.
- java_oracle_when [false]

Configure Oracle JDK version to use.
- java_oracle_version [7u51]

Configure Oracle JDK build to use.
- java_oracle_build [b13]

SHA256 sum for the downloaded Oracle Java JDK redistributable package.
- java_oracle_sha256sum [77367c3ef36e0930bf3089fb41824f4b8cf55dcc8f43cce0868f7687a474f55c]

Setup the default implementation of Java to use.
Must get set to 'openjdk' if Oracle is not get installed.
- java_default_implementation [oracle]

# Dependencies

None.


# License

Apache Version 2.0


# Author

Mark Kusch @mark.kusch silpion.de


<!-- vim: set ts=4 sw=4 et nofen: -->
