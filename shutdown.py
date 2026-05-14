def shut_down(check):
    check=input("did you close all apps(yes/no):")
    if check=="yes":
        return("shutting down")

    elif check=="no":
        return("aborting shutdown")

    else:
        return("sorry")

   