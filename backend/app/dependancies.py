count = 0

def get_company():
    global count
    count += 1
    print(f"Executed {count} times")
    return {"company": "Genesis AI"}