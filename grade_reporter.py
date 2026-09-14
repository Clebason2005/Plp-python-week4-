scores = [72, 45, 90, 61, 38]
passed = 0
failed = 0
total_score = 0
for score in scores:
    total_score += score
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    print(f"{score} - {grade}")
    if score >= 50:
        passed += 1
    else:
        failed += 1
average = total_score / len(scores)
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {round(average, 1)}")
