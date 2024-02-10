#
import decisions

options = float(input("Enter the options: "))
total = float(input("Enter the total: "))

result = decisions.get_options_ratio(options, total)

print("Faculty Rating:", decisions.get_faculty_rating(result))

