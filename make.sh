#! /bin/bash
# helper bash

pyuic4 bms_ui.ui > bms_ui_form.py

git add bms_interface.py bms_ui.ui bms_ui_form.py ui_helper.py
git commit -m "Uploading to github for file transfer. WIP."
git push
echo Done
