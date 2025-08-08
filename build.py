import sys

orgDir = "../"

java = True
cpp = True
cmake_args_file = None

def main():
    global java, cpp, orgDir, cmake_args_file
    print("Welcome to orgBUILD")
    for i in range(len(sys.argv)):
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
        elif (sys.argv[i] == "-DCMAKE_ARGS_FILE"):
            cmake_args_file = sys.argv[i+1]
        elif (sys.argv[i] == "-clean"):
            import clean
            clean.clean(orgDir)
    if cpp:
        import configs
        if cmake_args_file != None:
            with open(cmake_args_file, 'r') as file:
                configs.RunPP(orgDir, file.read())
        else:
            configs.RunPP(orgDir, "")
    if java:
        import configs
        configs.RunJAVA(orgDir)
if __name__ == "__main__":
    main()