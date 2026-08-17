clean-demos:
  rm -rf demo
  cp -r demo_templates demo
  docker container ls -aq | xargs --no-run-if-empty docker container rm -f
  docker image ls -aq | xargs --no-run-if-empty docker image rm -f
