import yaml
import re
import sys
import os

def build_solution(ra):
    #ra = sys.argv[-1]
    #print ra
    with open("/home/g9983898/shared/delivery/wave/files/fig.yml") as stream:
        data = yaml.safe_load(stream)

    apps = data['apps']
    apps[ra]['image'] = re.sub('\d+(?!\d)$', lambda x:str(int(x.group(0))+1),apps[ra]['image'])
    old_sol_version = "bpdr.io.blueplanet.{}:{}".format(data['solution_name'], data['solution_version'])

    data['solution_version'] = re.sub('\d+(?!\d)$', lambda x: str(int(x.group(0))+1), data['solution_version'])

    with open("/home/g9983898/shared/delivery/wave/files/fig_solution.yml","w") as fig:
        yaml.dump(data, fig, default_flow_style=False)

    ra_tag =  'bpdr.io/{}'.format(apps[ra]['image'])

    os.system("docker tag blueplanet/{}:latest {}".format(ra, ra_tag))
    os.system("docker push {}".format(ra_tag))

    solution_tag = "bpdr.io/blueplanet/solution-{}:{}".format(data['solution_name'], data['solution_version'])
    solution_version = "bpdr.io.blueplanet.{}:{}".format(data['solution_name'], data['solution_version'])

    build_sol = "/home/g9983898/dtkdist-18.10.0-3/bin/solmaker build /home/g9983898/shared/delivery/wave/files/fig_solution.yml --tag={} --vendor=blueplanet --base-image=artifactory.ciena.com/blueplanet/base-image-devops-toolkit:20180912".format(data['solution_version'])

    os.system(build_sol)
    os.system("docker push {}".format(solution_tag))

    return (old_sol_version, solution_version)

if __name__ == '__main__':
    pass
