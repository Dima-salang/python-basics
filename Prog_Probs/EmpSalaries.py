# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10^-5 of the actual answer will be accepted.


def avg_salaries(emp_salaries):
    emp_salaries.remove(max(emp_salaries))
    emp_salaries.remove(min(emp_salaries))
    return sum(emp_salaries) / len(emp_salaries)


