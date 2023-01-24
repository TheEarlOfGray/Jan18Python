from applications.classesandobjects import Person

def test_person_1():
    demo = Person("Earl", 34, "Password123!")
    assert demo.name == "Earl"

def test_person_2():
    demo = Person("Earl", 34, "Password123!")
    assert demo.age == 34

def test_person_3():
    demo = Person("Earl", 34, "Password123!")
    assert "123" in demo._password

def test_person_4():
    demo = Person("Earl", 34, "Password123!")
    assert f"{demo}" == "Earl: 34."



