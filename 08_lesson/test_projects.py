from ProjectApi import ProjectApi
import pytest

api = ProjectApi("https://ru.yougile.com/api-v2")

def test_create_project():
    api.get_company_id()
    api.get_token()
    project_ID = api.create_project()
    assert project_ID

def test_create_project_negative():
    api.get_company_id()
    api.get_token()
    neg_project_ID = api.create_project_negative()
    assert neg_project_ID

def test_update_project():
    api.get_company_id()
    api.get_token()
    new_project_ID = api.update_project()
    assert new_project_ID

def test_update_project_negative():
    api.get_company_id()
    api.get_token()
    project_ID_neg = api.update_project_negative()
    assert project_ID_neg

def test_get_by_ID():
    api.get_company_id()
    api.get_token()
    project = api.get_project_by_ID()

    assert project['title'] == 'Project_Test123'
    assert project['deleted'] is False

def test_get_by_ID_negative():
    api.get_company_id()
    api.get_token()
    project_neg = api.get_project_by_ID_negative()
    assert project_neg.status_code == 400