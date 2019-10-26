#!/usr/bin/env bash
set -e

if hash postgres 2>/dev/null; then
    echo PostgreSQL already configured! Run "vagranat destroy postgres" to reset. 1>&2
else
    echo Installing PostgreSQL... 1>&2
    # add the repository
    sudo tee /etc/apt/sources.list.d/pgdg.list <<END
    deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main
END

    # get the signing key and import it
    wget https://www.postgresql.org/media/keys/ACCC4CF8.asc
    sudo apt-key add ACCC4CF8.asc
    # sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7FCC7D46ACCC4CF8

    # fetch the metadata from the new repo
    sudo apt-get update
    sudo apt-get install -y postgresql-11 || echo "PostgreSQL Installation Failed" 1>&2
    echo PostgreSQL installed successfully! 1>&2

    echo Configuring Metrics Database... 1>&2
    sudo -u postgres psql <<__END__
    CREATE USER metrics WITH PASSWORD 'metrics';
    CREATE DATABASE csci_metrics;
    GRANT ALL PRIVILEGES ON DATABASE csci_metrics TO metrics;
    \q
__END__

    sudo sed -i 's/^#listen_addresses = .*/listen_addresses = '\''*'\''/' /etc/postgresql/11/main/postgresql.conf
    echo "host all all 0.0.0.0/0 md5" | sudo tee -a /etc/postgresql/11/main/pg_hba.conf
    sudo service postgresql restart
    echo Database configured! 1>&2
fi

echo Setup Complete! 1>&2