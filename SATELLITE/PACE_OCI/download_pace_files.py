# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:41:01 2025

@author: haley.synan
"""

import earthaccess
auth = earthaccess.login(persist=True,strategy='interactive')
def get_pace(local_dir=r"Y:\PACE\V3.1\SOURCE\MAPPED_4KM_DAILY\RRS",tspan=("2024-04-01", "2025-09-15"), bbox=(-76.4, 34, -60, 46)):
    results = earthaccess.search_data(
    short_name="PACE_OCI_L3M_RRS",
    temporal=tspan,
    bounding_box=bbox,
    granule_name="*.DAY.*.4km.*",
    )
    print("Results gathered...downloading now")
    earthaccess.download(results,local_path=local_dir)
    print("Files downloaded!")
    
get_pace()