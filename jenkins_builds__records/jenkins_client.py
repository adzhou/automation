from __future__ import print_function
try:
    import jenkins
except ImportError:
    print("please install jenkins api first. for example:")
    print("  pip install jenkins-cli")
    exit(1)
from jenkins import JenkinsException

try:
    import config
    configflag = True
except ImportError:
    configflag = False
    print ('can\'t find config.py file')

LAUNCHER_COMMAND = 'hudson.slaves.CommandLauncher'


def timer(start, end):
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    return ("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))


class JenkinsClient(object):
    def __init__(self, url=None, username=None, password=None):
        # some config
        if configflag:
            self.jenkins_url = url if url else config.Jenkins_url
            self.jenkins_username = username if username else config.Jenkins_username
            self.jenkins_password = password if password else config.Jenkins_password
        else:
            # this url for test.
            self.jenkins_url = url if url else 'http://16.187.186.99:8000/'
            self.jenkins_username = username
            self.jenkins_password = password
        self.server = self.login_jenkins()

    def get_server(self):
        # return server for fast debug .
        return self.server

    def login_jenkins(self):
        # login jenkins
        return jenkins.Jenkins(self.jenkins_url, username=self.jenkins_username, password=self.jenkins_password)

    def logout_jenkins(self):
        pass
        # TODO

    def get_version(self):
        return self.server.get_version()

    def get_all_jobs(self, depth=None):
        return self.server.get_all_jobs(folder_depth=depth)

    def get_job_info_by_name(self, jobname, depth=0):
        return self.server.get_job_info(name=jobname, depth=depth)

    def get_job_config(self, jobname):
        return self.server.get_job_config(jobname)

    def get_jobs_by_view(self, viewname):
        # TODO
        # not work, rewrite it if have time.
        viewconfig = self.server.get_view_config(viewname)
        # return self.server.get_jobs(view_name=viewname, folder_depth=depth)

    def create_job(self, name, configxml):
        self.server.create_job(name, configxml)

    def reconfig_job(self, name, configxml):
        self.server.reconfig_job(name, configxml)

    def get_build_info(self, jobname, number, depth=0):
        return self.server.get_build_info(name=jobname, number=number, depth=depth)

    def get_views(self):
        return self.server.get_views()

    def get_nodes(self):
        return self.server.get_nodes()

    def get_node_config(self, name):
        return self.server.get_node_config(name)

    def get_node_info(self, name, depth=0):
        return self.server.get_node_info(name=name, depth=depth)

    def create_node(self, name, numExecutors=2, nodeDescription=None,
                    remoteFS='/var/lib/jenkins', labels=None, exclusive=False,
                    launcher=LAUNCHER_COMMAND, launcher_params={}):
        self.server.create_node(name=name, numExecutors=numExecutors, nodeDescription=nodeDescription,
                                remoteFS=remoteFS, labels=labels, exclusive=exclusive,
                                launcher=launcher, launcher_params=launcher_params)

    def reconfig_node(self, name, configxml):
        self.server.reconfig_node(name=name, config_xml=configxml)
