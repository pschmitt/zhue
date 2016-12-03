#!/usr/bin/env bash

version=$(sed -nr "s/.*version='(.*)',/\1/p" setup.py)
echo "Release version $version"

echo -n "You sure? (y|n) "
read -r resp

case "$resp" in
    y|yes|Y¦YES)
        ;;
    *)
        exit 1
        ;;
esac

if git tag -l | grep "$version"
then
    echo "This version has already been released. Please edit setup.py"
    exit 2
fi

git add setup.py
git commit -m "version $version"
git tag -a "$version" -m "zhue $version"
git push --follow-tags
python setup.py sdist upload -r pypi
