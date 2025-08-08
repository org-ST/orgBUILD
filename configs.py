def RunPP(orgDir):
    import cnfgs.cpp
    orgstpp = cnfgs.cpp.orgSTpp(orgDir)
    if orgstpp == 0:
        print("Succesfully Built orgST++")
    else:
        print("Building orgST++ Failed")
        contin = input("Would you like to continue? [Y/N]: ")
        if (contin.lower != "y"):
            import shared
            shared.err("User Aborted")
def RunJAVA(orgDir):
    import cnfgs.java
    if cnfgs.java.orgSTJava(orgDir) == 0:
        print("Succesfully Built orgST Java")
    else:
        print("Building orgST Java Failed")
        contin = input("Would you like to continue? [Y/N]: ")
        if (contin.lower != "y"):
            import shared
            shared.err("User Aborted")
    
    