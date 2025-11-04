# vertex-cover-solver
## Bibliothèques utilisées...
Pour faciliter notre travail et se concentrer sur les algorithmes, nous avons utilisé `networkx` pour la représentation des graphes, ainsi que les opérations très basiques (rajout de sommets, d'arrêtes...etc). Nous avons également utilisé `matplotlib` pour représenter la compléxité des algorithmes étudiés. Il s'uffit d'executer la commande suivante pour installer toutes les dépendances :
```
pip install -r requirements.txt
```
## Structure du projet
Nous avons regroupé nos fonctions dans 4 fichiers :
- `basic_operations` pour les opérations de bases
- `branching` pour toutes les fonctions de branchement
- `testing` pour les fonctions qui testent les algorithmes
  - Il contient notamment la fonction `test_vc_solver` qui prend une fonction quelconque qui est censé résoundre notre problème et produit deux listes représentant les résultats des testes
- `approximation_algorithms` pour les algorithmes d'approximation