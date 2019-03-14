# __Author__ : Indu Sharma
# __Date__ : 14/03/2019
# __About__ : Metricbeat Install, Configure and operate

from core.utils.fabric_utils import run_command_with_sudo, copy_file_to_remote
from core.utils import global_constants
import yaml

stream = file('../configs/configs.yml')
confs = yaml.safe_load(stream=stream)
ips = confs['metricbeat_nodes']
index = confs['elastic_index']
es_ui = confs['elastic_url']


class MetricBeat:
    def __init__(self, index):
        self.index = index
        self.configure()

    @staticmethod
    def install(ip):
        commands = ["rpm -e metricbeat",
                    "curl -L -O https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-6.3.0-x86_64.rpm",
                    "rpm -vi metricbeat-6.3.0-x86_64.rpm"]
        map(lambda x: run_command_with_sudo(ip, global_constants.DEFAULT_SERVER_USERNAME,
                                            global_constants.DEFAULT_SERVER_PASSWORD, x), commands)

    def configure(self):
        stream = file('../third_party/metricbeat/metricbeat.yml')
        confs = yaml.safe_load(stream=stream)
        confs['output.elasticsearch']['index'] = self.index + '-%{+yyyy.MM.dd}'
        confs['output.elasticsearch']['hosts'] = [es_ui]
        confs['setup.template.name'] = self.index
        confs['setup.template.pattern'] = self.index + '-*'
        with open('../third_party/metricbeat/metricbeat_copy.yml', 'w') as outfile:
            yaml.dump(confs, outfile, default_flow_style=False)

    def _copy(self, ip):
        copy_file_to_remote(ip, global_constants.DEFAULT_SERVER_USERNAME, global_constants.DEFAULT_SERVER_PASSWORD,
                            '../third_party/metricbeat/metricbeat_copy.yml',
                            '/etc/metricbeat/metricbeat.yml')
        run_command_with_sudo(ip, global_constants.DEFAULT_SERVER_USERNAME, global_constants.DEFAULT_SERVER_PASSWORD,
                              'chown root:root /etc/metricbeat/metricbeat.yml;chmod go-w /etc/metricbeat/metricbeat.yml')

    def start(self, ip):
        self._copy(ip)
        run_command_with_sudo(ip, global_constants.DEFAULT_SERVER_USERNAME, global_constants.DEFAULT_SERVER_PASSWORD,
                              "service metricbeat start")

    @staticmethod
    def stop(ip):
        run_command_with_sudo(ip, global_constants.DEFAULT_SERVER_USERNAME, global_constants.DEFAULT_SERVER_PASSWORD,
                              "service metricbeat stop")


def metricbeat(operations="install,stop,start"):
    operations_support = operations.split(',')
    Obj = MetricBeat(index)

    def func(ip):
        [getattr(Obj, operation)(ip) for operation in operations_support]

    for ip in ips:
        func(ip)
