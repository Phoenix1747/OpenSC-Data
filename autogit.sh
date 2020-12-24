#!/bin/bash

gitpath="$(dirname $(realpath $0))"

git -C $gitpath pull
git -C $gitpath add "$gitpath/docs" "$gitpath/data/*.csv"
git -C $gitpath commit -m "auto data update"
git -C $gitpath push
