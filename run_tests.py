#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import unittest
from tests.movies.click_on_movie_test import ClickOnMovieTest
from tests.movies.click_on_genre_test import ClickOnGenreTest as ClickOnMovieGenreTest
from tests.series.click_on_genre_test import ClickOnGenreTest
from tests.series.click_on_series_test import ClickOnSeriesTest
from tests.auth.login_test import AuthTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(ClickOnSeriesTest),
        # unittest.makeSuite(ClickOnGenreTest),
        # unittest.makeSuite(ClickOnMovieTest),
        # unittest.makeSuite(ClickOnMovieGenreTest)
        unittest.makeSuite(AuthTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
