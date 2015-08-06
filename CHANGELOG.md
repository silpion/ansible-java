# 1.2.0

Ludovic Claude (1):

* Add Java 8u51

# 1.1.1

Mark Kusch (1):

* Fix: stderr: fish: Expected a command name, got token of type “Run job in background”.

# 1.1.0

Mark Kusch (5):

* Abstract supported platform in vars
* Maintain default places where to find shasum binaries
* Allow to configure shasum binary for local\_action: command when validating shasums

# 1.0.0

Marc Rohlfs (1):

* Fixed markdown

Mark Kusch (16):

* Draft: Manage Java keystores with the keystore module
* Create test SSL certificates with "usable" CN names
* Add support for create=BOOLEANS argument
* Make keytool= argument optional
* Do not add compiled Python code to the repository
* This role now requires ansible version 1.9
* s/sudo/become/g and proper sudo management again
* Add copy and creates arguments to keystore: module
* Install custom keystore when running vagrant
* Pre-checking shasums will not generate change events anymore
* Use util\_package\_state configuration from util role when installing packages
* Do not generate changed events when installing JCE

# 0.10.0

Travis Truman (1):

* Adding vars for 8u45

Mark Kusch (3):

* Add example playbook and contribution documentation
* Add supported versions to documentation and add trumant to contributors list
* Default Java to 8u45

# 0.9.0

Mark Kusch (5):

* Qualify galaxy meta data
* Allow ansible-galaxy install to install required dependencies
* Documentation for groover.util role dependency
* Implement util_template_use_cow variable to templates
* Use capabilities of groover.util role

# 0.8.0

Marc Rohlfs (3):

* Variables that should be overwritable must be moved to defaults/main.yml.
* Replaced hard coded patch version with proper variable substitution.
* Added version var definition for latest Java version 8u31 and set it as role default.

# 0.7.0

Mark Kusch (1):

* Add compatibility notes to documentation

Marc Rohlfs (4):

* Improved patterns for files to be ignored by Git.
* Removed obsolete files.
* Improved and simplified configuration of the Java version.
* Changed name of var ``java_default_distribution`` to ``java_oracle_distribution``.

# 0.6.0

Mark Kusch (2):

* Add support to install JCE policy for unlimited strength cryptography

# 0.5.1

Mark Kusch (9):

* Update ubuntu-upstart-sshkey container to version 1.0.0
* Provide cow in ansible managed templates
* This role will not deal with OpenJDK anymore for complexity reasons
* Cleanup defaults/ vs vars/
* Proper sudo management (based on github#4)
* Provide build/test instructions for travis (based on github#4)
* Update integration testing to work with Serverspec 2.N
* Update Java to install 7u71 by default
* Add support for current java 8u25 (build 17)

Sebastian Davids (1):

* MOD - add missing java_oracle_version_update role variable

# 0.5.0

Mark Kusch (15):

* Update variables documentation
* Add integration test infrastructure
* Persistent java_home fact
* Basic documentation for the java_home fact
* Fix java facts
* Update documentation formatting
* Enable custom local facts for other roles
* Do not add runtime facts
* Revert removal of runtime facts
* Provide some usage documentation for custom local facts
* Allow configuration of curl cookie for automated Oracle distribution downloads
* Move role version to dedicated file
* Remove variables from ansible_ scope to prevent clashes
* Update task description for local ansible data path directory creation
* Fix wrong tag name (thx to review)

# 0.0.1

* Initial commit.


<!-- vim: set nofen ts=4 sw=4 et: -->
