import pytest
from tmrrw import camel_case,coke_machine,just_setting_up_my_twttr


def test_camel_case():
    assert camel_case("sunny") == "sunny"
    assert camel_case("firstIdeaForEating") == "first_idea_for_eating"
    

def test_coke_machine():
    coins = [10,20,30,10,5]
    result = [40,20,20,10,5]
    for coin, change in zip(coins,result):
        assert coke_machine(coin) == change


def test_tmttr():
    assert just_setting_up_my_twttr("Tomorrow") == "Tmrrw"
    assert just_setting_up_my_twttr("I'll go to school tomorrow!") == "'ll g t schl tmrrw!"
    assert just_setting_up_my_twttr("CS50") == "CS50"



