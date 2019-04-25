========================
Installation of the VSDK
========================

.. contents:: Contents

Development set-up
~~~~~~~~~~~~~~~~~~

This are the instructions to install the VSDK on your local machine.
#TODO

Deployment on a Raspberry Pi or other server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These instructions will guide you to the process of installing the VSDK in a production environment, i.e. as a server of a voice-application that is deployed in the field. As the VSDK is intended to be used on the KasaDaka [1]_ voice-service platform, we will focus on this situation. If you want to use the VSDK in some other setup, the process is probably very similar.

In this guide we assume that the following dependencies are installed:
- Python 3 (including PIP)
- Apache 2
- Git

Note that this installation uses the default SQLite database implementation. For deployments that have more than one concurrent user, PostgreSQL is recommended.


# create a directory for the VSDK files and clone the application
  - ``mkdir /var/www/VSDK``
  - ``cd /var/www/VSDK``
  - ``git clone https://github.com/abaart/KasaDaka-VSDK.git .``
# Give the www-data (Apache) user rights to these files
  - ``sudo chown www-data -R /var/www/VSDK``
# Install the Python virtualenv package
  - ``sudo pip install virtualenv``
# Create a virtualenv with the required packages for the VSDK
  - ``sudo -u www-data virtualenv -p python3 venv``
  - ``source venv/bin/activate``
  - ``pip install -r requirements.txt``
# Insert the default data (or a dump of the data for your application) into the database.
  - ``

TODO: change secret key

.. [1] https://kasadaka.com
