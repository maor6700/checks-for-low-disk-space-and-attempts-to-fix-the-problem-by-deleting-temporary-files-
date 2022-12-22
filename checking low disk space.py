import os
import shutil
import psutil

# Get the total and free disk space
total, used, free = shutil.disk_usage('/')

# Calculate the used space in percentage
used_percent = used / total * 100

# Check if the used space is above a certain threshold
if used_percent > 90:
    print('Low disk space detected!')
    # Get a list of temporary files
    temp_files = [f for f in os.listdir('/tmp') if f.startswith('tmp')]
    # Delete the temporary files
    for f in temp_files:
        os.remove(os.path.join('/tmp', f))
    print('Temporary files deleted')
else:
    print('Disk space is sufficient')
