from __future__ import print_function
from jenkins_client import JenkinsClient

try:
    import config
    configflag = True
except ImportError:
    configflag = False
    print ('can\'t find config.py file')


class GetBuildsInfoFromJenkins(JenkinsClient):
    def __init__(self, **kwargs):
        super(GetBuildsInfoFromJenkins, self).__init__(**kwargs)
        pass

    def get_all_builds(self):
        jobslist = self.server.get_all_jobs()
        for job in jobslist:
            jobinfo = self.server.get_job_info(job['fullname'])
            print(jobinfo)
            builds = jobinfo['builds']

    def get_build_info(self, jobname, number, depth=0):
        nl = self.get_all_builds_number_by_jobname(jobname)
        if nl[0] > number or nl[1] < number:
            print ('Perhaps the build number you choose not exist : ')
            print ('    we prefer a number among %d and %d, but you select %d' % (nl[0], nl[1], number))
            return {}
        return self.server.get_build_info(name=jobname, number=number, depth=depth)

    def get_build_info_keys(self, jobname, number, depth=0):
        buildinfo = self.get_build_info(jobname, number, depth)
        return buildinfo.keys()

    def get_build_info_modify(self, jobname, number, depth=0):
        buildinfo = self.get_build_info(jobname, number, depth)
        # TODO

    def get_build_info_row_need(self, jobname, number, depth=0, ll=None):
        buildinfo = self.get_build_info(jobname, number, depth)
        if not buildinfo:
            return False
        if not ll:
            ll = config.Build_keys_to_save
        tmpl = []
        for l in ll:
            tmpl.append(buildinfo[l])
        return tmpl

    def get_all_builds_number_by_jobname(self, jobname):
        jobinfo = self.get_job_info_by_name(jobname)
        firstbuild = jobinfo['firstBuild']
        lastbuild = jobinfo['lastBuild']
        if firstbuild:
            first = firstbuild.get('number')
        else:
            first = -1
        if lastbuild:
            last = lastbuild.get('number')
        else:
            last = -1
        return (first, last)


if __name__ == '__main__':
    pass