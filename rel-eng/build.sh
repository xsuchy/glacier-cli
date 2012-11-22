#!/bin/bash
set -e 
set -o pipefail
git merge -m "Merge remote-tracking branch 'glacier-cli/master' by rel-eng/build.sh" glacier-cli/master
#just test if we are able to create srpm, and do not proceed if there is big change in code
tito build --test --srpm

HASH=$(git show glacier-cli/master  |grep commit |head -n1 | awk '{print $2}' |cut -c-7)
sed -i "s/%global glacier_hash .*$/%global glacier_hash .$HASH/" glacier-cli.spec
git add glacier-cli.spec
git commit -m 'Automatic rebase to latest nightly glacier-cli'
tito tag --accept-auto-changelog
git push && git push --tags
tito release koji
