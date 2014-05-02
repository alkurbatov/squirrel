# This file is a part of Squirrel project
#
# Copyright (C) 2014, Alexander Kurbatov <sir.alkurbatov@yandex.ru>
#
# Squirrel is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Squirrel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import ConfigParser
import sys, os.path
import re

class Unit(object):
    def __init__(self):
        self.delay = "0m"
        self.path = []
        self.keep = False

    def parse(self, src):
        c = ConfigParser.RawConfigParser()
        if not c.read(src):
            return

        if c.has_option("General", "period"):
            self.delay = c.get("General", "period")

        if c.has_option("General", "workDir"):
            self.path = c.get("General", "workDir").split(";")

    def merge(self, opts):
        if opts.delay:
            self.delay = opts.delay

        if opts.path:
            self.path = opts.path.split(";")

        if opts.keep:
            self.keep = opts.keep

    def is_invalid(self):
        if not self.path:
            print >> sys.stderr, "The working directory was not specified", os.linesep
            return True

        for p in self.path:
            if os.path.isdir(p):
                continue

            print >> sys.stderr, "The working directory does not exists - %s" %p, os.linesep
            return True

        if not re.search(r"(?i)[0-9][dhm]", self.delay):
            print >> sys.stderr, "Invalid time format", os.linesep
            return True

        return False

