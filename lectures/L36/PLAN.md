# Lecture 36 preparation

Exact title: Simple learning circuits: Aplysia gill-withdrawal habituation and sensitization (Kandel)

Exact date: Friday, November 20, 2026

The authoritative default branch was refreshed before preparation (commit recorded in research.json). AGENTS.md, the repository lecture skill, the template, schedule, theme inventory, Lecture 35 preparation and approved reference decks were reviewed. Lectures 8–10 each have 46 slides and images on all 44 content slides. The cloud runtime and onboarding skills were applied; Python presentation/PDF dependencies and native rendering tools are available. No environment configuration change is required.

Status: awaiting the five original PDFs in PAPERS.md. Fifteen other primary PDFs are retained. No lecture spec, deck or scientific image has been created; no theme is marked used. The explicit original-PDF stop rule applies.

## Proposed allocation of 44 content slides

This allocation requires full-source methods, numerical results and figure checks before final prose. It is not a completed lecture.

- 1–4: Aplysia defensive behavior; siphon stimulation and gill withdrawal; habituation versus fatigue or sensory adaptation; recovery, dishabituation and sensitization (Pinsker et al., 1970; Castellucci et al., 1970).
- 5–8: abdominal ganglion and identified sensory/motor cells; monosynaptic and polysynaptic contributions; excitatory postsynaptic potentials; behavioral and intracellular measurements with preparation limits (Castellucci et al., 1970; Antonov et al., 1999).
- 9–12: quantal release, presynaptic reduction and postsynaptic sensitivity; homosynaptic depression; release-site silencing versus vesicle depletion; persistence and recovery controls (Castellucci & Kandel, 1974; Gover et al., 2002).
- 13–15: long-term habituation, spaced training and retention; sensory-neuron varicosities; structural correlates distinguished from causal identification of memory storage (Carew et al., 1972; Bailey & Chen, 1988).
- 16–19: noxious stimulation and heterosynaptic facilitation; serotonin application versus endogenous modulation; cyclic AMP and protein kinase A; potassium-current/action-potential mechanisms only after appropriate primary-source verification (Brunelli et al., 1976; Liu et al., 2004).
- 20–22: kinase regulatory subunits and anchoring; presynaptic signaling localization; fast excitatory transmission and glutamate pharmacology (Liu et al., 2004; Dale & Kandel, 1993).
- 23–26: postsynaptic calcium stores; exocytosis intervention; AMPA-type receptor efficacy; behavioral dishabituation and the limits of a solely presynaptic explanation (Li et al., 2005).
- 27–30: single versus repeated serotonin; short- versus long-term facilitation; macromolecular synthesis timing; persistent monosynaptic enhancement in behaviorally trained animals (Montarolo et al., 1986; Frost et al., 1985).
- 31–34: presynaptic contact growth; CREB-dependent gene expression; synapsin transcription, localization and knockdown controls; consolidation versus immediate facilitation (Bailey & Chen, 1988; Hart et al., 2011).
- 35–38: local translation and ApCPEB4; initiation versus maintenance; neurotrophin isoforms, ApTrk intervention and growth of varicosities (Lee et al., 2016; Kassabov et al., 2013).
- 39–41: CREB1 knockdown and partial rescue; empirical training-protocol outcomes distinguished from computational predictions; no newly plotted/model-derived visual (Zhou et al., 2015).
- 42–44: behavioral/synaptic expression versus latent memory; loss and reinstatement; protein synthesis timing and DNA-methylation intervention limits (Chen et al., 2014; Pearce et al., 2017).

References above are preliminary author-year labels. The verified metadata in research.json takes precedence; every final label must be checked against the source author list. Tail/siphon findings will be explicitly distinguished from gill findings. Cultured sensorimotor facilitation is a cellular analog, not a behavioral measurement. Pharmacological blockade establishes intervention dependence subject to specificity controls; it does not establish a complete circuit. Release-site silencing is a supported explanation, not a direct image of the proposed molecular switch. Structural correlations and recovery after memory-expression disruption require explicit interpretive limits.

## Final build and delivery requirements

After the PDFs arrive, inspect all originals and crop intact published panels with tools/crop_figure.py or tools/crop_panels.py. Add a real animal image on the title slide and published anatomy for named structures. Use images on at least 40 of 44 content slides, with at least 34 primary-paper figure slides; aim for native color on at least half. Preserve axes, units, scale bars, panel letters and original colors.

Write three to five substantial paragraphs per content slide and natural teaching transcripts, verified full DOI references and caption figure/panel IDs. Use Arial, a new unused restrained palette, adjacent figure/text columns, the exact schedule title/date and six bold-led exam takeaways. Build with tools/build_lecture.py, fix all checks, inspect all 46 rendered slides, then record the theme and commit/push the completed deck. Presenton exports will provide newly verified public PPTX/PDF download links and one preview link. No substitute or generated scientific visuals are permitted.

The persistent image restriction is already in AGENTS.md and .claude/skills/neuroethology-lecture/SKILL.md. The reusable lecture request is prompts/make_lecture_36.md.
