import os
from subprocess import run
import shared

class orgSTpp :
    orgDir = ""
    def __init__(self, orgdir):
        self.orgDir = orgdir
        print("Initializing orgST++")
        print(f"orgST Directory is: {self.orgDir}")
        print("Ensuring Libraries")
        if os.path.isdir({self.orgDir}+"/orgST++/third-party/cpp-httplib"):
            print("Detected cpp-httplib for orgST++")
        else:
            print("Couldn't find cpp-httplib which is required for orgST++")
            self.UpdateMods()
        if os.path.isdir({self.orgDir}+"/orgST++/third-party/CryptoPP"):
             print("Detected CryptoPP for orgST++")
        else:
             print("Couldn't find CryptoPP which is required for orgST++")
             self.UpdateMods()
        self.checkTools()
        self.RunCmake()
        return 0
    def UpdateMods(self):
        gethttplib = input("Would you like to ensure required libraries now? [Y/N]: ")
        if (gethttplib.lower == "y"):
                run(["git", "submodule", "update", "--init", "--recursive"], cwd={self.orgDir}, check=True)
        else:
             shared.err("User chose to not update, exiting")
    def RunCmake(self):
         run(["cmake", "-G", "Ninja", "-B", f"{self.orgDir}/orgST++/build", "-S", f"{self.orgDir}/orgST++"])
         run(["ninja", "-C", f"{self.orgDir}/orgST++/build"])
    def checkTools():
        cmakeres = run(["cmake", "--version"], capture_output=True, check=True)
        if cmakeres.returncode == 0:
             print("Found CMake")
        else:
             shared.err("CMake not found, please install CMake")
        ninjares = run(["ninja", "--version"], capture_output=True, check=True)
        if ninjares.returncode == 0:
             print("Found Ninja")
        else:
             shared.err("Ninja not found, please install Ninja")
                