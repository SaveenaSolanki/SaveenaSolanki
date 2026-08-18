<p align="center">
  <img src="banner.svg" alt="Saveena Solanki — Computational Biology and Molecular AI" width="100%">
</p>

<p align="center">
  <a href="https://saveenasolanki.github.io/"><img src="https://img.shields.io/badge/Portfolio-saveenasolanki.github.io-17110d?style=for-the-badge&logo=githubpages&logoColor=17110d&labelColor=f5e3ca" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/saveenasolanki/"><img src="https://img.shields.io/badge/LinkedIn-saveenasolanki-17110d?style=for-the-badge&logo=linkedin&logoColor=17110d&labelColor=d4b87a" alt="LinkedIn"></a>
  <a href="mailto:saveenas@iiitd.ac.in"><img src="https://img.shields.io/badge/Email-saveenas%40iiitd.ac.in-17110d?style=for-the-badge&logo=gmail&logoColor=17110d&labelColor=ac946f" alt="Email"></a>
</p>

---

## Computational Biology × Molecular AI

I develop computational approaches for understanding biology across molecular scales — from learning representations of individual molecules to modeling protein interactions and the biological systems those interactions reshape.

My research sits at the intersection of:

*molecular representation learning · protein interactions · targeted protein degradation · molecular glues · mechanistic machine learning · biomedical knowledge graphs*

**Research question:** How can AI move beyond memorizing observed chemical and biological space to reason about unseen molecules, interactions and biological states?

---

## Research Program

<p align="center">
  <b>MOLECULES</b> &nbsp; → &nbsp; <b>REPRESENTATIONS</b> &nbsp; → &nbsp; <b>INTERACTIONS</b> &nbsp; → &nbsp; <b>BIOLOGICAL SYSTEMS</b> &nbsp; → &nbsp; <b>DISCOVERY</b>
</p>

My projects address different parts of this continuum — from representation to intervention. The projects below are my own research (01–06); the final entry (07) is collaborative work.

---

## Research

### 01 · SynGlue
**Designing molecules that control protein fate**

*Why do apparently similar PROTACs produce very different degradation outcomes?*

SynGlue approaches targeted protein degradation as a coupled molecular-design problem involving:

> Target ligand + E3-ligase ligand + linker + ternary-complex geometry + degradation behaviour

rather than treating the warhead as the sole determinant of degrader activity.

The platform integrates computational approaches for analysing and designing PROTACs, including molecular generation, linker reasoning, degradation modelling and structure-informed prioritisation. The larger scientific question is how small molecules can be engineered to create productive interactions between proteins and redirect cellular machinery.

**Research themes:** Targeted Protein Degradation · PROTACs · Generative AI · Ternary Complexes · Polypharmacology

**Resources:** [Code](https://github.com/the-ahuja-lab/SynGlue) · [PyPI](https://pypi.org/project/synglue/)

---

### 02 · MetaboGlue
**Understanding molecules that reprogram protein interactions**

*Can endogenous metabolites and small molecules create, stabilise or inhibit protein interactions?*

MetaboGlue extends my interest from conventional protein–ligand modelling toward unified **Protein–Ligand (PL)** and **Protein–Ligand–Protein (PLP)** interaction modelling. The goal is to understand the molecular principles governing metabolite-mediated protein-interaction modulation and molecular-glue behaviour.

The framework combines ligand, protein and structural information to study how small molecules may alter interaction landscapes rather than acting only through classical one-protein/one-ligand binding.

**Research themes:** Molecular Glues · Protein Interactions · PL/PLP Modelling · Multimodal AI · Structural Biology

**Status:** Active research.

---

### 03 · ChemicalDice / CDI
**Learning representations of molecules**

*How should a molecule be represented when no single molecular description captures all of its biology and chemistry?*

ChemicalDice / CDI explores multimodal molecular representation learning by integrating complementary molecular views into a unified latent representation. The framework brings together information derived from:

- physicochemical properties
- molecular graphs
- two-dimensional molecular representations
- bioactivity information
- quantum-chemical properties
- molecular language models

These complementary representations are integrated and subsequently distilled into a deployable molecular representation accessible from SMILES. The broader objective is to construct representations that remain useful beyond the exact chemical space observed during training.

**Research themes:** Multimodal Learning · Molecular Representations · Representation Distillation · Chemical Space · Drug Discovery

**Resources:** [Code](https://github.com/the-ahuja-lab/ChemicalDice) · [Documentation](https://the-ahuja-lab.github.io/ChemicalDice/)

---

### 04 · Trojan-Horses
**Mechanism-aware molecular machine learning**

*Can molecular ML distinguish compounds through the mechanisms by which they alter redox biology?*

This work develops mechanism-aware models for analysing ROS modulators and antioxidant behaviour while connecting molecular information with biologically interpretable mechanisms.

**Role:** first author

**Themes:** Redox Biology · Mechanistic ML · Molecular Representations · Interpretability

**Resources:** [Code](https://github.com/the-ahuja-lab/Trojan-Horses)

---

### 05 · EvOlf
**Evolution-guided ligand–GPCR prediction**

*Can evolutionary information improve molecular recognition models across the mammalian GPCRome?*

EvOlf uses evolutionary and molecular information to model ligand–GPCR interactions across diverse mammalian receptors and species, with applications including receptor deorphanisation. The accompanying computational pipeline supports large-scale ligand–receptor screening using molecular featurisation, protein representations and deep-learning inference.

**Role:** first author

**Themes:** GPCRs · Evolutionary Biology · Protein Embeddings · Molecular Recognition

**Resources:** [Code](https://github.com/the-ahuja-lab/EvOlf) · [Web Server](https://evolf.ahujalab.iiitd.edu.in/) · [Pipeline](https://github.com/the-ahuja-lab/evolf-pipeline)

---

### 06 · Inertrope
**Thermodynamic fingerprints as biological signals**

*Can molecular-interaction thermodynamics encode diagnostically useful biological states?*

Inertrope investigates machine-learning approaches based on thermodynamic and spectroscopic fingerprints for distinguishing biological sample states. This work reflects a broader interest in extracting predictive biological information from biophysical measurements rather than relying only on conventional molecular descriptors.

**Role:** first author

**Themes:** Biophysical ML · Thermodynamics · Diagnostics · Molecular Interactions

**Resources:** [Code](https://github.com/the-ahuja-lab/Inertrope)

---

### 07 · Gcoupler *(collaborative)*
**Structure-guided molecular design**

*Can structural information guide the discovery of molecules that modulate protein signalling?*

Gcoupler explores AI-driven structure-based molecular design with applications in GPCR–G-protein signalling and allosteric modulation. The framework combines computational molecular design, graph-based learning, structural information and bioactivity prioritisation.

**Role:** contributing author (collaboration)

**Themes:** Structure-Based Design · Graph Neural Networks · GPCR Signalling · Molecular Design

**Resources:** [Code](https://github.com/the-ahuja-lab/Gcoupler) · [eLife](https://elifesciences.org/reviewed-preprints/106397)

---

## How the Projects Connect

**Represent**

ChemicalDice / CDI — learn richer representations of molecular identity.

↓

**Recognise**

EvOlf · Trojan-Horses · Gcoupler — understand how molecular structure relates to biological recognition and mechanism.

↓

**Reprogram**

SynGlue · MetaboGlue — study molecules that create, stabilise, inhibit or redirect protein interactions.

↓

**Reason**

Biomedical knowledge graphs · pathway models — connect molecular perturbations to larger biological systems.

↓

**Discover**

Develop computational strategies for molecular intervention and biological discovery.

---

## Research Infrastructure

The models above depend on molecular and biological data that are standardised, traceable and evaluation-ready. I therefore maintain a set of lightweight computational-biology tools addressing recurring infrastructure problems.

<p align="center">
  <b>PREPARE</b> &nbsp; → &nbsp; <b>HARMONISE</b> &nbsp; → &nbsp; <b>MAP</b> &nbsp; → &nbsp; <b>SPLIT</b> &nbsp; → &nbsp; <b>STRUCTURE</b> &nbsp; → &nbsp; <b>AUDIT</b>
</p>

**Prepare** — [smiles-cleankit](https://github.com/SaveenaSolanki/smiles-cleankit)
Canonicalise, validate and standardise molecular structures.

**Harmonise** — [assaytablecleaner](https://github.com/SaveenaSolanki/assaytablecleaner)
Standardise bioactivity measurements and derive comparable activity values.

**Map** — [molidmapper](https://github.com/SaveenaSolanki/molidmapper)
Resolve and harmonise molecular and biological identifiers across databases.

**Split** — [scaffoldsplitlab](https://github.com/SaveenaSolanki/scaffoldsplitlab)
Generate leakage-aware molecular machine-learning splits.

**Structure** — [biokg-signmapper](https://github.com/SaveenaSolanki/biokg-signmapper)
Standardise relation semantics in biomedical knowledge graphs.

**Audit** — [kg-stats-audit](https://github.com/SaveenaSolanki/kg-stats-audit)
Inspect graph structure, connectivity and dataset quality.

**Toolkit** — [CompBio Toolkit Suite](https://github.com/SaveenaSolanki/compbio-toolkit-suite)
A common entry point connecting the reusable components.

---

## Open Scientific Software

### SciSVG

[SciSVG](https://github.com/SaveenaSolanki/SciSVG) is an open collection of editable scientific vector graphics designed for figures, presentations and scientific communication.

This project reflects another principle of my work: *scientific outputs should be reusable* — not only scientific models and datasets, but also the tools used to communicate them.

---

## Scientific Questions I Care About

- **Molecular generalisation** — How do molecular models remain useful outside the chemical space on which they were trained?
- **Representation complementarity** — What genuinely new information does one molecular representation contribute beyond another?
- **Interaction biology** — How can small molecules create, stabilise, inhibit or reconfigure protein interactions?
- **Mechanistic machine learning** — Can predictive models provide insight into biological mechanisms rather than producing endpoint scores alone?
- **Biological state** — How can molecular perturbations be linked to pathways, interaction networks and system-level biological consequences?
- **Reproducibility** — How do we turn computational experiments into research systems that another scientist can reproduce and extend?

---

## Computational Focus

Python · PyTorch · RDKit · scikit-learn · pandas · NumPy

Deep Learning · Multimodal Learning · Molecular Representation Learning

Protein–Ligand Modelling · Protein Interaction Modelling

Cheminformatics · Biomedical Knowledge Graphs

Docker · Reproducible Pipelines · Scientific Software

---

## Collaboration

I am interested in collaborations spanning:

- molecular representation learning
- molecular recognition
- protein-interaction modulation
- targeted protein degradation
- molecular glues
- multimodal biological AI
- biomedical knowledge graphs
- computational drug discovery

---

<p align="center">
  <b>Computational Biology · IIIT Delhi</b>
</p>

<p align="center">
  <a href="https://saveenasolanki.github.io/"><img src="https://img.shields.io/badge/Portfolio-saveenasolanki.github.io-17110d?style=for-the-badge&logo=githubpages&logoColor=17110d&labelColor=f5e3ca" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/saveenasolanki/"><img src="https://img.shields.io/badge/LinkedIn-saveenasolanki-17110d?style=for-the-badge&logo=linkedin&logoColor=17110d&labelColor=d4b87a" alt="LinkedIn"></a>
  <a href="mailto:saveenas@iiitd.ac.in"><img src="https://img.shields.io/badge/Email-saveenas%40iiitd.ac.in-17110d?style=for-the-badge&logo=gmail&logoColor=17110d&labelColor=ac946f" alt="Email"></a>
  <a href="https://github.com/SaveenaSolanki"><img src="https://img.shields.io/badge/GitHub-%40SaveenaSolanki-17110d?style=for-the-badge&logo=github&logoColor=17110d&labelColor=e5d8c4" alt="GitHub"></a>
</p>
