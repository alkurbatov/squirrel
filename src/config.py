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

import sys, os.path
import re

class Unit(object):
    def __init__(self):
        #defaults
        self.delay = "0m"
        self.path = None
        self.dry_run = False

    def merge(self, opts):
        if opts.delay:
            self.delay = opts.delay

        if opts.path:
            self.path = opts.path

        if opts.dry_run:
            self.dry_run = opts.dry_run

def is_invalid(conf):
    if not conf.path:
        print >> sys.stderr, "The working directory was not specified", os.linesep
        return True

    if not os.path.isdir(conf.path):
        print >> sys.stderr, "The specified working directory does not exists", os.linesep
        return True

    if not re.search(r"(?i)[0-9][dhm]", conf.delay):
        print >> sys.stderr, "Invalid time format", os.linesep
        return True

    return False

def get(opts):
    c = Unit()
    c.merge(opts)

    if is_invalid(c):
        return None

    return c

