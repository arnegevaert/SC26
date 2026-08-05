# Copy the demos folder to the parent directory
# because some of the demos use separate git repositories
# which would conflict with the main repo if run inside it
clean-demos:
  rm -rf ../demos
  cp -r demos ../
