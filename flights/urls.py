#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:33:20 2020

@author: sunnywang
"""

from django.urls import path

from . import views

urlpatterns=[
        path("",views.index,name="index"),
        path("<int:flight_id>",views.flight, name="flight"),
        path("<int:flight_id>/book",views.book, name="book")
        ]