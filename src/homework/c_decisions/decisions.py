def get_options_ratio(option, total):
    if total == 0:
        return None
    return option / total

def get_faculty_rating(rating):
    if rating >= 0.91:
        return 'Excellent'
    elif rating >= 0.85:
        return 'Very Good'
    elif rating >= 0.71:
        return 'Good'
    elif rating >= 0.66:
        return 'Needs Improvement'
    else:
        return 'Unacceptable'

