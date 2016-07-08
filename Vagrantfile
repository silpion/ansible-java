# vim: set ft=ruby ts=2 sw=2 et:
# -*- mode: ruby -*-


VAGRANT_API_VERSION = '2'
Vagrant.configure(VAGRANT_API_VERSION) do |config|

  # user based configuration with nugrant
  #   - vagrant plugin: https://github.com/maoueh/nugrant
  #
  # defaults for user configurable items
  cfg = {
    'vm' => {
      'box' => 'centos/7',
      'check_update' => false,
      'synced_folders' => false
    },
    'provisioner' => {
      'ansible' => {
        'verbose' => nil,
        'diff' => nil,
        'ask_sudo_pass' => false,
        'ask_vault_pass' => false
      }
    }
  }

  if Vagrant.has_plugin?('nugrant')
    # get defaults from cfg as user defaults
    config.user.defaults = cfg
    c = config.user
  else
    c = cfg
  end


  # vm configuration
  config.vm.box = ENV['ANSIBLE_JAVA_VAGRANT_BOXNAME'] || c['vm']['box']
  config.vm.box_check_update = c['vm']['check_update']

  config.vm.define :ansiblejavatest do |d|

    d.vm.hostname = 'ansiblejavatest'
    if not c['vm']['synced_folders']
      d.vm.synced_folder '.', '/vagrant', id: 'vagrant-root', disabled: true
      d.vm.synced_folder '.', '/home/vagrant/sync', id: 'vagrant-root', disabled: true
    end

    # provisioner configuration

    #   ansible-galaxy dependency managemant
    d.vm.provision "galaxy", type: :ansible do |ansible|
      ansible.playbook = 'tests/test.yml'
      ansible.galaxy_roles_path = 'tests/roles/:../'
      ansible.galaxy_role_file = 'tests/requirements.yml'
      ansible.galaxy_command = 'ansible-galaxy install --role-file=%{role_file} --roles-path=tests/roles/ --ignore-errors --force'
    end

    #   default ansible play with various middleware versions
    d.vm.provision "versions", type: :ansible do |ansible|
      ansible.playbook = 'tests/test.yml'
      ansible.groups = {
        'vagrant_versions' => ['ansiblejavatest']
      }
      ansible.limit = 'vagrant_versions'

      #   dynamic ansible-playbook configuration based on environment variables
      ansible.tags = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_TAGS']
      ansible.skip_tags = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_SKIP_TAGS']
      #   dynamic ansible-playbook configuration based on environment variables or user configuration
      ansible.verbose = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_VERBOSE'] || c['provisioner']['ansible']['verbose']

      # ansible-playbook raw arguments
      ansible.raw_arguments = []

      if ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_CHECKMODE'] == '1'
        ansible.raw_arguments << '--check'
      end

      if ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_DIFFMODE'] == '1' or c['provisioner']['ansible']['diff']
        ansible.raw_arguments << '--diff'
      end

    end

    #   keystore play
    d.vm.provision "keystore", type: :ansible do |ansible|
      ansible.playbook = 'tests/test.yml'
      ansible.groups = {
        'vagrant_keystore' => ['ansiblejavatest']
      }
      ansible.limit = 'vagrant_keystore'

      #   dynamic ansible-playbook configuration based on environment variables
      ansible.tags = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_TAGS']
      ansible.skip_tags = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_SKIP_TAGS']
      #   dynamic ansible-playbook configuration based on environment variables or user configuration
      ansible.verbose = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_VERBOSE'] || c['provisioner']['ansible']['verbose']

      # ansible-playbook raw arguments
      ansible.raw_arguments = []

      if ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_CHECKMODE'] == '1'
        ansible.raw_arguments << '--check'
      end

      if ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_DIFFMODE'] == '1' or c['provisioner']['ansible']['diff']
        ansible.raw_arguments << '--diff'
      end

    end

    #   current versions plays
    d.vm.provision "current", type: :ansible do |ansible|
      ansible.playbook = 'tests/test.yml'
      ansible.groups = {
        'vagrant_current' => ['ansiblejavatest']
      }
      ansible.limit = 'vagrant_current'

      #   dynamic ansible-playbook configuration based on environment variables
      ansible.tags = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_TAGS']
      ansible.skip_tags = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_SKIP_TAGS']
      #   dynamic ansible-playbook configuration based on environment variables or user configuration
      ansible.verbose = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_VERBOSE'] || c['provisioner']['ansible']['verbose']

      # ansible-playbook raw arguments
      ansible.raw_arguments = []

      if ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_CHECKMODE'] == '1'
        ansible.raw_arguments << '--check'
      end

      if ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_DIFFMODE'] == '1' or c['provisioner']['ansible']['diff']
        ansible.raw_arguments << '--diff'
      end

    end

    #   idempotency play
    d.vm.provision "idempotency", type: :ansible do |ansible|
      ansible.playbook = 'tests/test.yml'
      ansible.groups = {
        'vagrant_idempotency' => ['ansiblejavatest']
      }
      ansible.limit = 'vagrant_idempotency'

      #   dynamic ansible-playbook configuration based on environment variables
      ansible.tags = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_TAGS']
      ansible.skip_tags = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_SKIP_TAGS']
      #   dynamic ansible-playbook configuration based on environment variables or user configuration
      ansible.verbose = ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_VERBOSE'] || c['provisioner']['ansible']['verbose']

      # ansible-playbook raw arguments
      ansible.raw_arguments = []

      if ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_CHECKMODE'] == '1'
        ansible.raw_arguments << '--check'
      end

      if ENV['ANSIBLE_JAVA_VAGRANT_ANSIBLE_DIFFMODE'] == '1' or c['provisioner']['ansible']['diff']
        ansible.raw_arguments << '--diff'
      end

    end


    # vm configuration
    d.vm.provider :virtualbox do |v|
      v.customize 'pre-boot', ['modifyvm', :id, '--nictype1', 'virtio']
      v.customize [ 'modifyvm', :id, '--name', 'ansiblejavatest', '--memory', '1024', '--cpus', '1' ]
    end

    d.vm.provider :libvirt do |lv|
      lv.memory = 1024
      lv.cpus = 1
    end

  end

end
