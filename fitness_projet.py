import csv

FILENAME = "members.csv"


def read_members():
    members = []
    try:
        with open(FILENAME, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                members.append(row)
    except FileNotFoundError:
        print("❌ Erreur : le fichier members.csv est introuvable.")
    return members



def members_to_html(members):
    html = ['''
    <html>
    <head>
        <meta charset="utf-8">
        <title>Fitness Club - Liste des Membres</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f7f9fb;
                color: #333;
                margin: 20px;
            }
            h1 {
                text-align: center;
                color: #d63384;
            }
            table {
                width: 90%;
                margin: auto;
                border-collapse: collapse;
                background: white;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                border-radius: 10px;
                overflow: hidden;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 10px;
                text-align: center;
            }
            th {
                background-color: #ffb6c1;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>🏋️‍♀️ Fitness Club - Liste des Membres</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Nom & Prénom</th>
                <th>Âge</th>
                <th>Email</th>
                <th>Téléphone</th>
                <th>Spécialité</th>
                <th>Compétences</th>
                <th>Intérêts</th>
                <th>Activité</th>
                <th>Statut</th>
            </tr>
    ''']

    for m in members:
        html.append(f"""
        <tr>
            <td>{m['id']}</td>
            <td>{m['NomPrenom']}</td>
            <td>{m['age']}</td>
            <td>{m['email']}</td>
            <td>{m['numerotel']}</td>
            <td>{m['major']}</td>
            <td>{m['skills']}</td>
            <td>{m['interests']}</td>
            <td>{m['activity']}</td>
            <td>{m['subscription_status']}</td>
        </tr>
        """)

    html.append("""
        </table>
    </body>
    </html>
    """)

    return "\n".join(html)



def save_html(content):
    filename = "members.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Fichier HTML généré avec succès : {filename}")



if __name__ == "__main__":
    members = read_members()
    if members:
        html_content = members_to_html(members)
        save_html(html_content)
