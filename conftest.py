import pytest
from fixture.application import Application
from comtypes.client import CreateObject
import os.path


@pytest.fixture(scope='session')
def app(request):
    fixture = Application('D:\\AddressBookPortable\\AddressBook.exe')
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:  # тестовые данные
        if fixture.startswith('data_'):
            xl = CreateObject("Excel.Application")
            wb = xl.Workbooks.Open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/%s.xlsx' % fixture[5:]))
            worksheet = wb.Sheets[1]
            data_list = []
            for row in range(1, 11):
                data = worksheet.Cells[row, 1].Value()
                data_list.append(data)
            xl.Quit()
            metafunc.parametrize(fixture, data_list, ids=[str(x) for x in data_list])
