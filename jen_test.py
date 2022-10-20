import jenkins
import xml.etree.ElementTree as ET
import os
import pout
import config

server = jenkins.Jenkins("http://k9-ThinkPad-L14-Gen-2:8080", username=config.jenk_uname, password=config.jenk_pass)

server.create_job('freestyle-job', jenkins.EMPTY_CONFIG_XML)
config = server.get_job_config('freestyle-job')
pout.v(config)


# def convert_xml_file_to_str():
#     tree = ET.parse('/home/praveenbabu/dollartree/config.xml')
#     root = tree.getroot()
#     return ET.tostring(root, encoding='utf8', method='xml').decode()
#
# def main():
#     target_server = jenkins.Jenkins('http://localhost:8080',
#     username=os.getenv('username'), password=os.getenv('password'))
#     config = convert_xml_file_to_str()
#     target_server.create_job('pipeline-job', config)
#     pout.v(config)
# main()
#
# server = jenkins.Jenkins("http://k9-ThinkPad-L14-Gen-2:8080", username=config.jenk_uname, password=config.jenk_pass)
# jobs = server.get_jobs()
#
#
#
# # server.create_job('config_test', config_xml="Jenkinsfile")
# #
# # print(jobs)
