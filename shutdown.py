def shutdown(answer):
    if answer == "yes":
        return "Its shutting down"
    if answer   == "no":
        return "shutdown aborted"
    return "invalid answer"
print(shutdown("yes"))
