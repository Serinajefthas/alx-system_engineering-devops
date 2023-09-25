#!/usr/bin/env bash
# Connect to server using puppet format
exec { 'echo "PasswordAuthentication no
	IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
        path    => '/bin/'
}
