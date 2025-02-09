import os

# Access an environment variable directly
where_am_i = os.environ['WHICH_ENV']

print(where_am_i.replace("_",""))

