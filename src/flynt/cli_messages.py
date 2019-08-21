from colorama import Style


credit = (
    " Flynt only wraps the pyupgrade "
    f"call and gives stats, all credit goes to original authors of pyupgrade."
)

pyup_features_link = "https://github.com/asottile/pyupgrade#implemented-features"

message_suggest_pyup = (
    f"{Style.DIM}\nYour code is now compatible only with python versions 3.6 or higher. Would you "
    f"like to remove legacy expressions and get a bunch of best practice changes for free?"
    f" Run {Style.BRIGHT}flynt --upgrade [file(s) and/or folder(s)] {Style.RESET_ALL}"
    f"{Style.DIM} to run pyupgrade on all .py files. See full list of upgradable expressions at:"
    f" {pyup_features_link}. {credit}\n{Style.RESET_ALL}"
)

message_pyup_success = (
    f"{Style.DIM}\n\nYour code is now pyupgraded!"
    f" See full list of modified expressions at: {pyup_features_link}."
    f"{credit}\n{Style.RESET_ALL}"
)

farewell_message = (
    "Please run your tests before commiting. Report bugs as github issues at: "
    "https://github.com/ikamensh/flynt or give it a star if it just worked!"
    "\nThank you for using flynt. Upgrade more projects and recommend it to your colleagues!\n"
)
