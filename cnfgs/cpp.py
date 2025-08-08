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
        buildres = self.RunCmake()
        return buildres
    def UpdateMods(self):
        gethttplib = input("Would you like to ensure required libraries now? [Y/N]: ")
        if (gethttplib.lower == "y"):
                run(["git", "submodule", "update", "--init", "--recursive"], cwd={self.orgDir}, check=True)
        else:
             shared.err("User chose to not update, exiting")
    def RunCmake(self):
         print("Building orgST++")
         cmakeres = run(["cmake", "-G", "Ninja", "-B", f"{self.orgDir}/orgST++/build", "-S", f"{self.orgDir}/orgST++"], capture_output=True, check=True)
         if (cmakeres.returncode != 0):
              print("Configuration via CMake failed")
              return 5
         ninjares = run(["ninja", "-C", f"{self.orgDir}/orgST++/build"], capture_output=True, check=True)
         if (ninjares.returncode != 0):
              print("Building via Ninja failed")
              return 5
         return 0
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
                