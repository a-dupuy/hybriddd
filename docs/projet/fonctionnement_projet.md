# Projet HybridDD – Règles du Jeu & Processus

**Date de création :** 18 décembre 2025  
**Manager / Product Owner / Scrum Master / Tech Lead / QA / Client :** Sillynius (alias d'Alexandre)  
**Dev Principal (100% code) :** Alex (Grok IA)  
**Nom de code du projet :** HybridDD (Hybrid thinking + Driven Development)  
**Objectif :** Développer un produit pro en TDD strict (unit, integration, E2E, perf, robustesse, sécurité), avec 100% du code écrit par l'IA. Projet perso, à partager sur LinkedIn/X comme retour d'expérience (sous l'alias Sillynius).

## 1. Principes Fondamentaux
- **TDD strict à 100%** : Pas une ligne de code sans test d'abord (red → green → refactor).
- **100% du code par Alex** : Sillynius définit la spec, valide les tests, et accepte le done.
- **Agilité pure** : Sprints courts, feedback immédiat, retrospective systématique.
- **Documentation continue** : Chaque sprint = commits clairs, tests visibles, notes pour le thread LinkedIn/X.

## 2. Équipe (pour l'instant)
- **Sillynius** : Manager total (Product Owner, Scrum Master, Tech Lead, Business Analyst, QA, Client).
- **Alex** : Dev Principal (code, tests auto, refactor, bonnes pratiques).
- **Futur recrutement IA** : QA stricte, Designer UI/UX, Security Expert, etc., quand besoin.

## 3. Cadence : Sprints de 3 "jours ouverts maison"
- **Jours ouverts maison** : Jours où Sillynius a du temps/énergie (pas forcément consécutifs).
- **Durée réelle** : 3-7 jours calendaires par sprint selon l'agenda.
- **Structure d'un sprint** :
  1. **Jour 1** : Plan + spec + user stories + acceptance criteria + premier red test.
  2. **Jour 2** : Green + refactor + tests avancés (E2E, perf, sécurité).
  3. **Jour 3** : Review + retrospective + planning prochain sprint.
- **Pause** : Au moins 1 jour off entre sprints pour digérer.
- **Cap** : 4-5 sprints max avant une pause stabilisation (polish, doc, audit).

## 4. Process TDD & Agile
- **Daily stand-up** : Nos échanges ici (ce qu'on a fait, ce qu'on fait, blockers).
- **Sprint Review** : Quand une story est done → Sillynius valide code/tests/couverture.
- **Retrospective** : Fin de sprint → ce qui a marché, à améliorer.
- **Backlog** : Construit itérativement. Priorité par valeur utilisateur.

## 5. Stack Technique (à définir ensemble au Sprint 0 ou 1)
- Plateforme : À choisir (web, desktop, mobile, CLI, API ? On décidera selon la vision).
- Tests : Selon stack (Jest, pytest, Cypress, etc.).
- CI/CD : GitHub Actions (tests auto sur push).
- Outils sécurité/perf : Adaptés au projet (OWASP, etc.).

## 6. Repo & Documentation
- Repo GitHub : [lien à créer]
- Branches : `main` (stable), `feature/*` (par story), `sprint-x` (par sprint).
- Commits : Clairs, avec prefix (ex. : test: ajoute test login, feat: impl auth).
- Thread LinkedIn/X : Un post par sprint + rétrospective finale, sous l'alias Sillynius.

## 7. Règles Non-Négociables
- Pas de code sans test.
- Coverage > 90% sur code critique.
- Sécurité dès le départ (auth, encryption, OWASP).
- Clean code + refactor systématique.
