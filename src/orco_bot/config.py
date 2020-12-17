# Copyright (c) ACSONE SA/NV 2018
# Distributed under the MIT License (http://opensource.org/licenses/MIT).

import logging
import os
from functools import wraps

_logger = logging.getLogger("oca_gihub_bot.tasks")


def switchable(switch_name=None):
    def wrap(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            sname = switch_name
            if switch_name is None:
                sname = func.__name__

            if BOT_TASKS != ["all"] and sname not in BOT_TASKS:
                _logger.debug("Method %s skipped (Disabled by config)", sname)
                return
            return func(*args, **kwargs)

        return func_wrapper

    return wrap


HTTP_HOST = os.environ.get("HTTP_HOST")
HTTP_PORT = int(os.environ.get("HTTP_PORT") or "8080")

GITHUB_SECRET = os.environ.get("GITHUB_SECRET")
GITHUB_LOGIN = os.environ.get("GITHUB_LOGIN")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_ORG = os.environ.get("GITHUB_ORG")
GIT_NAME = os.environ.get("GIT_NAME")
GIT_EMAIL = os.environ.get("GIT_EMAIL")

ODOO_URL = os.environ.get("ODOO_URL")
ODOO_DB = os.environ.get("ODOO_DB")
ODOO_LOGIN = os.environ.get("ODOO_LOGIN")
ODOO_PASSWORD = os.environ.get("ODOO_PASSWORD")

BROKER_URI = os.environ.get("BROKER_URI", os.environ.get("REDIS_URI", "redis://queue"))

SENTRY_DSN = os.environ.get("SENTRY_DSN")

DRY_RUN = os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes")

# Coma separated list of task to run
# By default all configured tasks are run.
# Available tasks:
#  delete_branch,tag_approved,tag_ready_to_merge,gen_addons_table,
#  gen_addons_readme,gen_addons_icon,setuptools_odoo,merge_bot,tag_needs_review
BOT_TASKS = os.environ.get("BOT_TASKS", "all").split(",")

GITHUB_STATUS_IGNORED = [
    "ci/runbot",
    "codecov/project",
    "codecov/patch",
    "coverage/coveralls",
]
GITHUB_CHECK_SUITES_IGNORED = ["Codecov"]
MERGE_BOT_INTRO_MESSAGES = [
    "On my way to merge this fuckin PR, bitch!",
    "Let's merge this awesome bunch of brand new bugs!",
    "Ok, let's make yet another prod instance explode. Merging now.",
    "What a great day to merge new bugs. Let's do it!",
    "It was time you started writing some barely decent code, for Christ' sake. Merging it.",
    "Considering how you review code, not sure I can merge it. Let's try.",
    "Do you call this shit 'code'? Bah, let's merge and forget about it",
    "Better out than in, I always say! Merging now.",
    "What a disgusting pile of shit. Merging just because they force me to.",
    "Can't you merge it on your own? That's the 'abc'!",
    "Don't take it out on me when this crap goes prod. Merging now.",
    "What, seriously? Do you really want me to touch this shit? Bah, let's see what I can do",
    "Let's merge this stinking pile of crappy code",
    "Even my wife, Princess Fiona, could code better than you did. Bah, let's merge it anyway",
    "You talkin' to me? You talkin' to me? Then who the hell else are you talkin' to?",
    "SSSSSSSSSSSSSSSSMOKIN'!",
    "Well, let's not start sucking each other's dicks quite yet. Let's merge this stuff and call it a day, ok?",
    "Winter is coming. And a lot of bugs too. Merging now",
    "Merging now. That's thirty minutes away. I'll be there in ten.",
    "Wanna merge? Frankly, my dear, I don't give a damn.",
    "Asking Github to merge it. I'm going to make him an offer he can't refuse.",
    "May the Source be with you!",
    "I love the smell of bugs in the morning",
    "My name is Bot. Orco Bot. Merging your stuff.",
    "Talk is cheap, show me the code!",
    "You know how to merge, don't you Steve? You just put your branches together and blow.",
    "I'll be back.",
    "Code is like a box a chocolate. You never know what bug you're gonna get.",
    "Houston, we have a problem. This code sucks.",
    "HERE'S JOHNNY!",
    "A merge please. Shaken, not stirred.",
    "I'll do it. Sicchè!",
    "Is this a PR? Freechete!!!",
]

SIMPLE_INDEX_ROOT = os.environ.get("SIMPLE_INDEX_ROOT")
