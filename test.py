import subprocess

result = subprocess.run(['java', '--version'],
                        capture_output=True, text=True)

output = result.stdout.strip().splitlines()

first_line = output[0]

for part in first_line.split():
    if part[0].isdigit():
        major_version = part.split('.')[0]
        print("Major Java version:", major_version)
        break