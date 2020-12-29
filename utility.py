import re


def name_regex(name_input):
    name = re.match(r"^[A-Z][A-Za-z '-]+$", name_input)
    return name


def date_regex(date_input):
    date = re.match(r"^(\d{2})-(\d{2})-(\d{4}) (\d{2}):(\d{2})$", date_input)
    return date


def birthdate_regex(birthdate_input):
    birthdate = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", birthdate_input)
    return birthdate
