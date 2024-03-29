import re

pattern = re.compile(r"\[on|off\]")  # Slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-("))
# Doesn't return anything.
# End Example


# Exercise: Make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = [
        "john@example.com",
        "python-list@python.org",
        "wha.t.`1an?utg{}y@email.com"
    ]
    for email in emails:
        if not re.match(pattern, email):
            print("you failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")


pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)
