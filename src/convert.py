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

import re

def to_seconds(time):
    s = 0

    d = re.search(r"(?i)([0-9]+)d", time)
    if d:
        s += int(d.group(1)) * 24 * 60 * 60

    h = re.search(r"(?i)([0-9]+)h", time)
    if h:
        s += int(h.group(1)) * 60 * 60

    m = re.search(r"(?i)([0-9]+)m", time)
    if m:
        s += int(m.group(1)) * 60

    return s

