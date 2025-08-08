def err(msg :str, code=1):
    print("--ERROR--")
    print(msg)
    print(f"Program Exiting with Code: {code}")
    exit(code)