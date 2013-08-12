from sample_data_utils.people import GENDER_MALE, first_name, person, gender, GENDER_FEMALE, fullname, name, title


def test_first_name():
    assert first_name(languages=('en',), genders=(GENDER_MALE,))


def test_gender():
    assert gender() in (GENDER_MALE, GENDER_FEMALE)


def test_person():
    assert person(['en'])[3] in (GENDER_MALE, GENDER_FEMALE)


def test_name():
    assert name()


def test_fullname():
    assert fullname()


def test_title():
    assert title()
    assert title(['en'])
    assert title(['it'], ['m', 'f'])
