import sys
import subprocess
import pkg_resources
import pip
def check(required = {'plotly', 'pandas'}):
    def install(package):
        pip.main(['install', package])

    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    
    print(missing)
    
    for m in missing: 
        print("missing librarh[%s], installing now; restart terminal!")
        install(m)
