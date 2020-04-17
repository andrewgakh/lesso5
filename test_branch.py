import divisor_master as divisor


# 29 простое число, результат теста Passed
def test_1_prst_chsl():
    n = 29
    assert divisor.prostoe_chislo(n) == False

# 1000 составное число, результат теста Passed
def test_2_prst_chsl():
    n = 1000
    assert divisor.prostoe_chislo(n) == True

# 1000 составное число, результат теста Failed
def test_3_prst_chsl():
    n = 1000
    assert divisor.prostoe_chislo(n) == False

# У 1000 максимальный простой делитель 5, результат теста Passed
def test_5_max_dlt():
    nn = 1000
    assert divisor.max_delitel_chisla(nn) == 5

# У 1000 максимальный простой делитель 5, результат теста Failed
def test_6_max_dlt():
    n = 1000
    assert divisor.max_delitel_chisla(n) == 6

# У 29 максимальный простой делитель 29, результат теста Failed
def test_7_max_dlt():
    nn = 29
    assert divisor.max_delitel_chisla(nn) == 5

# У 29 максимальный простой делитель 29, результат теста Passed
def test_8_max_dlt():
    nn = 29
    assert divisor.max_delitel_chisla(nn) == 29