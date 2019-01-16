`sudo rm /etc/resolv.conf` <br>
`sudo ln -s ../run/resolvconf/resolv.conf /etc/resolv.conf` <br>
`sudo resolvconf -u` <br>
and maybe <br>
`sudo service network-manager restart` <br>
