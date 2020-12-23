#!/bin/bash

gitpath="$(dirname $(realpath $0))"
git -C $gitpath add "$gitpath/*"
git -C $gitpath commit -m "update data"
git -C $gitpath push
