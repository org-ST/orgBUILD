import sys

orgDir = "../"

java = True
cpp = True

def main():
    print("Welcome to orgBUILD")
    for i in sys.argv:
        if (sys.argv[i] == "-java"):
            print("Only build Java")
            cpp = False
            java = True
        elif (sys.argv[i] == "-cpp"):
            print("Only build orgST++")
            java = False
            cpp = True
        elif (sys.argv[i] == "--help"):
            print("Help page for orgBUILD")
            print("-java : Only build java")
            print("-cpp : Only build orgST++")
            print("-od <dir> : Set the directory orgST is in")
        elif (sys.argv[i] == "-od"):
            orgDir = sys.argv[i+1]
    if cpp:
        import configs
        configs.RunPP(orgDir)
if __name__ == "__main__":
    main()