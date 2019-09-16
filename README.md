# Première initiation à git en programmant des formules de quadrature en python

Ce fichier fait office de compte rendu. Il doit donc être mis à jour au
cours de la séance, au fur et à mesure que vous réalisez le travail. Les
fichiers modifiés et ajoutés font évidemment partie du travail.

C'est la version du mardi 17 septembre 2019 à 23h et son historique qui
sera notée.

*Il n'est pas nécessaire d'aller au bout des questions (le travail est
adapté à vos expériences de programmation, qui sont très
variables). C'est l'effort dans l'utilisation des outils (git et python)
qui est valorisé.*

**À la fin de votre travail, il est donc capital de pousser (*git push*)
  vos modifications sur le serveur, afin que je puisse les voir**

*Rappel:* prenre connaissance, brièvement, du [langage
Markdown](https://guides.github.com/features/mastering-markdown) propre
à la plateforme Github.

Si vous lisez ceci, c'est que vous avez:

- un compte sur la plateforme github.com, et un email validé de l'
  Université

- accepté le lien envoyé sur votre messagerie étudiante, et ainsi obtenu
  la création automatique d'un dépôt git contenant le descriptif du
  travail à réaliser (ce fichier).

## Première partie: environnement de travail et initiation à Python

1. Une fois le dépôt créé, vous le voyez sur votre compte github (en
ligne). Vous pouvez donc récupérer l'adresse et télécharger le dépôt
pour commencer à travailler (*git clone <url à récupérer en ligne>*).

2. N'oubliez pas de configurer git si nécessaire (*git config --list,
git config --local user.{name,email}*).

3. Préparez votre environnement de travail: éditeur de texte (*emacs*,
*vim*, *atom*...) et terminaux (terminal par défaut du système, pour git
et pour l'interpréteur *ipython3*), ou bien environnement de
développement intégré (comme *spyder3*). Pouvez-vous détailler
ci-dessous votre choix d'environnement de travail ?

*...écrire la réponse ici...*

4. Puisque vous avez apporté des modifications cohérentes (réponse à la
question 3. ci-dessus), validez ces modifications (*git add* et *git
commit -m "..."*).

5. Familiarisez vous avec le contenu du répertoire, qui devrait
ressembler à :
    
```
├── README.md
├── img
│   └── test_1.png
├── src
│   ├── fonctions_test.py
│   ├── quadratures.py
│   └── tests.py
└── tex
    ├── memo_quadratures.pdf
    ├── memo_quadratures.tex
```

Quel est la nature (langage ?) et le rôle (texte, programme, autre) de
chacun des fichiers présents ?

**Pensez à valider régulièrement votre travail, et à pousser les
  changements sur le serveur (*git push*)**

## Deuxième partie: formules de quadrature

1. En suivant le modèle de la formule du point milieu, dans le fichier
[./src/quadratures.py](./src/quadratures.py) programmer la méthode des
trapèzes (programmer une autre fonction dans le même fichier
[./src/quadratures.py](./src/quadratures.py)).

2. Tester cette nouvelle quadrature en utilisant comme modèle le
programme [./src/tests.py](./src/tests.py): vérifier que cette formule
calcul de manière exacte les intégrales de polynoes de degré au plus 1,
et comment une erreur équivalente à $h^2$ (ou encore
$N^{-2}$). Reproduire ci-dessous les tableaux d'erreurs qui démontrent
ce résultat, et inclure le graphe de convergence des approximations.

3. On veut tester nos formules pour d'autres fonctions que les
polynômes. Pour cela, on ajoute les fonctions souhaitées dans le fichier
[./src/fonctions_test.py](./src/fonctions_test.py). En suivant le modèle
donné pour les monômes, programmer les fonctions (et une de leurs
primitives)
 - $f(x) = |x|$ et $g(x) = 0.5*x*|x|$;
 - $f(x) = cos(x)$ et $g(x) = sin(x)$;
 - $f(x) = exp(x)$ et $g(x) = exp(x)$;
 - $f(x) = 1/(1+x^2)$ et $g(x) = atan(x)$.

4. En adaptant le programme [./src/tests.py](./src/tests.py), produire
une unique graphes qui compare les graphes de convergence de l'erreur
pour ces nouvelles fonctions integrées entre $-1$ et $+1$. Insérez
l'image ci-dessous, et faites tous les commentaires utiles.
