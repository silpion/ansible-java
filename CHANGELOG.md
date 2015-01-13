# 0.6.0

Mark Kusch (2):
      Add support to install JCE policy for unlimited strength cryptography

# 0.5.1

Mark Kusch (9):
      Update ubuntu-upstart-sshkey container to version 1.0.0
      Provide cow in ansible managed templates
      This role will not deal with OpenJDK anymore for complexity reasons
      Cleanup defaults/ vs vars/
      Proper sudo management (based on github#4)
      Provide build/test instructions for travis (based on github#4)
      Update integration testing to work with Serverspec 2.N
      Update Java to install 7u71 by default
      Add support for current java 8u25 (build 17)

Sebastian Davids (1):
      MOD - add missing java_oracle_version_update role variable

# 0.5.0

Mark Kusch (15):
      Update variables documentation
      Add integration test infrastructure
      Persistent java_home fact
      Basic documentation for the java_home fact
      Fix java facts
      Update documentation formatting
      Enable custom local facts for other roles
      Do not add runtime facts
      Revert removal of runtime facts
      Provide some usage documentation for custom local facts
      Allow configuration of curl cookie for automated Oracle distribution downloads
      Move role version to dedicated file
      Remove variables from ansible_ scope to prevent clashes
      Update task description for local ansible data path directory creation
      Fix wrong tag name (thx to review)

# 0.0.1

* Initial commit.


<!-- vim: set nofen ts=4 sw=4 et: -->
