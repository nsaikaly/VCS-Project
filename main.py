import sys, os

if __name__ == "__main__":
    commands_allowed = set(["create_repo", "check_in", "check_out"])
    if len(sys.argv) == 1 or 2 < len(sys.argv):
        print "Only 1 argument allowed after calling main.py"
    else:
        sys.path.insert(0, os.getcwd() + "/VCS")
        argument = sys.argv[1]
        if argument not in commands_allowed:
            print "The command " + argument + " is not allowed."
            print "Allowed arguments are: " + commands_allowed
        else:
            execfile("VCS/" + argument + ".py")