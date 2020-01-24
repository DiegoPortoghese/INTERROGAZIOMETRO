#!/bin/sh
echo "Starting deploying in production server"
echo "cmd: git pull"
git pull
echo "copying configuration.."
echo "cmd: cp prod_config/nuxt.config.js site/nuxt.config.js"
cp prod_config/nuxt.config.js site/nuxt.config.js
echo "cmd: cp prod_config/settings.py main/main/settings.py"
cp prod_config/settings.py main/main/settings.py
echo "FINISH"
