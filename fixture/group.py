class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_groups_list(self):
        self.open_group_editor()
        groups_tree = self.group_editor.window(auto_id='uxAddressTreeView')  # найти список элемент списка групп
        root = groups_tree.tree_root()  # найти корневой элемент
        groups_list = [node.text() for node in root.children()]  # получить список групп
        self.close_group_editor()
        return groups_list

    def create(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id='uxNewAddressButton').click()
        input_field = self.group_editor.window(class_name='Edit')
        input_field.set_text(name)
        input_field.type_keys('\n')

    def delete(self, group):
        self.open_group_editor()
        self.group_editor.window(class_name='%s' % group).click()
        self.group_editor.window(auto_id='uxDeleteAddressButton')
        self.group_editor.window(auto_id='uxDeleteAllRadioButton')
        self.group_editor.window(auto_id='uxOKAddressButton')
        self.close_group_editor()

        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id='groupButton').click()
        self.group_editor = self.app.application.window(title='Group editor')
        self.group_editor.wait('visible')

    def close_group_editor(self):
        self.group_editor.close()
