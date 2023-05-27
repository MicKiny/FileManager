import os
import string
import random
import psutil

    # this function using the psutil library detects all attached drives to the system
def detect_attached_drives():
        # creating a variable that lists the drives
    atch_drive = []
    for drive in psutil.disk_partitions():
            # describes the initial file path(mountpoint)
        if drive.mountpoint:
                # adds the mountpoint to the atch_drive list using the .append function for the user
            atch_drive.append(drive.mountpoint)
                # returns the list of drives available
    return atch_drive

drives = detect_attached_drives()
    # self explanitory, if no detectable drives there are no drives 
if not drives:
    print("No drives found.")
    exit()

print("Available drives:")
    # enumerate puts 'drives' into a list starting at 0
for i, drive in enumerate(drives):
    # {i+1} this takes the list of drives and for user convienence adds a value of 1 since lists begin at 0
    print(f"{i+1}. {drive}")

    # if there is no selected drive procede to the try statement
selected_drive = None
while True:
    try:
        choice = input("Enter corresponding number of desired drive: ")
        choice = int(choice)
        if choice < 1 or choice > len(drives):
            raise ValueError("Invalid selection, please enter appropriate value.")
        selected_drive = drives[choice - 1]

        print("Selected Drive:", selected_drive)
        
        confirm = input("Are you sure about your selected drive? (y/n): ")
        if confirm.lower() != 'y':
            selected_drive = None
            continue
        break
    except ValueError as e:
        print(str(e))

if selected_drive is None:
    print("Drive selection aborted.")
    exit()

    # the following code is to generate the random files to be written to the selected drive
file_form_list = [".txt", ".jpeg", ".jpg", ".mp4", ".mp3"]
NumF = 126
N = 14

for i in range(NumF):
# .join(random.choices) combines the ascii 26 letter alphabet and digits 0-9 to create a file name to the specified length of N
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    rand_fform = random.choice(file_form_list)
    filename = str(res) + str(rand_fform)
    ext_path = os.path.join(selected_drive, filename)
# opens ext_path as a writable file
    with open(ext_path, "w") as file:
        pass

print("Files created in:", selected_drive)
