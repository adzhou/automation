from __future__ import print_function
import time
from jenkins_record_status import GetBuildsInfoFromJenkins
import SM95xBATconfig as SMconfig
import resultToCSV


def main():
    time_now = time.strftime("20%y-%m-%d_%H-%M-%S")
    gbi = GetBuildsInfoFromJenkins()
    jobs = gbi.get_all_jobs()
    for job in jobs:
        print (job['fullname'])
    for jobname in SMconfig.Jobs_to_record.keys():
        csvfilename = jobname + '--' + time_now + '.csv'
        rtc = resultToCSV.ToCSV(csvfilename)
        if SMconfig.Number_or_time == 'number':
            numberse = SMconfig.Jobs_to_record[jobname]['numberstartend']
            numberig = SMconfig.Jobs_to_record[jobname]['numberignore']
            for buildnumber in range(numberse[0], numberse[1]+1):
                if buildnumber in numberig:
                    continue
                row = gbi.get_build_info_row_need(jobname, buildnumber)
                if row:
                    print(row)
                    rtc.addrow(row)
        elif SMconfig.Number_or_time == 'time':
            # TODO
            pass

def test():
    time_now = time.strftime("20%y-%m-%d_%H-%M-%S")
    gbi = GetBuildsInfoFromJenkins(url=SMconfig.Jenkins_url, username=SMconfig.Jenkins_username,
                                   password=SMconfig.Jenkins_password)
    # alljobs = gbi.get_all_jobs()
    # for job in alljobs:
    #     print (job)
    for jobname in SMconfig.Jobs_to_record.keys():
        print(jobname)
        jobinfo = gbi.get_server().get_job_info(jobname)
        print (jobinfo)
        for key in jobinfo.keys():
            print(key, jobinfo[key])
        if SMconfig.Number_or_time == 'number':
            numberse = SMconfig.Jobs_to_record[jobname]['numberstartend']
            numberig = SMconfig.Jobs_to_record[jobname]['numberignore']
            for buildnumber in range(numberse[0], numberse[1] + 1):
                if buildnumber in numberig:
                    continue
                # row = gbi.get_build_info_row_need_info_row_need(jobname, buildnumber)
                row = gbi.get_build_info(jobname, buildnumber)
                if row:
                    print(row)




if __name__ == '__main__':
    main()
    # test()