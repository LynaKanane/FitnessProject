import csv

FILENAME = "members.csv"

# ----------- CLASSE MEMBER -----------
class Member:
    def __init__(self, id, name, age, email, phone, major, skills, interests, activity, subscription):
        self.id = int(id)
        self.name = name
        self.age = int(age)
        self.email = email
        self.phone = phone
        self.major = major
        self.skills = skills.split(",")
        self.interests = interests.split(",")
        self.activity = activity
        self.subscription = subscription

    def is_paid(self):
        return self.subscription.lower() == "paid"

    def display_profile(self):
        print(f"👤 {self.name} ({self.age} ans)")
        print(f"📧 {self.email} | ☎️ {self.phone}")
        print(f"🎓 {self.major}")
        print(f"💪 Skills: {', '.join(self.skills)}")
        print(f"❤️ Interests: {', '.join(self.interests)}")
        print(f"🏃 Activity: {self.activity}")
        print(f"💰 Subscription: {self.subscription}")
        print("-" * 40)


# ----------- FONCTION POUR LIRE LES MEMBRES -----------
def read_members():
    members = []
    try:
        with open(FILENAME, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                member = Member(
                    row['id'],
                    row['NomPrenom'],
                    row['age'],
                    row['email'],
                    row['numerotel'],
                    row['major'],
                    row['skills'],
                    row['interests'],
                    row['activity'],
                    row['subscription_status']
                )
                members.append(member)
    except FileNotFoundError:
        print("Erreur : fichier introuvable !")
    return members


# ----------- TEST DU PROGRAMME -----------
if __name__ == "__main__":
    members = read_members()
    for m in members:
        m.display_profile()
