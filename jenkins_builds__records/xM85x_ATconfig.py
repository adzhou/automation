Jenkins_url = 'http://yyyy.xxxx.net:8080/jenkins/'
Jenkins_username = 'user'
Jenkins_password = 'pass'

# default csv name, no use.
Csv_buildInfo_name = 'buildinfo.csv'

# Don't modify build_keys_all. This is just to reference.
Build_keys_all = ['building', 'changeSet', 'builtOn', 'description', 'artifacts', 'timestamp', 'number',
                  'actions', 'id', 'keepLog', 'url', 'culprits', 'result', 'executor', 'duration',
                  'fullDisplayName', 'estimatedDuration']
# You can modify Build_keys_to_save as you like.
Build_keys_to_save = ['fullDisplayName', 'result', 'number', 'id', 'timestamp', 'url', 'duration',
                      'estimatedDuration']


# filter
Number_or_time = 'number' # time or number is ok.
# jobs to record
Jobs_to_record = {
                    'XM-85x-BAT': {'numberstartend':(242, 243), 'numberignore':[]},
                  }