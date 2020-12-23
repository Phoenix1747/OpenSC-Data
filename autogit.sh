#!/bin/bash

gitpath="$(dirname $(realpath $0))"

git -C $gitpath pull
git -C $gitpath add "$gitpath/docs" "$gitpath/data"
git -C $gitpath commit -m "update data"
git -C $gitpath push
