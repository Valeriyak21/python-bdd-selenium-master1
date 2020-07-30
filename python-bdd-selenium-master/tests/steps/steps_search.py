from behave import *
from hamcrest import *

use_step_matcher("re")


@then("I see repositories associated with this user")
def see_repositories(context):
    repo_count = len(context.search_page.get_repositories())
    print("Find {} repos".format(repo_count))
    assert_that(repo_count, is_(greater_than_or_equal_to(2)))
