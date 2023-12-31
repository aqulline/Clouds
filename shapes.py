x = [7, 5]

total_data = [7, {
    'GST 06101': {'Course Code': 'GST 06101', 'Course Name': 'Development Studies', 'Unit': '9', 'CA': '27.4 / 40',
                  'SE': '41.4 / 60', 'Total': '69', 'Grade': 'B+', 'Point': '36', 'Remark': 'PASS'}}, {
                  'ITT 06104': {'Course Code': 'ITT 06104', 'Course Name': 'Object Oriented Programming', 'Unit': '12',
                                'CA': '34.5 / 40', 'SE': '52.5 / 60', 'Total': '87', 'Grade': 'A', 'Point': '60',
                                'Remark': 'PASS'}}, {
                  'ITT 06105': {'Course Code': 'ITT 06105', 'Course Name': 'System Analysis and Design', 'Unit': '9',
                                'CA': '20.3 / 40', 'SE': '39.0 / 60', 'Total': '59', 'Grade': 'B', 'Point': '27',
                                'Remark': 'PASS'}}, {
                  'ITT 06107': {'Course Code': 'ITT 06107', 'Course Name': 'IT Project Management', 'Unit': '12',
                                'CA': '29.0 / 40', 'SE': '32.4 / 60', 'Total': '61', 'Grade': 'B', 'Point': '36',
                                'Remark': 'PASS'}}, {
                  'ITT 06108': {'Course Code': 'ITT 06108', 'Course Name': 'Multimedia Concepts', 'Unit': '15',
                                'CA': '32.0 / 40', 'SE': '45.0 / 60', 'Total': '77', 'Grade': 'A', 'Point': '75',
                                'Remark': 'PASS'}}, {
                  'ITT 06109': {'Course Code': 'ITT 06109', 'Course Name': 'Web Application Development', 'Unit': '12',
                                'CA': '34.0 / 40', 'SE': '30.3 / 60', 'Total': '64', 'Grade': 'B', 'Point': '36',
                                'Remark': 'PASS'}}, {
                  'ITT 06110': {'Course Code': 'ITT 06110', 'Course Name': 'Field Practical Training II', 'Unit': '12',
                                'CA': '', 'SE': '66.7 / 100', 'Total': '67', 'Grade': 'B+', 'Point': '48',
                                'Remark': 'PASS'}}, 5, {
                  'ITT 06203': {'Course Code': 'ITT 06203', 'Course Name': 'Elements of Computerized Accounting',
                                'Unit': '9', 'CA': '33.8 / 40', 'SE': '37.2 / 60', 'Total': '71', 'Grade': 'B+',
                                'Point': '36', 'Remark': 'PASS'}}, {
                  'ITT 06204': {'Course Code': 'ITT 06204', 'Course Name': 'E-Commerce Applications', 'Unit': '12',
                                'CA': '25.5 / 40', 'SE': '40.6 / 60', 'Total': '66', 'Grade': 'B+', 'Point': '48',
                                'Remark': 'PASS'}}, {
                  'ITT 06205': {'Course Code': 'ITT 06205', 'Course Name': 'Computer Network Security', 'Unit': '12',
                                'CA': '32.0 / 40', 'SE': '44.4 / 60', 'Total': '76', 'Grade': 'A', 'Point': '60',
                                'Remark': 'PASS'}}, {
                  'ITT 06206': {'Course Code': 'ITT 06206', 'Course Name': 'Final Year Project', 'Unit': '9', 'CA': '',
                                'SE': '84.5 / 100', 'Total': '85', 'Grade': 'A', 'Point': '45', 'Remark': 'PASS'}}, {
                  'ITT 06207': {'Course Code': 'ITT 06207',
                                'Course Name': 'Principles of Customer Relationship Management', 'Unit': '9',
                                'CA': '30.0 / 40', 'SE': '32.4 / 60', 'Total': '62', 'Grade': 'B', 'Point': '27',
                                'Remark': 'PASS'}}]

organized_data = {}
i = 0  # Index for iterating through the total_data list
cote = 0

while i < len(total_data):
    count_or_course = total_data[i]
    i += 1

    if isinstance(count_or_course, int):  # If it's a count
        count = count_or_course
        courses = {}
        cote += 1

        for _ in range(count):
            course_dict = total_data[i]
            course_code = list(course_dict.keys())[0]
            courses[course_code] = course_dict[course_code]
            i += 1
        count = f"t{cote}"
        organized_data[count] = courses
    else:  # If it's a single course
        course_code = list(count_or_course.keys())[0]
        organized_data[course_code] = count_or_course[course_code]

# Print the organized data
print(organized_data.keys())


def to_organize(total_data):
    i = 0  # Index for iterating through the total_data list
    cote = 0
    organized_data = {}

    while i < len(total_data):
        count_or_course = total_data[i]
        i += 1

        if isinstance(count_or_course, int):  # If it's a count
            count = count_or_course
            courses = {}
            cote += 1

            for _ in range(count):
                course_dict = total_data[i]
                course_code = list(course_dict.keys())[0]
                courses[course_code] = course_dict[course_code]
                i += 1
            count = f"t{cote}"
            organized_data[count] = courses
        else:  # If it's a single course
            course_code = list(count_or_course.keys())[0]
            organized_data[course_code] = count_or_course[course_code]

    return organized_data
