def parse_txt_logs(filepath):
    logs = []

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            try:
                ip, event = line.split(",")

                logs.append({
                    "ip": ip.strip(),
                    "event": event.strip()
                })

            except:
                print("Skipping invalid line:", line)

    return logs