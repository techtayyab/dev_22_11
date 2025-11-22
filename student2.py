import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("user provided input values:")
    print("script name:", script_name)
    print("student name:", name)
    print("roll number:", rollno)

else:
    script_name = sys.argv[0]
    name = "tayyab"   # default value as string
    rollno = "100"    # default value as string
    print("no input given - using default values:")
    print("script name:", script_name)
    print("student name:", name)
    print("roll number:", rollno)
