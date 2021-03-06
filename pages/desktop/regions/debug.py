#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import Page


class Debug(Page):

    _region_select_locator = (By.ID, 'region')

    def __init__(self, testsetup):
        Page.__init__(self, testsetup)
        self.wait_for_element_visible(*self._region_select_locator)

    def select_region(self, region):
        self.select_option(region, self._region_select_locator)
