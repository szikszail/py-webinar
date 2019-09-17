def grade(score):
    """The function returns the grade (1-5) of the student

    It is based on the following rules:
    - 90 -    : 5
    - 80 - 89 : 4
    - 70 - 79 : 3
    - 60 - 69 : 2
    -    - 59 : 1

    Parameters
    ----------
    score : int
        (0 <= score <= 100)

    Returns
    -------
    grade : int
        The grade or 0 if the score is not valid
    """

    gradeOfStudent = -1
    # Your task is to calculate the grade of the student
    # based on his/her score which can be found in the
    # score variable and those rules can be found in the
    # documentation of the function.
    # Store the grade in the gradeOfStudent variable.
    # Also take into consideration the documentation of the function!
    # PLACE YOUR CODE BETWEEN THIS...

    if (0 <= score <= 100):
        if (score >= 90):
            gradeOfStudent = 5
        elif (score >= 80):
            gradeOfStudent = 4
        elif (score >= 70):
            gradeOfStudent = 3
        elif (score >= 60):
            gradeOfStudent = 2
        else:
            gradeOfStudent = 1
    else:
        gradeOfStudent = 0

    # ...AND THIS COMMENT LINE!
    return gradeOfStudent
