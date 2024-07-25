Python script that goes through an existing node_modules to find an npm package and all its dependencies. Useful for sitautions when you want to build something using nodejs but don't have internet access. It only uses the built-in modules of python and thus has no dependency.

Run the main.py script, it will ask for inputs. You will have to provide the name of the npm package you want to install, path of the node_modules folder where its stored and the path of the folder where you want to copy all the npm packages (the one you want to install and its dependencies).

Notes:

1. this script does not modify any package.json like npm install does.
2. this will work only on unix-based system (macos and linux) as it uses the cp command line tool to copy and I dont think works in windows.
