class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

#releases the variables
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

print(bcolors.HEADER +  "HEADER" + bcolors.ENDC)
print(bcolors.OKBLUE +  "INSTRUCTIONS" + bcolors.ENDC)
print(bcolors.OKGREEN +  "NORMAL TEXT" + bcolors.ENDC)
print(bcolors.WARNING + "WARNING" + bcolors.ENDC)
print(bcolors.FAIL +  "ERROR" + bcolors.ENDC)

bcolors.disable(bcolors)

print("DONE!!")
