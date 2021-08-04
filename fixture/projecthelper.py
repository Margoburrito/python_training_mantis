from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("my_view_page.php"):
            wd.find_element_by_link_text("My View").click()

    def open_manage_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            wd.get(self.app.base_url + "/manage_proj_page.php")

    def open_start_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def accept_alert(self):
        wd = self.app.wd
        wd.switch_to_alert().accept()

    def create_project(self, project_name):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_data(project_name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_manage_projects_page()
        self.project_cache = None

    def fill_data(self, project_name):
        self.change_name(project_name.name)

    def change_name(self, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name("name").click()
            wd.find_element_by_name("name").clear()
            wd.find_element_by_name("name").send_keys(text)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.select_project_by_index(index)
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()
        self.open_manage_projects_page()
        self.project_cache = None

    def select_project_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath(
            "//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]//a")[index].click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_projects_page()
            self.project_cache = []

            for row in wd.find_elements_by_xpath(
                    "//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]/."):
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].find_element_by_tag_name("a").text
                id = cells[0].find_element_by_tag_name("a").get_attribute("href").split("=", 1)[1]
                self.project_cache.append(Project(name=name, id=id))
        return list(self.project_cache)