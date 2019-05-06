def test_add_group(app):
    old_groups_list = app.group.get_groups_list()
    app.group.create('test_add_group')
    new_groups_list = app.group.get_groups_list()
    old_groups_list.append('test_add_group')
    assert sorted(old_groups_list) == sorted(new_groups_list)
