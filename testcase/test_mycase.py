# import pytest
# @pytest.fixture()
# def my_fixtures():
#    print("用户模块")
#    yield
#    print("退出")
# @pytest.mark.usefixtures("my_fixtures")
# def test_first():
#    print("我的1")
   #assert 1 == 2
# @pytest.mark.usefixtures("my_fixtures")
# def test_second():
#     print("我的2")
    #assert 2 == 2
# @pytest.mark.bug
# @pytest.mark.usefixtures("my_fixtures")
# def test_three():
#    print("我的3")
   #assert 'b' in 'ab'
# @pytest.mark.usefixtures("my_fixtures")
# def test_four():
#    print("我的4")
#    b={1,2,3}
   #assert 3 in b