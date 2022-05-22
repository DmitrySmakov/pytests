import pytest
from functions import get_shelf1 ,get_people1 ,add_document1 , del_document1
from yadisk  import YaDisk

fixtures = [('2207 876234','1'), ("10006",'2')]

class TestFunctions:
    def setUp(self) -> None:
        print("setUp --> work")

    def tearDown(self) -> None:
        print("tearDown --> work")

    def test_get_people1(self):
        assert get_people1('2207 876234') == 'Василий Гупкин'

    @pytest.mark.parametrize("a,result",fixtures )
    def test_get_shelf1(self, a , result):
        assert get_shelf1(a) == result
#
@pytest.mark.parametrize("a,result",fixtures )
def test_get_shelf2(a , result):
    assert get_shelf1(a) == result

def test_get_people2():
    assert get_people1('2207 876234') == 'Василий Гупкин'

def test_add_document1():
    documents = []
    directories = {'2': []}
    add_document1("passport", "2207 876234", "Василий Гупкин", '2', documents , directories)
    assert documents == [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}]
    assert directories == {'2': ["2207 876234"] }

def test_del_document1():
    documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}]
    directories = {'1': ['2207 876234', '11-2', '5455 028765']}
    del_document1("2207 876234", documents, directories)
    assert documents == []
    assert directories == {'1': ['11-2', '5455 028765']}

# !!! token_ya.txt скопировал в пакет tests
ya = YaDisk('token_ya.txt')

def test_ya_disk_new_folder():
    filename = 'ya_test'
    assert ya.new_folder(filename).status_code == 201
    assert ya.ckeck_file(filename).status_code == 200

def test_ya_disk_exist_folder():
    filename = 'ya_test'
    assert ya.new_folder(filename).status_code == 409
    assert ya.ckeck_file(filename).status_code == 200