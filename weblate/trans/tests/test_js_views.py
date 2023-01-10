#
# Copyright © Michal Čihař <michal@weblate.org>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""Test for AJAX/JS views."""

from django.urls import reverse

from weblate.trans.tests.test_views import FixtureTestCase


class JSViewsTest(FixtureTestCase):
    """Testing of AJAX/JS views."""

    def test_get_unit_translations(self):
        unit = self.get_unit()
        response = self.client.get(
            reverse("js-unit-translations", kwargs={"unit_id": unit.id})
        )
        self.assertContains(response, 'href="/translate/')
