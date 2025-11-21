# simple file-based logger
log_file = "actions.log"

def write_log(message: str):
    # append log message to file
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")
