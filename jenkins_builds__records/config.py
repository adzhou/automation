Jenkins_url = 'http://11.111.111.99:8000/'
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






