# Lecture 83 plan

Exact title: **Biocomputing III: Animals in virtual worlds: navigation, learning, and adaptive behavior across species**

Date: **Date TBD**. Planned format: title + 44 content slides + six exam-level key takeaways = 46 slides.

The lecture connects navigation, reward-based visual choice, virtual prey capture, altered feedback, intracellular recording, and spatial coding. Experimental virtual tasks are identified as such, rather than described as commercial video games. Species-specific display physiology and active sensory sampling are part of the teaching content.

## Closed-loop worlds across animals

2. Animal action changes the next visual input (stowers).
3. Head tracking preserves the animal’s visual perspective (stowers).
4. Virtual agents interact with real animals (stowers).
5. Scene changes isolate visual causes of behavior (stowers).

## Flies: landmarks, heading, and recalibration

6. A visual landmark anchors the fly’s heading (seelig).
7. Ellipsoid-body activity forms a heading signal (seelig).
8. Self-motion maintains orientation in darkness (seelig).
9. Visual input reaches the heading network (fisher).
10. Experience changes the visual-to-heading mapping (fisher).
11. Virtual feedback exposes sensorimotor recalibration (fisher).

## Honey bees: choices, transfer, and neural activation

12. Walking bees choose rewarded virtual colors (buatois).
13. Active sampling determines the available visual evidence (buatois).
14. Learned choices transfer from screens to a real maze (buatois).
15. Transfer depends on the direction between environments (buatois).
16. Color learning recruits mushroom-body gene expression (geng).
17. Neural activation differs between brain regions (geng).

## Praying mantises: virtual prey and depth

18. Separate eye images create a virtual prey distance (mantis).
19. Binocular disparity changes the decision to strike (mantis).
20. Display design determines the insect’s depth information (mantis).
21. Optic-lobe neurons respond to virtual prey depth (rosner).
22. Spatial tuning connects disparity to prey location (rosner).

## Cockroaches and blowflies: exploration and display physiology

23. Cockroaches explore a projected virtual forest (takalo).
24. Ball motion controls progress through the forest (takalo).
25. Photoreceptors can detect projector flicker (takalo).
26. Visual displays must match the animal’s sensory dynamics (takalo).

## Zebrafish: altered feedback and adaptive motor output

27. Swimming changes the motion of a virtual visual field (portugues).
28. Feedback gain changes the required swimming effort (portugues).
29. Motor adjustments persist across feedback changes (portugues).
30. Fictive swimming permits brain-wide activity recording (ahrens).
31. Different neuronal responses accompany adaptation (ahrens).
32. Anatomical maps locate sensorimotor response classes (ahrens).
33. Olivocerebellar lesions alter adaptive locomotion (ahrens).

## Mice: virtual navigation and intracellular coding

34. Mice run through a controlled virtual corridor (harvey).
35. Place-cell firing depends on virtual location (harvey).
36. Membrane depolarization accompanies a place field (harvey).
37. Theta timing links membrane activity to spatial firing (harvey).
38. Freely moving mice respond to virtual height (stowers).
39. Perspective and movement determine the virtual experience (stowers).

## Rats: two-dimensional worlds and spatial representations

40. Rats rotate and walk through two-dimensional worlds (aronov).
41. Place and head-direction cells engage during navigation (aronov).
42. Grid activity organizes virtual space (aronov).
43. Virtual boundaries recruit spatial responses (aronov).
44. Changing environment shape changes hippocampal coding (aronov).

## Cross-species synthesis

45. Adaptive behavior depends on each animal’s feedback loop (stowers, seelig, buatois, portugues, harvey, aronov).

## Source and build requirements

Ahrens (2012) and Aronov & Tank (2014) PDFs are required before those neural and rat-navigation sections can be finalized. No substitute figures or papers will replace those inaccessible sources. Ten other source PDFs are secured under papers/ (ignored by Git).

All content slides will have 3–5 teaching paragraphs and connected teaching transcripts with full DOI references. At least 40 content slides carry images and at least 34 carry primary-article figures. Original anatomical figures accompany discussion of named structures. Figures remain original crops, with intact axes, units, scales, and panel letters. No generated, redrawn, replotted, or recolored images.

Useful original article recordings will be selected from the cited supplementary materials, embedded with exact identifiers and provenance, and checked for decode, package relationships, and static fallbacks. No YouTube recordings. New unused muted theme, Arial throughout, no em dashes in visible text, and no routine caveat endings.

Build with tools/build_lecture.py; validate with tools/check_lecture.py and review all 46 rendered slides. Record the final theme as used, commit, push, and deliver the complete PPTX.
