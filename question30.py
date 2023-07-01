# Nested dictionary Problem
# Calculate percentage of students on the based of marks 
# subject : 5

students={
    'jay':{'details':{'rollno':101, 'marks':[92,89,90,78,95]}},
    'viru':{'details':{'rollno':102, 'marks':[92,89,70,68,85]}},
    'basanti':{'details':{'rollno':103, 'marks':[72,89,98,88,95]}},
    'thakur':{'details':{'rollno':104, 'marks':[92,89,90,68,45]}}
}
subject=5
for std in students:
    per=(sum(students[std]['details']['marks']))/subject
    print(f"{std} is scored {per}%")