from github import Github
from env import GITHUB_TOKEN, DEFAULT_ORG
import issues
from nose.tools import *


#def test_credential_exception():
#    gt = Github('badcreds')
#    assert_raises(Exception, gt.get_organization, DEFAULT_ORG)

def test_gh_init_exception():
    gt = Github('badcreds')
    assert_raises(Exception, issues.gh_init, gt) 

def test_filter_exceptions():
    gt = Github(GITHUB_TOKEN)
    assert_raises(Exception, issues.get_issues, 'fake_issue', gt)


def test_assigned_issues():
    pass


def test_mentioned_issues():
    pass


def test_created_issues():
    pass


def test_subscribed_issues():
    pass
