from __future__ import print_function
import time
from jenkins_record_status import GetBuildsInfoFromJenkins
import recordBuildInfoConfig as BIconfig
import resultToCSV
# import csv


def main():
    time_now = time.strftime("20%y-%m-%d_%H-%M-%S")
    gbi = GetBuildsInfoFromJenkins()
    jobs = gbi.get_all_jobs()
    for job in jobs:
        print (job['fullname'])
    for jobname in BIconfig.Jobs_to_record.keys():
        csvfilename = jobname + '--' + time_now + '.csv'
        rtc = resultToCSV.ToCSV(csvfilename)
        if BIconfig.Number_or_time == 'number':
            numberse = BIconfig.Jobs_to_record[jobname]['numberstartend']
            numberig = BIconfig.Jobs_to_record[jobname]['numberignore']
            for buildnumber in range(numberse[0], numberse[1]+1):
                if buildnumber in numberig:
                    continue
                row = gbi.get_build_info_row_need(jobname, buildnumber)
                if row:
                    print(row)
                    rtc.addrow(row)
        elif BIconfig.Number_or_time == 'time':
            # TODO
            pass


def test():
    binfo = GetBuildsInfoFromJenkins()
    jobs = binfo.get_all_jobs()
    print (jobs)
    for jobname in BIconfig.Jobs_to_record.keys():
        # jobname = 'test_project_1'
        # viewname = 'test_view_1'
        # buildnumber = 4
        numberse = BIconfig.Jobs_to_record[jobname]['numberstartend']
        for buildnumber in range(numberse[0], numberse[1]):
            row = binfo.get_build_info_row_need(jobname, buildnumber)
            print(row)
        # server = binfo.get_server()
        jobinfo = binfo.get_job_info_by_name(jobname)
        print (jobinfo)
        for key in jobinfo.keys():
            print (key)
        # bse = binfo.get_all_builds_number_by_jobname(jobname)
        # print (bse)
        # buildinfo = binfo.get_build_info(jobname, buildnumber)
        # print (buildinfo)
        # print (buildinfo.keys())
        # for key in buildinfo.keys():
        #     print (key)
        # print(buildinfo['fullDisplayName'], buildinfo['result'], buildinfo['id'])
        # jobs = binfo.get_jobs_by_view(viewname)
        # print(binfo.get_all_views())
        # print (jobs)
        # aa = server.get_view_name(viewname)
        # print (aa)
        # bb = server.get_view_config(viewname)
        # print (bb)


if __name__ == '__main__':
    main()
    # test()
    # print (BIconfig.Build_keys_all)