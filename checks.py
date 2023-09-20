import shutil
import psutil
disk = shutil.disk_usage("/")
freeDiskSpace =int(disk.free/disk.total*100)
cpuUsage = psutil.cpu_percent(1)

if (freeDiskSpace>20 and cpuUsage<75):
    print("There is ", freeDiskSpace, " percent free space left and it is good")
    print("The cpu usage is ", cpuUsage, "percent and it is good")
    print("Everything is OK!!")

else:
    print("There is ", freeDiskSpace, " percent free space left.")
    print("The cpu usage is ", cpuUsage, "percent.")
    print("Something is fishy run disk cleanup and disable background apps")

