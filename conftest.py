import pytest
import yaml
from module import Site

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    

@pytest.fixture()
def select_input_login():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def select_input_password():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def select_input_button():
    return '''button'''


@pytest.fixture()
def select_error():
    return '''//*[@id="app"]/main/div/div/div[2]/h2'''


@pytest.fixture()
def select_hello_user():
    return '''//*[@id="app"]/main/nav/ul/li[3]/a'''


@pytest.fixture()
def select_input_create_new_post():
    return '''//*[@id="create-btn"]'''


@pytest.fixture()
def select_input_name_new_post():
    return '''//*[@id="create-item"]/div/div/div[1]/div/label/input'''


@pytest.fixture()
def select_input_button_new_post():
    return '''//*[@id="create-item"]/div/div/div[7]/div/button/span'''


@pytest.fixture()
def select_title_post():
    return '''//*[@id="app"]/main/div/div[1]/h1'''


@pytest.fixture()
def site():
    site_class = Site(testdata['address'])
    yield site_class
    site_class.close()