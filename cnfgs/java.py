import os
from subprocess import run
import shared
import sys

class orgSTJava:
    orgDir = ""
    def __init__(self, orgDir):
        print("Initialzing orgST Java")
        self.orgDir = orgDir
        if self.chkjava() != 21: shared.err("orgST Java required Java 21 or Later")
        if self.chkmvn() == 0: print("Found Maven")
        if self.Build() == 0: return None
    def chkjava(self):
        result = run(['java', '--version'],
                                capture_output=True, text=True)

        output = result.stdout.strip().splitlines()

        first_line = output[0]

        for part in first_line.split():
            if part[0].isdigit():
                major_version = part.split('.')[0]
                print("Major Java version:", major_version)
                return int(major_version)
    def chkmvn(self):
        if run(["mvn", "--version"], check=True, stdout=sys.stdout, stderr=sys.stderr).returncode != 0:
            shared.err("Failed to locate Maven, please install Maven")
        else:
            return 0
    def Build(self):
        currdir = os.path.curdir
        os.chdir(self.orgDir)
        if run(["mvn", "package"], check=True, stdout=sys.stdout, stderr=sys.stderr).returncode != 0:
            os.chdir(currdir)
            shared.err("Failed to build orgST Java")
        else:
            os.chdir(currdir)
            return 0
