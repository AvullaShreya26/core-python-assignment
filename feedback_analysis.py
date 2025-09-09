def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."
    positives = sum(1 for r in ratings if r >= 4)
    percentage = (positives / len(ratings)) * 100
    return f"Positive Feedback: {round(percentage, 2)}%"
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(positive_feedback_percentage(ratings))
