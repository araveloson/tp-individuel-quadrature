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

**À la fin de votre travail, il est donc capital de pousser (git push)
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
développement intégré (comme *spyder3*). Pouvez-vous détailler ci-dessous
votre choix d'environnement de travail ?

*...écrire la réponse ici...*

4. Puisque vous avez apporté des modifications cohérentes (réponse à la
question 3. ci-dessus), validez ces modifications (*git add* et *git
commit -m "..."*).

5. Familiarisez vous avec le contenu du répertoire, qui devrait
ressembler à :
    
├── README.md
├── img
│   └── test_1.png
└── src
    ├── fonctions_test.py
    ├── quadratures.py
    ├── tests.py

Quel est la nature (langage ?) et le rôle (texte, programme, autre) de
chacun des fichiers présents ?
