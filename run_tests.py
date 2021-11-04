#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import unittest
from tests.movies.click_on_movie_test import ClickOnMovieTest
from tests.movies.click_on_genre_test import ClickOnGenreTest as ClickOnMovieGenreTest
from tests.series.click_on_genre_test import ClickOnGenreTest
from tests.series.click_on_series_test import ClickOnSeriesTest
from tests.login.login_test import LoginTest
from tests.navbar.logout_test import LogoutTest
from tests.navbar.go_to_profile_test import GoToProfileTest
from tests.navbar.go_to_favourites_test import GoToFavouritesTest
from tests.details.tests_without_auth.transit_to_auth_page_test import TransitToAuthTest
from tests.details.tests_without_auth.click_on_actor_name_test import ClickOnActorNameTest
from tests.details.tests_with_auth.transit_to_profile_page_test import TransitToProfileTest
from tests.details.tests_with_auth.details_buttons_tests import OpenPlayerTest, AddToFavouritesTest,\
    RemoveFromFavouritesTest, LikeMovieTest, DislikeMovieTest
from tests.profile.click_on_sub_btn import ClickOnSubscriptionBtnTest
from tests.profile.change_to_invalid_avatar_test import ChangeToInvalidAvatarTest
from tests.profile.correct_update_profile_tests import ChangeToValidAvatarTest, ChangeToValidEmailTest, \
    ChangeToValidLoginTest, ChangeToValidLoginAndEmailTest
from tests.profile.error_update_profile_tests import ChangeToInvalidLoginTest, ChangeToEmptyLoginTest, \
    ChangeToInvalidEmailTest, ChangeToEmptyEmailTest, ChangeToInvalidEmailAndLoginTest, \
    ChangeToInvalidLoginAndValidEmailTest
from tests.signup.transit_to_login_page_test import TransitToLoginPageTest
from tests.signup.signup_with_errors_test import SignUpWithEmptyFieldsTest, SignUpWithInvalidLoginTest, \
    SignUpWithNumericLoginTest, SignUpWithInvalidEmailTest, SignUpWithSmallPasswordTest, SignUpWithLetterLoginTest, \
    SignUpWithBigPasswordTest, SignUpWithDifferentPasswordsTest, SignUpWithAllInvalidFieldsTest, \
    SignUpAlreadySignupedTest
from tests.signup.signup_test import SignUpTest
from tests.search_popup.close_popup_test import ClosePopupTest
from tests.search_popup.enter_letter_test import EnterLetterTest
from tests.search_popup.find_movie_test import FindMovieTest
from tests.search_popup.find_actor_test import FindActorTest
from tests.player.closed_test import ClosedTest
from tests.player.not_opened_test import NotOpenedTest
from tests.player.esc_to_part_screen_test import EscToPartScreenTest
from tests.player.close_fullscreen_test import CloseFullscreenTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(ClickOnSeriesTest),
        # unittest.makeSuite(ClickOnGenreTest),
        # unittest.makeSuite(ClickOnMovieTest),
        # unittest.makeSuite(ClickOnMovieGenreTest),
        # unittest.makeSuite(LoginTest),
        unittest.makeSuite(LogoutTest),
        # unittest.makeSuite(GoToProfileTest),
        # unittest.makeSuite(GoToFavouritesTest),
        # unittest.makeSuite(TransitToAuthTest),
        # unittest.makeSuite(ClickOnActorNameTest),
        # unittest.makeSuite(TransitToProfileTest),
        # unittest.makeSuite(OpenPlayerTest),
        # unittest.makeSuite(AddToFavouritesTest),
        # unittest.makeSuite(RemoveFromFavouritesTest),
        # unittest.makeSuite(LikeMovieTest),
        # unittest.makeSuite(DislikeMovieTest),
        # unittest.makeSuite(ClickOnSubscriptionBtnTest),
        # unittest.makeSuite(ChangeToInvalidAvatarTest),
        # unittest.makeSuite(ChangeToValidAvatarTest),
        # unittest.makeSuite(ChangeToValidEmailTest),
        # unittest.makeSuite(ChangeToValidLoginTest),
        # unittest.makeSuite(ChangeToValidLoginAndEmailTest),
        # unittest.makeSuite(ChangeToInvalidLoginTest),
        # unittest.makeSuite(ChangeToEmptyLoginTest),
        # unittest.makeSuite(ChangeToEmptyEmailTest),
        # unittest.makeSuite(ChangeToInvalidEmailTest),
        # unittest.makeSuite(ChangeToInvalidEmailAndLoginTest),
        # unittest.makeSuite(ChangeToInvalidLoginAndValidEmailTest),
        # unittest.makeSuite(TransitToLoginPageTest),
        # unittest.makeSuite(SignUpWithEmptyFieldsTest),
        # unittest.makeSuite(SignUpWithInvalidLoginTest),
        # unittest.makeSuite(SignUpWithNumericLoginTest),
        # unittest.makeSuite(SignUpWithInvalidEmailTest),
        # unittest.makeSuite(SignUpWithLetterLoginTest),
        # unittest.makeSuite(SignUpWithSmallPasswordTest),
        # unittest.makeSuite(SignUpWithBigPasswordTest),
        # unittest.makeSuite(SignUpWithDifferentPasswordsTest),
        # unittest.makeSuite(SignUpWithAllInvalidFieldsTest),
        # unittest.makeSuite(SignUpAlreadySignupedTest),
        # unittest.makeSuite(SignUpTest),
        # unittest.makeSuite(ClosePopupTest),
        # unittest.makeSuite(EnterLetterTest),
        # unittest.makeSuite(FindMovieTest),
        # unittest.makeSuite(FindActorTest),
        # unittest.makeSuite(ClosedTest),
        # unittest.makeSuite(NotOpenedTest),
        # unittest.makeSuite(EscToPartScreenTest),
        # unittest.makeSuite(CloseFullscreenTest)
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
