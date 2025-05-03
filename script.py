# script.py
import csv

def lire_csv(fichier):
    with open(fichier, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def statistiques(rows):
    scores = [int(r['score']) for r in rows]
    return {
        'nombre_lignes': len(rows),
        'score_max': max(scores),
        'score_min': min(scores),
        'moyenne': sum(scores) / len(scores)
    }

if __name__ == '__main__':
    donnees = lire_csv('data.csv')
    stats = statistiques(donnees)
    print(f"Nombre de lignes traitées : {stats['nombre_lignes']}")
    print(f"Score maximum : {stats['score_max']}")
    print(f"Score minimum : {stats['score_min']}")
    print(f"Score moyen : {stats['moyenne']:.2f}")
