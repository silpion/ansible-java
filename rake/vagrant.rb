require 'rake'
require 'rspec/core/rake_task'


desc "Bring up Vagrant VM"
task :up do
  if ENV['ANSIBLE_JAVA_VAGRANT_PROVIDER']
    sh 'vagrant', 'up', '--no-provision', '--provider', ENV['ANSIBLE_JAVA_VAGRANT_PROVIDER']
  else
    sh %{vagrant up --no-provision}
  end
end


desc "ansible-galaxy install..."
task :galaxy do
  sh %{vagrant provision --provision-with galaxy}
end

desc "ansible-playbook --limit vagrant_versions"
task :versions => [:up] do
  sh %{vagrant provision --provision-with versions}
end

desc "ansible-playbook --limit vagrant_keystore"
task :keystore => [:up] do
  sh %{vagrant provision --provision-with keystore}
end

desc "ansible-playbook --limit vagrant_current"
task :current => [:up] do
  sh %{vagrant provision --provision-with current}
end

desc "ansible-playbook --limit vagrant_idempotency"
task :idempotency => [:current] do
  sh %{vagrant provision --provision-with idempotency}
end


desc "Provision Vagrant VM"
task :provision => [:galaxy, :versions, :keystore, :idempotency] do
end


desc "Cleanup Vagrant VM environment"
task :clean do
  if not ENV['RAKE_ANSIBLE_VAGRANT_DONT_CLEANUP'] == '1'
    sh %{vagrant halt}
    sh %{vagrant destroy --force}
  end
end


desc "SSH into the Vagrant VM"
task :ssh do
  sh %{vagrant ssh}
end
