<p align="center">
  <img src="banner.jpeg" alt="Saveena Solanki — Computational Biologist" width="100%">
</p>

<p align="center">
  <a href="https://github.com/SaveenaSolanki/SaveenaSolanki"><img src="https://komarev.com/ghpvc/?username=SaveenaSolanki&label=PROFILE+VIEWS&color=ac946f&style=flat&labelColor=17110d" alt="Profile views"></a>
  <a href="https://github.com/SaveenaSolanki?tab=repositories"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FSaveenaSolanki&query=public_repos&label=repos&color=ac946f&style=flat&labelColor=17110d" alt="Public repos"></a>
  <a href="https://saveenasolanki.github.io/"><img src="https://img.shields.io/badge/academic+site-saveenasolanki.github.io-d4b87a?style=flat&labelColor=17110d" alt="Academic site"></a>
  <a href="https://github.com/SaveenaSolanki/compbio-toolkit-suite"><img src="https://img.shields.io/badge/CompBio+Toolkit+Suite-6+tools-f5e3ca?style=flat&labelColor=17110d" alt="CompBio Toolkit Suite"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-ac946f?style=flat&labelColor=17110d" alt="Python 3.10+"></a>
</p>

---

## Prologue

**Biology is messy.** Molecules arrive salted, malformed, mislabeled. Assays speak in
competing dialects — nanomolar here, micromolar there, thresholds everywhere. Knowledge
graphs tangle thousands of relations without a shared grammar. And before any model can
learn from this, someone has to make the data *honest*.

That is what I do.

I am a computational biologist at **IIIT Delhi**, working at the intersection of machine
learning, cheminformatics, and biomedical knowledge graphs. My research is aimed at
**building AI beyond observed biological space** — across unseen molecules, proteins,
interactions, and cellular states. The road to that goal runs through data that is clean,
comparable, and reproducible. Every repository on this profile is a step on that road.

---

## Chapter I · The Mission

Four arenas, one thread — turning raw biology into learned models.

| Arena | What I work on | Tools of the trade |
|---|---|---|
| 🧪 **Molecular representation** | Cleaning and canonicalizing structures, scaffold-aware splits, chemical-space analysis | RDKit, scikit-learn |
| 🧫 **Bioactivity & assay data** | Unit standardization, pActivity conversion, quality flagging | pandas, NumPy |
| 🕸️ **Biomedical knowledge graphs** | Relation-sign standardization, structural auditing, identifier harmonization | pandas, Typer |
| 🤖 **ML engineering for biology** | Leakage-aware evaluation, featurizer baselines, reproducible CLI pipelines | scikit-learn, pytest, ruff |

---

## Chapter II · The Pipeline

**From raw molecules to learned models** — the *CompBio Toolkit Suite* is not six random
utilities. It is one pipeline, split into composable stages. Each stage owns one problem,
ships a CLI, and is tested. Install only the stage you need; run them together when you
need the whole journey.

```
   molecules           assays            graphs            models
 ─────────────      ─────────────      ─────────────      ─────────────
 raw SMILES    ──▶  smiles-cleankit   ──▶  clean, canonical, desalted structures
 bioassay      ──▶  assaytablecleaner ──▶  unit-standardized values + pActivity
 libraries     ──▶  scaffoldsplitlab  ──▶  leakage-free train / val / test splits
 identifiers   ──▶  molidmapper       ──▶  harmonized PubChem / ChEMBL / UniProt IDs
 KG edges      ──▶  biokg-signmapper  ──▶  relations mapped to controlled signs
 KG structure  ──▶  kg-stats-audit    ──▶  node/edge statistics + audit report
```

| Stage | Tool | CLI | Role in the pipeline |
|---|---|---|---|
| 1 · Molecules | [**smiles-cleankit**](https://github.com/SaveenaSolanki/smiles-cleankit) | `smiles-clean` | Validate, canonicalize, desalt; InChIKey generation |
| 2 · Assays | [**assaytablecleaner**](https://github.com/SaveenaSolanki/assaytablecleaner) | `assay-clean` | Unit conversion to molar, pActivity, quality flags |
| 3 · Splits | [**scaffoldsplitlab**](https://github.com/SaveenaSolanki/scaffoldsplitlab) | `scaffold-split` | Scaffold / random / hash splits with leakage checks |
| 4 · Identifiers | [**molidmapper**](https://github.com/SaveenaSolanki/molidmapper) | `molid-map` | Detect & merge PubChem / ChEMBL / DrugBank / UniProt |
| 5 · Relations | [**biokg-signmapper**](https://github.com/SaveenaSolanki/biokg-signmapper) | `biokg-sign` | KG relations → activation / inhibition / association… |
| 6 · Structure | [**kg-stats-audit**](https://github.com/SaveenaSolanki/kg-stats-audit) | `kg-audit` | Degree distributions, isolated nodes, audit reports |

Three more stages are on the bench — chemical-space maps, featurizer benchmarks, and
target-set profiling. See the [suite roadmap](https://github.com/SaveenaSolanki/compbio-toolkit-suite/blob/main/ROADMAP.md).

---

## Chapter III · The Craft

Small tools. One job each. CLI-first. Tested with `pytest`, linted with `ruff`,
documented with examples. No private datasets, no black boxes — toy examples only, so
every result is reproducible by anyone, anywhere.

<p align="center">
  <img src="https://img.shields.io/badge/Python-ac946f?style=for-the-badge&logo=python&logoColor=17110d&labelColor=241a14" alt="Python">
  <img src="https://img.shields.io/badge/RDKit-f5e3ca?style=for-the-badge&logo=rdkit&logoColor=17110d&labelColor=241a14" alt="RDKit">
  <img src="https://img.shields.io/badge/pandas-ac946f?style=for-the-badge&logo=pandas&logoColor=17110d&labelColor=241a14" alt="pandas">
  <img src="https://img.shields.io/badge/NumPy-f5e3ca?style=for-the-badge&logo=numpy&logoColor=17110d&labelColor=241a14" alt="NumPy">
  <img src="https://img.shields.io/badge/scikit--learn-ac946f?style=for-the-badge&logo=scikitlearn&logoColor=17110d&labelColor=241a14" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Typer-f5e3ca?style=for-the-badge&logo=python&logoColor=17110d&labelColor=241a14" alt="Typer CLI">
  <img src="https://img.shields.io/badge/pytest-ac946f?style=for-the-badge&logo=pytest&logoColor=17110d&labelColor=241a14" alt="pytest">
  <img src="https://img.shields.io/badge/ruff-f5e3ca?style=for-the-badge&logo=ruff&logoColor=17110d&labelColor=241a14" alt="ruff">
  <img src="https://img.shields.io/badge/GitHub+Actions-ac946f?style=for-the-badge&logo=githubactions&logoColor=17110d&labelColor=241a14" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Jupyter-f5e3ca?style=for-the-badge&logo=jupyter&logoColor=17110d&labelColor=241a14" alt="Jupyter">
</p>

---

## Chapter IV · The Record

<div align="center">
  <img src="https://github-stats-extended.vercel.app/api?username=SaveenaSolanki&show_icons=true&theme=transparent&title_color=d4b87a&icon_color=ac946f&text_color=f5e3ca&bg_color=17110d&hide_border=true&count_private=true" alt="GitHub stats" height="180">
  <img src="https://github-stats-extended.vercel.app/api/top-langs/?username=SaveenaSolanki&layout=compact&langs_count=8&theme=transparent&title_color=d4b87a&text_color=f5e3ca&bg_color=17110d&hide_border=true" alt="Top languages" height="180">
  <br>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=SaveenaSolanki&theme=transparent&background=17110d&hide_border=true&ring=d4b87a&fire=ac946f&currStreakLabel=d4b87a&sideLabels=f5e3ca&dates=a08a6c" alt="GitHub streak" width="420">
  <br><br>
  <img src="analytics/achievements.svg" alt="Achievement wall — self-hosted analytics" width="100%">
  <br><br>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=SaveenaSolanki&theme=react-dark&bg_color=17110d&hide_border=true&area=true&color=d4b87a&line=ac946f&point=f5e3ca&area_color=2d221c" alt="GitHub activity graph" width="100%">
</div>

> 🏆 The achievement wall is **self-hosted** — generated from the GitHub API by
> [`.github/workflows/analytics.yml`](.github/workflows/analytics.yml) on a monthly schedule.
> No third-party badge services.

---

## Epilogue · Open Science

Science should be reproducible, and figures should be re-usable. Alongside the toolkit,
I maintain [**SciSVG**](https://github.com/SaveenaSolanki/SciSVG) — an open library of
editable scientific vector graphics (30+ assets, CC BY 4.0) for figures, presentations,
and publications — and an [academic profile](https://saveenasolanki.github.io/) with my
research and portfolio.

<p align="center">
  <a href="https://saveenasolanki.github.io/"><img src="https://img.shields.io/badge/Portfolio-saveenasolanki.github.io-17110d?style=for-the-badge&logo=githubpages&logoColor=17110d&labelColor=f5e3ca" alt="Portfolio"></a>
  <a href="mailto:saveenas@iiitd.ac.in"><img src="https://img.shields.io/badge/Email-saveenas%40iiitd.ac.in-17110d?style=for-the-badge&logo=gmail&logoColor=17110d&labelColor=ac946f" alt="Email"></a>
  <a href="https://github.com/SaveenaSolanki"><img src="https://img.shields.io/badge/GitHub-%40SaveenaSolanki-17110d?style=for-the-badge&logo=github&logoColor=17110d&labelColor=d4b87a" alt="GitHub"></a>
</p>

<p align="center">
  <sub><i>"From raw molecules to learned models — open tools, reproducible science, small composable pieces."</i></sub>
</p>
