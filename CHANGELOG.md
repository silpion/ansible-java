# 2.2.1

Anja Siek (3):

* update generator
* use variable instead of hardcoded lib role path

Mark Kusch (1):

* Reduce test playbook for ansible-java

Ruslan Tumarkin (1):

* Add two new supported versions: 8u101, 8u102

# 2.2.0

Alvaro Aleman (1):

* Only do upgrades when explicitly asked

Mark Kusch (12):

* Re-run ansible-generator
* Re-run ansible-generator (part 2)
* Fixup java\_keystore\_certificates variable undefined
* Provide separation for better role testing
* Add role\_version fact
* Use ansible\_check\_mode fact
* ansible-java now requires min\_ansible\_version >= 2.1.N
* Remove leftover keystore test playbook
* Use package module in favor of action: {{ fact }}
* Fedora 23 has no python 2
* Fix vagrant bug with galaxy\_roles\_path
* Fixup Vagrant/ansible-galaxy for Vagrant >= 1.8.4

Nathan Mische (1):

* Fixing keystore for Ansible 2.1.0.0

# 2.1.0

Ludovic Claude (1):

* Use local become settings from sipion.util

Mark Kusch (3):

* Fix ansible v2 deprecation warnings
* Do not hardcode privilege escalation
* Remove stub become configuration

# 2.0.3

Mark Kusch (1):

* PEBKAC

# 2.0.2

Mark Kusch (1):

* Fixup dependency management

# 2.0.1

Mark Kusch (4):

* Re-add dependency to silpion.util
* ansible-galaxy shall install both lib and util roles
* Minor documentation "fixes" related to dependencies

# 2.0.0

Anja Siek (2):

* fix keystore module for v2 compatibility

Mark Kusch (12):

* Add dependency to min Ansible version 2.0.0.2
* Update documentation to be hopefully more meaningful
* Wrap util\_template\_use\_cow variable for templates
* Use lib\_ variables for templates
* Update dependencies from util to lib
* ansible-java librification
* Do not download anything in --check mode operations
* Do not allow curl to hang the play forever

# 1.6.0

Alvaro Aleman (1):

* Add java\_download tag to all required tasks

Mark Kusch (2):

* Ensure version specific sha256sum templates
* Add latest 8 and 7 for jre, jdk and srv to test playbook<Paste>

# 1.5.1

Mark Kusch (3):

* Add documentation for server-jre distribution support starting with 7u80 in Java 7 tree
* Add missing sha256sums for 7u80 server-jre distribution
* Fixup wrong sha256sum for 7u80 JRE distribution (thx to WeVaSoft)

# 1.5.0

Alvaro Aleman (2):

* Add \*.swp to gitignore
* Add Java 7u80 support

# 1.4.0

Marc Rohlfs (3):

* Added version var definition for latest Java version 8u60 and set it as role default.
* Added version var definition for Java version 7u21.
* Fixed path to keytool - it must not be hardcoded.

Mark Kusch (7):

* Update default Java version to 8u66
* Remove redundant tasks
* Add support for Oracle server-jre
* Update documentation for server-jre support and default versions
* Fix "the inline if-expression on line 1 evaluated to false and no else section was defined"
* Use complex args coding style
* Use true and false for boolean arguments

Ruslan Tumarkin (1):

* Add 8u65 as supported version

# 1.3.0

Alvaro Aleman (4):

* Added always_run=yes to fact gathering tasks, introduced java_download tag
* Readme: Added checkmode description
* use true instead of yes for booleans
* tdd functionality updated

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
