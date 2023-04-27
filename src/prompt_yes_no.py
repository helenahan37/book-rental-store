from colored import fg, bg, attr

# Define if user would like continue to take an action
def prompt_yes_or_no(prompt):
    while True:
        confirm_browse = input(prompt).lower()
        if confirm_browse not in ["y", "n"]:
            print(f"\n{fg(229)}Sorry, the option you have entered is not valid, please enter 'y' or 'n'. {attr(0)}")         
        else:
            return confirm_browse == "y"