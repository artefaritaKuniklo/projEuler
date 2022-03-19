# projEuler
刷题丢人现场

devcontainer.postbuild
```shell
# in host
cp -r ~/.ssh [PATH_TO_CLONE]/projectEuler
cp ~/.wakatime.cfg [PATH_TO_CLONE]/projectEuler

# in container
rm -rf ~/.ssh
mv .ssh ~/
mv .wakatime.cfg ~/
```