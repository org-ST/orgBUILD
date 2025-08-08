import os
import shutil
from subprocess import run
def clean(orgDir):
    curr = os.path.curdir
    os.chdir(orgDir)
    run(["mvn", "clean"], check=True)
    os.chdir("orgST++")
    shutil.rmtree("build")