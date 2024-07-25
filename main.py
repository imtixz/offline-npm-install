import os
import json

toFind = input('npm install: ')
nodeModulesDir = input("look for packages in: ")
destination = input("store copies in: ")

def findDependency(packageName, requiredPackages):

    # Efficiency, return if package name already been explored
    if packageName in requiredPackages:
        return requiredPackages
    
    requiredPackages.append(packageName)

    # Read the file
    file = open(f"{nodeModulesDir}/{packageName}/package.json" ,"r")
    content = file.read()
    file.close()

    # Serialize it
    fileContent = json.loads(content)

    # Actual base case
    if 'dependencies' not in fileContent.keys():
        return requiredPackages

    # Recursive case
    deps = list(fileContent['dependencies'].keys())
    for dep in deps:
        findDependency(dep, requiredPackages)

    return requiredPackages

needToCopy = findDependency(toFind, [])


def copyModules(directory, requiredPackages):

    # create directory if it doesnt exist
    try:
        os.mkdir(directory)
    except Exception as e:
        print(e)

    # copy the node_modules into the new directory
    for pkg in requiredPackages:
        os.system(f"cp -r {nodeModulesDir}/{pkg} {directory}" )

print(needToCopy)
copyModules(destination, needToCopy)
    