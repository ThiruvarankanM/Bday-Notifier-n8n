from datetime import datetime, timedelta

# Step 1: Get contacts from previous node
contacts = [item["json"] for item in items]

# Step 2: Get tomorrow's date in dd-mm format
tomorrow = datetime.now() + timedelta(days=1)
str_tomorrow_md = tomorrow.strftime("%d-%m")

# Step 3: Prepare list for matches
birthday_contacts = []

# Step 4: Loop through each contact and match
for contact in contacts:
    dob_raw = contact.get("Date of Birth", "").strip().replace(".", "-").replace("/", "-")
    name = contact.get("Name", "").strip()

    if dob_raw == str_tomorrow_md:
        birthday_contacts.append({
            "Name": name,
            "Date of Birth": dob_raw,
            "Date to reminder": datetime.now().strftime("%d-%m"),
            "message": f"🎉 Reminder: {name} has a birthday tomorrow!"
        })

# Step 5: Return in required format
return [{
    "json": {
        "birthday_contacts": birthday_contacts
    }
}]
