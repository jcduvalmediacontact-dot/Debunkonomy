# Integration — Debunk'Onomy Assistant Widget

**Version 1.0** — Août 2026

---

## Résumé rapide

Le widget assistant de Debunk'Onomy est un **fichier HTML/JS standalone** qui se copie-colle à la fin du `<body>` de n'importe quelle page du site. Il crée un bouton flottant (coin bas droit) qui ouvre une interface de chat pour expliquer NEMO IMS et l'économie de l'équilibre.

**Aucune dépendance externe.** Aucun backend nécessaire. Aucune configuration.

---

## Installation (3 étapes)

### 1. Télécharger le fichier
Récupérez `debunkonomy-assistant-widget.html`

### 2. Copier le contenu
Ouvrez le fichier et copiez **tout son contenu** (du premier `<div>` au dernier `</div>`)

### 3. Coller sur vos pages
Pour chaque page où vous voulez le widget, collez le code immédiatement **avant la balise de fermeture `</body>`**

**Exemple :**
```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <!-- ... head content ... -->
</head>
<body>
  <!-- ... page content ... -->
  
  <!-- COLLER LE WIDGET ICI -->
  <div style="font-family: var(--font-sans, -apple-system, ...">
    ...
  </div>
  <!-- FIN DU WIDGET -->
  
</body>
</html>
```

---

## Déploiement recommandé

### Option A : Injecter globalement (recommandé)
Si votre site a un **layout ou template partagé** (header/footer commun), injectez le widget une seule fois dans le template partagé. Il apparaîtra alors sur **toutes les pages**.

**Exemple pour un site statique :**
- Si vous avez une structure `_layout.html` ou `base.html` incluse partout, y coller le widget une fois suffit.

### Option B : Injecter page par page
Si votre site n'a pas de template partagé, ajoutez le widget manuellement à chaque page (ou chaque section importante : `/articles/`, `/nemo-ims/`, `/medias/`, etc.).

### Option C : Charger depuis un fichier externe (avancé)
Si vous préférez maintenir le widget dans un fichier séparé sans dupliquer le code :

1. Sauvegardez `debunkonomy-assistant-widget.html` quelque part accessible (e.g., `/assets/widgets/`)
2. Chargez-le avec un `<script>` ou une technique `fetch()` :

```html
<script>
  fetch('/assets/widgets/debunkonomy-assistant-widget.html')
    .then(r => r.text())
    .then(html => document.body.insertAdjacentHTML('beforeend', html))
</script>
```

---

## Configuration (optionnel)

### Désactiver le widget sur certaines pages
Si vous voulez que le widget **n'apparaisse PAS** sur une page donnée, ajoutez ceci **avant** le widget :

```html
<script>
  window.DEBUNK_CHAT_DISABLED = true;
</script>
```

Puis, en début du script du widget, ajoutez un test :
```javascript
if (window.DEBUNK_CHAT_DISABLED) return;
```

### Personnaliser le message d'accueil
Dans le code du widget, repérez :
```html
<div class="debunk-empty-state">
  Posez vos questions sur NEMO IMS, l'économie de l'équilibre...
```

Vous pouvez modifier le texte entre les balises.

### Ajouter de nouveaux thèmes de réponses
Dans la section `knowledgeBase`, ajoutez une nouvelle clé :

```javascript
nouveau_theme: {
  keywords: ['mot-clé1', 'mot-clé2', 'mot-clé3'],
  response: "Votre réponse ici..."
}
```

Le widget cherchera automatiquement ces mots-clés dans les questions de l'utilisateur.

---

## Langues

**Actuellement :** Le widget est **100% en français**.

**Pour supporter d'autres langues :**
1. Créez une version du widget pour chaque langue (copier + traduire les textes UI et les réponses)
2. Ou, implémentez une détection de langue et chargez le bon widget basé sur `document.documentElement.lang`

Exemple de structure pour multilingue :
```html
<script>
  const lang = document.documentElement.lang || 'fr';
  const widgetSrc = {
    fr: '/assets/widgets/assistant-fr.html',
    en: '/assets/widgets/assistant-en.html',
    es: '/assets/widgets/assistant-es.html'
  }[lang];
  
  if (widgetSrc) {
    fetch(widgetSrc)
      .then(r => r.text())
      .then(html => document.body.insertAdjacentHTML('beforeend', html))
  }
</script>
```

---

## Vérification

Après intégration, testez sur chaque page :

- [ ] Le bouton `?` apparaît en bas à droite
- [ ] Cliquer le bouton ouvre la fenêtre de chat
- [ ] Le champ de saisie est focalisable
- [ ] Les messages s'envoient avec `Enter` ou le bouton `→`
- [ ] L'assistant répond (avec petit délai d'animation)
- [ ] Le bouton `✕` ferme le chat
- [ ] Le bouton `?` réapparaît après fermeture

---

## Limitations actuelles

1. **Base de connaissances statique** — Les réponses sont pré-écrites, pas générées par IA. Bon pour les questions prévisibles, limité pour les questions libres.

2. **Pas d'historique persistant** — L'historique du chat disparaît au rechargement. Chaque visite = nouvelle conversation.

3. **Pas de liage avec le contexte de la page** — Le widget ne sait pas sur quelle page l'utilisateur se trouve actuellement. Toutes les réponses sont génériques.

4. **Pas de traduction automatique** — Chaque langue demande un fichier widget séparé.

---

## Évolutions futures

Pour monter en puissance, trois directions possibles :

### v2.0 : IA backend
- Widget reste le même, mais appelle une fonction backend (Serverless) qui utilise l'API Claude
- Réponses intelligentes et contextualisées
- Possibilité de poser des questions libres
- Demande : une fonction backend (Vercel, AWS Lambda, etc.) + clé API Anthropic sécurisée

### v2.1 : Multilingue
- Widget traduit en 7 langues (FR, EN, ES, PT, DE, IT, AR)
- Chaque langue a sa propre base de connaissances enrichie
- Détection automatique basée sur `document.documentElement.lang`

### v3.0 : Persistance et analytics
- Historique stocké en localStorage (optionnel, avec opt-in)
- Metrics basiques : nombre de messages, thèmes les plus demandés
- Intégration avec Google Analytics ou similar

---

## Support & Maintenance

**Ajouter une réponse :** Modifiez la section `knowledgeBase` du widget.

**Corriger une réponse :** Cherchez le mot-clé correspondant, modifiez le champ `response`.

**Ajouter un nouveau thème :** Duplicat une entrée existante, changez les `keywords` et la `response`.

**Signaler un bug :** Contactez `contact@debunkonomy.org` avec :
- Page URL où le problème survient
- Navigateur et OS
- Description du problème
- Screenshot si possible

---

## Changelog

**v1.0 (27 août 2026)**
- Initial release
- 16 thèmes de réponses couverts
- Support FR complet
- Widget flottant standalone
- Support dark mode

---

*Debunk'Onomy — Think & Move to Degrowth*  
*contact@debunkonomy.org*
