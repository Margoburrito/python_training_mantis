# -*- coding: utf-8 -*-
import time
import random
from model.project import Project


def test_del_project(app):
    if len(app.projecthelper.get_project_list()) == 0:
        app.projecthelper.create_project(Project(name="name" + str(round(time.time() * 1000))))

    old_projects = app.projecthelper.get_project_list()
    index = random.randrange(len(old_projects))
    app.projecthelper.delete_by_index(index)
    new_projects = app.projecthelper.get_project_list()

    assert len(old_projects) - 1 == len(new_projects)
    old_projects[index:index + 1] = []
    assert old_projects == new_projects
    assert sorted(old_projects, key=Project.id_or_max) == \
           sorted(app.projecthelper.get_project_list(), key=Project.id_or_max)
