def RunPP(orgDir):
    import cnfgs.cpp
    orgstpp = cnfgs.cpp.orgSTpp(orgDir)
    if orgstpp == 0:
        print("Succesfully Setup orgST++")
    