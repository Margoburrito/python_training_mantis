
from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_all_accessible_projects(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects_list = []

        for row in client.service.mc_projects_get_user_accessible(username, password):
            projects_list.append(Project(name=row.name, id=row.id))

        return projects_list

    def get_all_admin_projects(self):
        return self.get_all_accessible_projects("administrator", "root")