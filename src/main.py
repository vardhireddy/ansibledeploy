from buildsolution import build_solution
import os
import sys
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def undeploy():
    try:
        os.system("ansible-playbook runsetup.yml --tags 'undeploy' --extra-vars 'version={}'".format(old_version))
        deploy()
    except Exception as e:
        rollback()
        logging.error(e)

def deploy():
    try:
        os.system("ansible-playbook runsetup.yml --tags 'deploy' --extra-vars 'version={}'".format(new_version))
    except Exception as e:
        logging.error(e)

def pull():
    try:
        os.system("ansible-playbook runsetup.yml --skip-tags 'undeploy, deploy, rollback'")
    except Exception as e:
        logging.error(e)


def rollback():
    try:
        os.system("ansible-playbook runsetup.yml --tags 'rollback' --extra-vars 'version={}'".format(old_version))
    except Exception as e:
        logging.error(e)

pull()
ra = sys.argv[-1]
old_version, new_version = build_solution(ra)
print old_version
print new_version
undeploy()



