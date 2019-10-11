# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # Specific configuration for Django
  config.vm.define "django" do |django|
    django.vm.box = "hashicorp/bionic64"
    django.vm.hostname = "django"
    django.vm.network "private_network", ip: "10.0.0.10"
    django.vm.network "forwarded_port", guest: 8000, host: 8000
    django.vm.provision "shell", path: "djangobootstrap.sh", privileged: false
  end

  # Specific configuration for postgresql
  config.vm.define "postgres" do |postgres|
    postgres.vm.box = "hashicorp/bionic64"
    postgres.vm.hostname = "postgres"
    postgres.vm.network "private_network", ip: "10.0.0.11"
    postgres.vm.network "forwarded_port", guest: 5432, host: 5432
    postgres.vm.provision "shell", path: "postgresbootstrap.sh", privileged: false
  end

  # Provision all vm's with this first - runs updates.
  config.vm.provision "shell", path: "bootstrap.sh", privileged: false
end
