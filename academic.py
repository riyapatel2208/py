courses = {}

def add_course(name, credits, points):
    courses[name] = (credits, points)
    print(f"Added: {name}")

def drop_course(name):
    if name in courses:
        del courses[name]
        print(f"Dropped: {name}")
    else:
        print(f"Course not found: {name}")

def print_record():
    if not courses:
        print("No courses.")
    else:
        for name, (credits, points) in courses.items():
            print(f"{name}: {credits} credits, {points} points")

def calculate_cgpa():
    total_credits = sum(credits for credits, _ in courses.values())
    total_points = sum(credits * points for credits, points in courses.values())
    cgpa = total_points / total_credits if total_credits > 0 else 0
    print(f"CGPA: {cgpa:.2f}")




