import jenkins

import config

server = jenkins.Jenkins("http://k9-ThinkPad-L14-Gen-2:8080", username=config.jenk_uname, password=config.jenk_pass)
jobs = server.get_jobs()



server.create_job('config_test', config_xml="Jenkinsfile")

print(jobs)
