#!/usr/bin/env python3
from org_obs.env import *
import os
import shutil


class OrgObs:
    def __init__(self):
        self.obs_path = OBSIDIAN_FOLDER
        self.roam_path = ORG_ROAM_FOLDER
        self.tmp_path = PROJECT_PATH + '/tmp'
        if not os.path.exists(self.tmp_path):
            os.mkdir(self.tmp_path)

    def paths_not_null(self):
        obs_exists=self.obs_path != ''
        roam_exists=self.tmp_path != ''
        tmp_exists=self.roam_path != ''
        return obs_exists and roam_exists and tmp_exists

    def move_to_temp_path(self):
        destination = shutil.copytree(self.obs_path,self.tmp_path)
