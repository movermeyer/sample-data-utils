from sample_data_utils.geo import country, iso2, iso3, lang, isonum, CONTINENTS, continent, countries


def test_continent():
    assert continent() in CONTINENTS


def test_country():
    print 1111, countries
    print next(countries)
    print next(countries)
    print next(countries)

    # assert len(c) == 8
    # assert len(c[0]) == 2  # iso2
    # assert len(c[1]) == 3  # iso3
    # assert len(c[2]) == 3  # iso_num
    # assert c[4] in [i[0] for i in CONTINENTS]  # Continent
    # assert len(c[5]) == 3  # tld
    # assert len(c[6]) == 3  # CurrencyCode


def test_iso2():
    u = iso2()
    assert len(u) == 2
    assert u == u.upper()


def test_iso3():
    u = iso3()
    assert len(u) == 3
    assert u == u.upper()


def test_isonum():
    u = isonum()
    assert len(u) == 3
    assert int(u)


def test_lang():
    assert len(lang()) == 3
