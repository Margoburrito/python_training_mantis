# -*- coding: utf-8 -*-
import time
from model.project import Project


def test_add_new_project(app):
    project_name = Project(name="name" + str(round(time.time() * 1000)))
    old_projects = app.projecthelper.get_project_list()
    app.projecthelper.create_project(project_name)
    new_projects = app.projecthelper.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project_name)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
