from src.routine import Activity, Activities, frequency_choice

# AAA - 3A -> Arrange Act Assert
def test_constructor_activity():
    activity = Activity("leitura", "7")
    result = activity.freq
    assert result == '7'

def test_return_frequency_choice_function():
    result_name = frequency_choice("weekend")
    result_number = frequency_choice("2")
    assert result_name == '2' and result_number == '2'

def test_add_activity():
    # TODO: improve
    name_activity = "leitura"
    manage_activities = Activities()
    manage_activities.add_activity(name_activity, "5")
    for activity in manage_activities.activities:
        if activity.name == name_activity:
            result = True
    assert result == True
        