# Udacity_TournamanetResults
How to install and run the Tournamanet Results

1. Downlaod and install VirtualBox: https://www.virtualbox.org/wiki/Downloads
2. Download and install vagrant: https://www.vagrantup.com/downloads.html
3. Clone this repo to your local machine
4. Via command line navigate to this repo and run `vagrant up`
5. Next run `vagrant ssh`
6. Change directory to vagrant/tournament `cd /vagrant/tournament`
7. Once the virtual machine is running and loggined into run `psql`
8. Run `\i tournament.sql`
9. Run `\q`
10. Finnally run `python tournament_test.py` to run the tests.
