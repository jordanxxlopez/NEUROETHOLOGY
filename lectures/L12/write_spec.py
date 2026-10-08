#!/usr/bin/env python3
"""Writes lecture.json for Lecture 12 (kept in Python so references are defined once)."""
import json
from pathlib import Path

R = {
    "land69a": "Land MF (1969a). Structure of the retinae of the principal eyes of jumping spiders (Salticidae: Dendryphantinae) in relation to visual optics. Journal of Experimental Biology 51: 443–470. https://doi.org/10.1242/jeb.51.2.443",
    "land69b": "Land MF (1969b). Movements of the retinae of jumping spiders (Salticidae: Dendryphantinae) in response to visual stimuli. Journal of Experimental Biology 51: 471–493. https://doi.org/10.1242/jeb.51.2.471",
    "land71": "Land MF (1971). Orientation by jumping spiders in the absence of visual feedback. Journal of Experimental Biology 54: 119–139. https://doi.org/10.1242/jeb.54.1.119",
    "land72": "Land MF (1972). Stepping movements made by jumping spiders during turns mediated by the lateral eyes. Journal of Experimental Biology 57: 15–40. https://doi.org/10.1242/jeb.57.1.15",
    "land72c": "Land MF (1972). Mechanisms of orientation and pattern recognition by jumping spiders (Salticidae). In: Wehner R (ed.), Information Processing in the Visual Systems of Arthropods. Springer, Berlin, pp. 231–247. https://doi.org/10.1007/978-3-642-65477-0_34",
    "land85": "Land MF (1985). Fields of view of the eyes of primitive jumping spiders. Journal of Experimental Biology 119: 381–384. https://doi.org/10.1242/jeb.119.1.381",
    "wm80": "Williams DS, McIntyre P (1980). The principal eyes of a jumping spider have a telephoto component. Nature 288: 578–580. https://doi.org/10.1038/288578a0",
    "devoe75": "DeVoe RD (1975). Ultraviolet and green receptors in principal eyes of jumping spiders. Journal of General Physiology 66: 193–207. https://doi.org/10.1085/jgp.66.2.193",
    "blest81": "Blest AD, Hardie RC, McIntyre P, Williams DS (1981). The spectral sensitivities of identified receptors and the function of retinal tiering in the principal eyes of a jumping spider. Journal of Comparative Physiology A 145: 227–239. https://doi.org/10.1007/BF00605035",
    "koyanagi08": "Koyanagi M, Nagata T, Katoh K, Yamashita S, Tokunaga F (2008). Molecular evolution of arthropod color vision deduced from multiple opsin genes of jumping spiders. Journal of Molecular Evolution 66: 130–137. https://doi.org/10.1007/s00239-008-9065-9",
    "nagata12": "Nagata T, Koyanagi M, Tsukamoto H, Saeki S, Isono K, Shichida Y, Tokunaga F, Kinoshita M, Arikawa K, Terakita A (2012). Depth perception from image defocus in a jumping spider. Science 335: 469–471. https://doi.org/10.1126/science.1211667",
    "zurek15": "Zurek DB, Cronin TW, Taylor LA, Byrne K, Sullivan MLG, Morehouse NI (2015). Spectral filtering enables trichromatic vision in colorful jumping spiders. Current Biology 25: R403–R404. https://doi.org/10.1016/j.cub.2015.03.033",
    "zurek10": "Zurek DB, Taylor AJ, Evans CS, Nelson XJ (2010). The role of the anterior lateral eyes in the vision-based behaviour of jumping spiders. Journal of Experimental Biology 213: 2372–2378. https://doi.org/10.1242/jeb.042382",
    "zn12a": "Zurek DB, Nelson XJ (2012a). Hyperacute motion detection by the lateral eyes of jumping spiders. Vision Research 66: 26–30. https://doi.org/10.1016/j.visres.2012.06.011",
    "zn12b": "Zurek DB, Nelson XJ (2012b). Saccadic tracking of targets mediated by the anterior-lateral eyes of jumping spiders. Journal of Comparative Physiology A 198: 411–417. https://doi.org/10.1007/s00359-012-0719-0",
    "duelli78": "Duelli P (1978). Movement detection in the posterolateral eyes of jumping spiders (Evarcha arcuata, Salticidae). Journal of Comparative Physiology 124: 15–26. https://doi.org/10.1007/BF00656387",
    "jakob18": "Jakob EM, Long SM, Harland DP, Jackson RR, Carey A, Searles ME, Porter AH, Canavesi C, Rolland JP (2018). Lateral eyes direct principal eyes as jumping spiders track objects. Current Biology 28: R1092–R1093. https://doi.org/10.1016/j.cub.2018.07.065",
    "bruce21": "Bruce M, Daye D, Long SM, Winsor AM, Menda G, Hoy RR, Jakob EM (2021). Attention and distraction in the modular visual system of a jumping spider. Journal of Experimental Biology 224: jeb231035. https://doi.org/10.1242/jeb.231035",
    "loconsole24": "Loconsole M, Ferrante F, Giacomazzi D, De Agrò M (2024). Independence and synergy of spatial attention in the two visual systems of jumping spiders. Journal of Experimental Biology 227: jeb246199. https://doi.org/10.1242/jeb.246199",
    "sb93": "Strausfeld NJ, Barth FG (1993). Two visual systems in one brain: neuropils serving the secondary eyes of the spider Cupiennius salei. Journal of Comparative Neurology 328: 43–62. https://doi.org/10.1002/cne.903280104",
    "swb93": "Strausfeld NJ, Weltzien P, Barth FG (1993). Two visual systems in one brain: neuropils serving the principal eyes of the spider Cupiennius salei. Journal of Comparative Neurology 328: 63–75. https://doi.org/10.1002/cne.903280105",
    "steinhoff20": "Steinhoff POM, Uhl G, Harzsch S, Sombke A (2020). Visual pathways in the brain of the jumping spider Marpissa muscosa. Journal of Comparative Neurology 528: 1883–1902. https://doi.org/10.1002/cne.24861",
    "menda14": "Menda G, Shamble PS, Nitzany EI, Golden JR, Hoy RR (2014). Visual perception in the brain of a jumping spider. Current Biology 24: 2580–2585. https://doi.org/10.1016/j.cub.2014.09.029",
    "deagro21": "De Agrò M, Rößler DC, Kim K, Shamble PS (2021). Perception of biological motion by jumping spiders. PLoS Biology 19: e3001172. https://doi.org/10.1371/journal.pbio.3001172",
    "dolev14": "Dolev Y, Nelson XJ (2014). Innate pattern recognition and categorization in a jumping spider. PLoS ONE 9: e97819. https://doi.org/10.1371/journal.pone.0097819",
    "harland99": "Harland DP, Jackson RR, Macnab AM (1999). Distances at which jumping spiders (Araneae: Salticidae) distinguish between prey and conspecific rivals. Journal of Zoology 247: 357–364. https://doi.org/10.1111/j.1469-7998.1999.tb00998.x",
    "tj97": "Tarsitano MS, Jackson RR (1997). Araneophagic jumping spiders discriminate between detour routes that do and do not lead to prey. Animal Behaviour 53: 257–266. https://doi.org/10.1006/anbe.1996.0372",
    "pb59": "Parry DA, Brown RHJ (1959). The jumping mechanism of salticid spiders. Journal of Experimental Biology 36: 654–664. https://doi.org/10.1242/jeb.36.4.654",
    "nabawy18": "Nabawy MRA, Sivalingam G, Garwood RJ, Crowther WJ, Sellers WI (2018). Energy and time optimal trajectories in exploratory jumps of the spider Phidippus regius. Scientific Reports 8: 7142. https://doi.org/10.1038/s41598-018-25227-9",
    "forster77": "Forster LM (1977). A qualitative analysis of hunting behaviour in jumping spiders (Araneae: Salticidae). New Zealand Journal of Zoology 4: 51–62. https://doi.org/10.1080/03014223.1977.9517936",
    "cerveira19": "Cerveira AM, Jackson RR, Nelson XJ (2019). Dim-light vision in jumping spiders (Araneae, Salticidae): identification of prey and rivals. Journal of Experimental Biology 222: jeb198069. https://doi.org/10.1242/jeb.198069",
    "cerveira21": "Cerveira AM, Nelson XJ, Jackson RR (2021). Spatial acuity–sensitivity trade-off in the principal eyes of a jumping spider: possible adaptations to a ‘blended’ lifestyle. Journal of Comparative Physiology A 207: 437–448. https://doi.org/10.1007/s00359-021-01486-2",
    "gote19": "Goté JT, Butler PM, Zurek DB, Buschbeck EK, Morehouse NI (2019). Growing tiny eyes: how juvenile jumping spiders retain high visual performance in the face of size limitations and developmental constraints. Vision Research 160: 24–36. https://doi.org/10.1016/j.visres.2019.04.006",
    "rossler22": "Rößler DC, Kim K, De Agrò M, Jordan A, Galizia CG, Shamble PS (2022). Regularly occurring bouts of retinal movements suggest an REM sleep–like state in jumping spiders. Proceedings of the National Academy of Sciences USA 119: e2204754119. https://doi.org/10.1073/pnas.2204754119",
    "elias03": "Elias DO, Mason AC, Maddison WP, Hoy RR (2003). Seismic signals in a courting male jumping spider (Araneae: Salticidae). Journal of Experimental Biology 206: 4029–4039. https://doi.org/10.1242/jeb.00634",
    "govardovskii00": "Govardovskii VI, Fyhrquist N, Reuter T, Kuzmin DG, Donner K (2000). In search of the visual pigment template. Visual Neuroscience 17: 509–528. https://doi.org/10.1017/S0952523800174036",
}


def fig(path, caption):
    return {"path": f"figures/{path}", "caption": caption}


S = []


def add(title, body, cite, refs, layout="text", **kw):
    d = {"layout": layout, "title": title, "body": body, "cite": cite, "refs": [R[r] for r in refs]}
    d.update(kw)
    S.append(d)


# ------------------------------------------------------------------ behavior
add("Salticids hunt by sight rather than by web",
    ["Jumping spiders (family **Salticidae**) are cursorial predators: they locate, approach, and capture prey by walking and leaping, not by waiting in a web. Most species are only a few millimeters long, yet they respond to prey, rivals, and mates many body lengths away.",
     "Their visual system is **modular**. Eight eyes are divided into one forward-facing pair of **principal eyes** (the anterior median eyes, AMEs) and three pairs of **secondary eyes** (anterior lateral, posterior median, and posterior lateral eyes: ALEs, PMEs, PLEs). Each eye type has a distinct optical design and a distinct behavioral role.",
     "Land’s experiments on Californian salticids in 1969 established the central questions: how a camera-type eye only a fraction of a millimeter across reaches high spatial acuity, and how a narrow, movable retina is directed to the right part of the scene. Both questions connect optics, motor control, and neural selection of targets."],
    "Land (1969a, 1969b); Forster (1977)", ["land69a", "land69b", "forster77"])

add("Predatory behavior follows a structured sequence", [
    "Forster divided salticid hunting into three **response patterns**, each built from recognizable motor elements. **Orientation** comprises alerting, swiveling the body toward the stimulus, and aligning the principal eyes with it. **Pursuit** comprises following, running, and stalking. **Capture** comprises a pre-crouch, a crouch, and the jump.",
    "The sequence is not a fixed chain. Distance to the prey determines which pattern is expressed: a nearby target may be captured after a brief stalk, whereas a distant one requires extended pursuit.",
    "Before jumping, many salticids attach a silk **dragline** to the substrate. The line acts as a safety tether if the jump misses and can be used to brake during approach.",
    "Each element provides a measurable behavioral output, such as turn angle or jump distance, that later experiments relate to specific eyes and neural pathways."],
    "Forster (1977)", ["forster77"], layout="figure-right", figure_width=5.4,
    figure=fig("f01_hunt_sequence.png", "Hunting sequence of salticids: response patterns and their motor elements. Diagram drawn from the classification in Forster (1977)."))

add("Two eye systems divide the visual field", [
    "The **secondary eyes** together cover almost the entire horizon around the spider. The ALEs face forward with a field of roughly ±50° and overlap the field of the principal eyes; the PLEs extend coverage to the sides and rear.",
    "The **principal eyes** see a far smaller region. Each retina is a narrow vertical strip, about 20° tall but only about 1° wide at its center, so at any instant it samples a thin slice of the scene. Because the retina can be moved, the principal eyes can survey a forward region of roughly 60°.",
    "This arrangement separates **detection** from **inspection**. Wide-field secondary eyes detect that something has moved; the principal eyes then examine what it is. The division predicts that disabling one eye type should impair one stage of behavior while sparing the other, a prediction tested on later slides."],
    "Land (1985); Zurek & Nelson (2012a)", ["land85", "zn12a", "land69a"], layout="figure-right", figure_width=4.6,
    figure=fig("f02_fields_of_view.png", "Schematic top view of the visual fields. ALE field (±50°) from Zurek & Nelson (2012a); secondary-eye coverage and principal-eye scanning from Land (1985) and Land (1969b)."))

add("Secondary eyes sample space coarsely but widely", [
    "Land measured the angular spacing between neighboring receptors (the **interreceptor angle**) in the secondary eyes of _Portia_. The spacing sets the finest pattern an eye can resolve: two points closer than about one interreceptor angle fall on the same receptor.",
    "Values were about 0.55–0.97° for the ALEs, almost exactly 1.0° for the PMEs, and about 1.49° for the PLEs. These are coarse compared with the principal eyes, whose best resolution is about 0.04–0.1°.",
    "Coarse sampling is compatible with the main secondary-eye task. Detecting that an object has moved, and where, does not require resolving its shape. The principal eyes trade field of view for acuity; the secondary eyes make the opposite trade.",
    "Salticid secondary eyes have **inverted** retinas and, unlike those of many other spiders, lack a reflective **tapetum**, a layer that returns unabsorbed light through the receptors."],
    "Land (1985)", ["land85"], layout="figure-right", figure_width=5.4,
    figure=fig("f03_receptor_spacing.png", "Angular sampling of salticid eyes. Values re-plotted from Land (1985), Land (1969a; minimum spacing 11 arcmin) and Cerveira et al. (2021; 12.4 arcmin)."))

# ------------------------------------------------------------------ optics
add("The principal eye is a movable telescope tube", [
    "Each principal eye consists of a fixed **corneal lens** in the carapace, a long tube, and a retina at the tube’s rear. The lens does not move; the tube and retina do. Changing the position of the retina changes which part of the lens image falls on the receptors.",
    "Land’s anatomical work showed that the retina contains **four layers (tiers)** of receptors arranged one behind another along the path of light. The two deepest layers, 1 and 2, cover the whole retina and contain the highest receptor density.",
    "At the front of the retina lies a **pit**, a concave depression whose refractive boundary acts as a second, diverging lens. This element is the basis of the telephoto arrangement described on the next slide.",
    "A camera eye forms one continuous image through one lens, as in vertebrates. The insect compound eye studied in Lecture 11 instead divides the image among many separate optical units, each with its own lens."],
    "Land (1969a); Williams & McIntyre (1980)", ["land69a", "wm80"], layout="figure-right", figure_width=5.4,
    figure=fig("f04_principal_eye.png", "Schematic of the salticid principal eye: corneal lens, movable tube, pit, and four-tiered retina. Drawn from the descriptions in Land (1969a) and Williams & McIntyre (1980)."))

add("A diverging pit adds a telephoto component", [
    "**Spatial acuity** depends on how large the image is relative to the spacing of receptors. A longer **focal length** spreads a given visual angle over more retinal distance, so more receptors sample it.",
    "Williams and McIntyre showed that the pit in front of the retina acts as a negative (diverging) lens. Combined with the positive corneal lens, it forms a **telephoto system**, the arrangement of a Galilean telescope, that magnifies the image formed by the cornea before it reaches the receptors.",
    "The effective focal length therefore exceeds the physical length of the eye tube. This explains how an eye with a lens only a fraction of a millimeter wide can achieve angular resolution comparable to much larger eyes.",
    "The design has a cost. Magnification spreads light over more receptors and narrows the field of view, which is one reason the retina must be moved to inspect a scene."],
    "Williams & McIntyre (1980)", ["wm80"], layout="figure-right", figure_width=5.4,
    figure=fig("f05_telephoto.png", "Ray diagram of a converging lens followed by a diverging element. Thin-lens schematic illustrating the telephoto principle reported by Williams & McIntyre (1980); not to scale."))

add("Receptor spacing sets the limit of resolution", [
    "Land measured a minimum center-to-center receptor separation of 1.7 µm in the principal retina, corresponding to about 11 arcmin of visual angle in the species he examined. Later work on other salticids reported principal-eye resolution as fine as 0.04°, about 2.4 arcmin, with the telephoto component included.",
    "These values make the principal eyes among the most acute known for an eye of their size. Resolution is limited by two factors: the spacing of receptors and the blur imposed by **diffraction**, the spreading of light that passes through a small aperture.",
    "Acuity varies with ecology. _Cyrba algerina_ hunts under stones in dim light; its principal eyes have a short focal length and wide paired receptors that pool light. Their acuity is 12.4 arcmin, coarser than that of bright-light species, with higher **sensitivity**.",
    "Acuity and sensitivity therefore trade off within the same optical design. Small eyes cannot maximize both."],
    "Land (1969a); Cerveira et al. (2021)", ["land69a", "land85", "cerveira21"])

add("Four tiers raise a question about wavelength and focus", [
    "A lens with **chromatic aberration** brings different wavelengths into focus at different distances behind it: short wavelengths focus closer to the lens, long wavelengths farther away. Land proposed that the tiered retina exploits this property.",
    "From the optics, he calculated that for blue-green light the best image of distant objects falls on layer 2, whereas layer 1 is focused on a plane about 2 cm in front of the animal. For red light, layer 1 would be focused at infinity.",
    "He therefore predicted pigment differences among tiers: red-sensitive receptors in layer 1, blue-green in layer 2, and violet–ultraviolet in layer 3. This was a hypothesis derived from geometry, not a measurement of receptor sensitivity.",
    "Later intracellular recordings and opsin studies tested the prediction directly. Part of it held, layered spectral sensitivity, and part did not, red receptors in layer 1, as the following slides show."],
    "Land (1969a)", ["land69a"], layout="figure-right", figure_width=5.4,
    figure=fig("f07_conjugate_planes.png", "Object planes calculated to be in focus on layers 1 and 2. Values from Land (1969a); schematic axis, not to scale."))

add("Intracellular recordings found UV and green receptors", [
    "DeVoe recorded intracellularly from photoreceptors in the principal eyes of _Phidippus_ and measured each cell’s **spectral sensitivity**, the relative response to equal-energy flashes across wavelengths.",
    "Three response classes appeared. **UV cells** peaked at about 370 nm. **Green cells** were well fit by visual-pigment templates peaking at 532 nm. A third class showed two peaks, near 370 and 525 nm.",
    "A visual pigment absorbs light over a broad band, so one receptor class cannot distinguish wavelength from intensity. Discriminating color requires comparing at least two classes with different spectral sensitivities.",
    "The data established ultraviolet and green channels in the principal eyes. They did not show which tier each cell belonged to, because the recording electrode does not reveal the cell’s depth in the retina without separate marking."],
    "DeVoe (1975)", ["devoe75", "govardovskii00"], layout="figure-right", figure_width=5.6,
    figure=fig("f08_devoe_spectral.png", "Spectral classes reported by DeVoe (1975). Curves are standard visual-pigment templates (Govardovskii et al. 2000) drawn at the reported peak wavelengths, not recorded traces."))

add("Identified receptors link tiers to spectral classes", [
    "Blest and colleagues combined intracellular recording with dye marking to identify the tier of each recorded receptor. Green cells peaked at about 520 nm and UV cells at about 360 nm, close to DeVoe’s values.",
    "Molecular work in _Hasarius adansoni_ later localized green-sensitive opsin to layers 1 and 2 and ultraviolet-sensitive opsin to the more distal layers 3 and 4. Layer 1 therefore does not contain the red-sensitive pigment Land predicted.",
    "Land’s geometric reasoning about focal planes remained useful, but the pigment assignment changed. The layered design reflects both wavelength sensitivity and focus, without the specific red channel his model proposed.",
    "The result shows how an optical model generates testable predictions, and how direct measurement of identified cells is required to confirm them."],
    "Blest et al. (1981); Koyanagi et al. (2008); Nagata et al. (2012)", ["blest81", "koyanagi08", "nagata12", "land69a"],
    layout="figure-right", figure_width=5.6,
    figure=fig("f06_retina_tiers.png", "Pigment predicted for each tier by Land (1969a) compared with later spectral and opsin evidence in Hasarius adansoni (Koyanagi et al. 2008; Nagata et al. 2012). Summary table, not original data."))

add("Opsin genes define the spectral channels", [
    "An **opsin** is the protein part of a visual pigment. It binds a chromophore (a retinal derivative) whose photoisomerization activates the receptor. The amino-acid sequence of the opsin tunes the wavelength of peak absorption.",
    "Koyanagi and colleagues cloned opsin genes from _Hasarius adansoni_. Later work assigned a green-sensitive opsin (**Rh1**), a blue-sensitive opsin (**Rh2**), and ultraviolet-sensitive opsins (**Rh3**, **Rh4**). Rh1 is expressed in most eyes; most eyes use two opsins, in combinations that differ by eye type.",
    "Reports differ on where Rh2 is expressed. Immunolabeling studies have placed it in few or no principal-eye receptors, so its contribution to principal-eye color vision remains uncertain.",
    "Like insect photoreceptors, spider photoreceptors are **rhabdomeric**: the pigment sits in stacks of microvilli, and light depolarizes the receptor. The intracellular steps of the spider cascade have been studied far less than those of _Drosophila_."],
    "Koyanagi et al. (2008); Nagata et al. (2012)", ["koyanagi08", "nagata12"], layout="figure-right", figure_width=5.6,
    figure=fig("f26_opsins.png", "Salticid opsins and their reported locations, summarized from Koyanagi et al. (2008) and Nagata et al. (2012). Summary table, not original data."))

add("Layer 2 receives a deliberately defocused image", [
    "Nagata and colleagues found that receptors in both layer 1 and layer 2 of _Hasarius adansoni_ contain the same green-sensitive pigment. Because of chromatic aberration, green light is focused sharply only on layer 1.",
    "Layer 2 therefore always receives a blurred version of the green image. The amount of blur depends on the distance to the object: the object’s image plane shifts as it approaches, changing the blur on layer 2 relative to layer 1.",
    "Comparing a sharp image with a defocused image of the same scene provides **depth from defocus**, a monocular cue to **absolute distance**. It requires neither two eyes nor movement of the head.",
    "The anatomy alone does not prove the brain performs this comparison. The authors tested it behaviorally by manipulating the wavelength of light and measuring the accuracy of the jumps."],
    "Nagata et al. (2012)", ["nagata12"], layout="figure-right", figure_width=5.4,
    figure=fig("f09_defocus.png", "Schematic of the defocus mechanism: green light focused on layer 1 and blurred on layer 2. Drawn from the model described in Nagata et al. (2012); not to scale."))

add("Changing the color of light shortens the jump", [
    "Nagata and colleagues covered all but one principal eye and filmed spiders jumping at prey under **monochromatic** green or red illumination. With only one principal eye uncovered, **binocular disparity**, the difference between the two eyes’ views, was unavailable.",
    "Under green light the spiders jumped accurately. Under red light they consistently undershot, landing short of the prey.",
    "Red light has a longer focal length in the same lens. A target viewed in red produces the layer-2 blur that a closer target would produce in green. If the spider computes distance from a green-calibrated blur relation, it will underestimate distance in red, exactly as observed.",
    "A mathematical model of the eye’s optics predicted the direction of the error. The experiment supports defocus as a distance cue; it does not exclude other cues, such as motion parallax, being used under natural conditions."],
    "Nagata et al. (2012)", ["nagata12"], layout="figure-right", figure_width=5.4,
    figure=fig("f10_red_green.png", "Logic of the green–red test: identical targets, different predicted blur, accurate versus short jumps. Schematic summarizing results in Nagata et al. (2012); arc lengths illustrative."))

add("A retinal filter adds a red channel in Habronattus", [
    "Most salticid principal eyes have ultraviolet and green receptors and therefore cannot distinguish red from green. Males of _Habronattus pyrrithrix_, however, display red and orange ornaments during courtship.",
    "Zurek and colleagues found a ruby-red **filter pigment** in a restricted region of tier 1. Light passing through the filter reaches green-pigment receptors only at long wavelengths, shifting their effective peak from about 530 nm to a reported 626 nm.",
    "The filtered receptors form a third spectral class, making color vision **trichromatic** without a new opsin. The mechanism changes the light reaching a receptor rather than the receptor’s pigment.",
    "Because the filter covers only part of the retina, red information is available only where the filtered region points. The authors proposed that the spider must scan a scene to accumulate color information, an idea that links color vision to the retinal movements described next."],
    "Zurek et al. (2015)", ["zurek15", "govardovskii00"], layout="figure-right", figure_width=5.4,
    figure=fig("f11_red_filter.png", "Spectral shift produced by the tier-1 filter in Habronattus pyrrithrix. Peak values from Zurek et al. (2015); curves are pigment templates (Govardovskii et al. 2000), not measured spectra."))

add("Courtship signals combine vision and vibration", [
    "Color vision matters most in salticid social behavior. Males court females with leg waving, body postures, and colored ornaments presented within the female’s principal-eye field.",
    "Elias and colleagues used video and **laser vibrometry**, a non-contact measurement of surface vibration, to record courtship in _Habronattus dossenus_. Each prominent visual display was followed by a seismic signal transmitted through the substrate: thumps, scrapes, or buzzes.",
    "Ablation separated the mechanisms. Preventing abdominal movement silenced seismic signals without changing the visual display; blocking contact between abdomen and cephalothorax silenced thumps and scrapes but not buzzes. At least three mechanisms generate the vibrations.",
    "Visual and seismic components are tightly timed but separately produced. Female choice depends on both, so the principal-eye system is studied within a **multimodal** signaling context."],
    "Elias et al. (2003)", ["elias03"])

# ------------------------------------------------------------------ movement
add("Six muscles move each principal retina", [
    "Land showed that each principal-eye tube is moved by **six muscles**. Four attach the tube to the carapace and translate the retina side to side and up and down. Two thin bands encircle the tube and **rotate** it, twisting the retina about the visual axis.",
    "The nerve supplying these muscles contains only six motor axons, one terminating in each muscle. The full repertoire of retinal movements is therefore produced by six motor neurons per eye.",
    "Because the corneal lens is fixed, moving the retina shifts which part of the lens image is sampled. A spider can redirect its gaze without moving its body or head.",
    "Movements of the two eyes are usually **conjugate**: both retinae move together in the same direction. Conjugacy implies common central control of the two motor pools."],
    "Land (1969b)", ["land69b"], layout="figure-right", figure_width=5.4,
    figure=fig("f12_muscles.png", "Schematic of the principal-eye muscles: four translators and two torsion bands, six motor axons. Muscle positions simplified; drawn from Land (1969b)."))

add("Land identified four kinds of retinal movement", [
    "By viewing the retinae through the eye’s own optics with an ophthalmoscope while presenting stimuli, Land distinguished four movement types. **Spontaneous activity** is variable, periodic side-to-side motion without an obvious stimulus.",
    "**Saccades** are rapid shifts that bring the central region of the retina onto a target. They can be triggered by a small dark spot appearing in, or moving within, the field of a principal eye or of the ALEs.",
    "**Tracking** keeps the central region on a target as it moves. **Scanning** is a slower, structured movement across a stationary target, combining lateral oscillation with rotation.",
    "Saccades driven by the ALEs show that the secondary eyes can direct the principal retinae even when the principal eyes have not yet seen the target. This interaction between the two eye systems is the basis of later experiments with eye tracking and masking."],
    "Land (1969b)", ["land69b"], layout="table", text_height=2.85,
    table={"header": ["Movement", "Trigger", "Function proposed"],
           "rows": [["Spontaneous", "none apparent", "maintains sampling of the field"],
                    ["Saccade", "small spot in AME or ALE field", "centers the target"],
                    ["Tracking", "moving target", "holds the target centrally"],
                    ["Scanning", "stationary target", "pattern analysis"]]})

add("Scanning combines oscillation and rotation", [
    "During scanning, the retinae fixate a stimulus with their central region and move laterally back and forth across it at about 0.5–1 Hz, a period of 1–2 s. At the same time both retinae shift together more slowly, at about 0.1–0.2 Hz, and rotate about the visual axis.",
    "Rotation changes the orientation of the narrow retina relative to edges in the image. Lateral oscillation sweeps the receptor strip across the stimulus, producing relative motion between receptors and a stationary object.",
    "Reports of the amplitude of rotation differ between the original paper and later summaries. The temporal structure is well established; precise angular values should be checked against Land’s original measurements before being used quantitatively."],
    "Land (1969b); Land (1972)", ["land69b", "land72c"], layout="figure-right", figure_width=5.4,
    figure=fig("f13_scan_frequencies.png", "Frequencies of the two scanning components. Values re-plotted from Land (1969b) and Land (1972, chapter); periods computed from the frequencies."))

add("Scanning was proposed as a means of feature analysis", [
    "Land proposed that rotation aligns the long axis of the retina with lines or edges in the image, and that lateral oscillation moves edge-detecting receptors across those features. The retina would then sample orientation and position in sequence rather than all at once.",
    "The hypothesis fits salticid recognition behavior. Conspecifics are identified partly by the angle and arrangement of their legs, and a strip-shaped retina that rotates could match its orientation to leg segments.",
    "The proposal remains an interpretation. Land showed that scanning occurs and described its structure; he did not record neurons whose activity depends on retinal orientation relative to an edge.",
    "Modern eye trackers that present controlled shapes while recording retinal position now allow the idea to be tested quantitatively. Such studies ask which image features attract the central retina and how long it dwells on them."],
    "Land (1969b); Land (1972)", ["land69b", "land72c"])

add("The ophthalmoscope made retinal movement visible", [
    "Land observed the principal retinae with an **ophthalmoscope**, viewing the retina through the eye’s own optics. The retina reflects enough light to be seen through the lens, so its position can be followed directly.",
    "Modern versions use **infrared** illumination, which passes through the cuticle and is invisible to the spider. A beam splitter allows a visible stimulus and the infrared retinal image to share one optical axis, so stimulus position can be expressed in retinal coordinates.",
    "The spider is **tethered**: its carapace is fixed so the eyes stay in the camera’s field. Leg movements remain possible, and a sphere or ball beneath the legs can record attempted turns.",
    "Tethering changes behavior. A turn that would normally bring a target into view has no visual consequence, an **open-loop** condition in which the spider’s actions do not alter what it sees."],
    "Land (1969b); Jakob et al. (2018)", ["land69b", "jakob18"], layout="figure-right", figure_width=5.6,
    figure=fig("f14_eyetracker.png", "Schematic of an infrared eye tracker for jumping spiders, after the system described in Jakob et al. (2018). Components simplified."))

# ------------------------------------------------------------------ secondary eyes & orientation
add("ALE input alone can trigger orienting and stalking", [
    "Zurek and colleagues covered every eye except the ALEs and presented computer-generated dots to tethered spiders, varying dot size, contrast, and speed. The measured output was an **orienting turn**, a body rotation that would bring the target in front of the principal eyes.",
    "All three parameters affected the probability of turning. The most effective stimulus was a 4° dot at 40% contrast moving at 9°/s. Females responded more readily than males.",
    "With tethered flies as prey, ALE input alone was sufficient to elicit stalking. Detection and the initial approach therefore do not require the principal eyes.",
    "Because the principal eyes were covered, these turns cannot reflect recognition by the principal eyes. They show what the ALE pathway can initiate by itself, not that it acts alone in an intact animal."],
    "Zurek et al. (2010)", ["zurek10"], layout="figure-right", figure_width=5.4,
    figure=fig("f25_zurek_optimum.png", "Most effective dot parameters for ALE-mediated orienting. Values from Zurek et al. (2010)."))

add("Lateral eyes detect displacements finer than their mosaic", [
    "Zurek and Nelson presented small target displacements to the ALEs of tethered spiders and measured orienting saccades. Spiders responded to displacements roughly ten times smaller than the ALE interreceptor angle.",
    "Such performance is **hyperacuity**: detecting a change in position more finely than the receptor spacing. A displacement smaller than one receptor still alters how light is shared between neighboring receptors, and comparing their responses can reveal that change.",
    "Hyperacuity therefore depends on the overlap of receptor acceptance angles and on neural comparison between neighbors. It does not mean the ALEs can resolve fine spatial patterns; resolving two separate points remains limited by receptor spacing.",
    "Females again responded to lower contrast than males, consistent with the sex difference in the earlier orienting study."],
    "Zurek & Nelson (2012a); Land (1985)", ["zn12a", "land85"], layout="figure-right", figure_width=5.4,
    figure=fig("f24_hyperacuity.png", "Receptor spacing compared with the displacement the ALEs can detect. Ratio from Zurek & Nelson (2012a); spacing from Land (1985); schematic."))

add("ALEs steer the body with saccade-like turns", [
    "In a related study, Zurek and Nelson recorded spiders on a freely rotating ball while targets moved through the ALE field. Stimuli elicited a series of whole-body **saccades**, rapid discrete turns whose magnitude matched the target’s position.",
    "The ball moves opposite to the spider’s intended rotation, providing a continuous record of attempted turning. A spider that steps to turn left rotates the ball to the right.",
    "Smooth pursuit by the principal eyes was guided by the ALEs. Target position signaled by the secondary eyes sets the size of the body turn and directs the principal retinae.",
    "The result connects the ALE pathway to two motor outputs: rotation of the body by the legs and movement of the principal retinae by their six muscles."],
    "Zurek & Nelson (2012b)", ["zn12b"])

add("Turns are planned from the first sighting", [
    "Land fixed spiders by the carapace and allowed them to hold a light paper ring with their legs. When a target appeared in a lateral eye’s field, the spider stepped as if turning and rotated the ring instead of its body.",
    "Because the eyes never moved, the stimulus stayed in the same retinal position throughout the turn. Any accuracy in the turn had to come from information available at the first sighting.",
    "Ring rotation closely matched the turn required to face the target. Land concluded that the initial position of the image on a lateral eye sets the size of the turn, an **open-loop** command executed without visual feedback.",
    "Turn control therefore resembles a **ballistic** movement: a motor program is selected from the sensory input and then carried out, rather than continuously corrected while the spider turns."],
    "Land (1971)", ["land71"], layout="figure-right", figure_width=5.2,
    figure=fig("f23_ring.png", "Ring paradigm: the carapace is fixed and the legs rotate a light ring. Schematic drawn from the method described in Land (1971) and Land (1972, chapter)."))

add("Stepping patterns implement the turn", [
    "In a companion study, Land filmed the leg movements that produce turns triggered by the lateral eyes. Turning toward a target is a translation of a retinal position into a motor command distributed across eight legs: the lateral eye provides the angle, and leg circuits produce the rotation.",
    "Later work on salticid turning on a rotating ball relies on Land’s analysis. The ball’s low moment of inertia means it does not alter the orientation turn, so ball rotation can serve as a read-out of the intended turn.",
    "A similar transformation occurs in many visually guided animals. Image position on a sensory map is converted into a motor output of matching size, as when a toad orients toward prey before snapping, a mapping examined in Lectures 9 and 10.",
    "The neural circuitry for this transformation in salticids, from lateral-eye neuropils to leg motor neurons, has not been identified cell by cell."],
    "Land (1972); Zurek & Nelson (2012b)", ["land72", "zn12b"])

add("Posterolateral eyes respond to objects, not wide-field motion", [
    "Duelli tested the PLEs of _Evarcha arcuata_. A single moving object in the PLE field evoked an accurate turn of the prosoma, the front body section that carries the eyes, which brought the object into the principal-eye field.",
    "Moving stripe patterns did not elicit **optomotor** responses, and random patterns of moving squares did not elicit turning. The PLE pathway responded selectively to a single object, not to motion distributed across the whole field.",
    "By progressively thinning out a random square pattern, Duelli determined the conditions under which several simultaneous stimuli suppressed turning.",
    "The contrast with flies (Lecture 11) is instructive. Fly wide-field neurons drive compensatory turning in response to whole-field rotation; salticid lateral eyes instead select individual targets for inspection."],
    "Duelli (1978)", ["duelli78"], layout="table", text_height=3.25,
    table={"header": ["Stimulus to PLE", "Response", "Interpretation"],
           "rows": [["Single moving object", "accurate prosoma turn", "target localization"],
                    ["Moving stripes", "no optomotor turning", "no wide-field response"],
                    ["Random moving squares", "turning suppressed", "multiple targets inhibit"]]})

add("Lateral eyes direct the principal eyes during tracking", [
    "Jakob and colleagues used an infrared eye tracker to record principal-retina position in tethered _Phidippus audax_ females while presenting moving disks (3, 4, or 5° in diameter; 2.77, 7.60, or 15.13°/s) and stationary objects.",
    "The ALEs were then covered with removable paint. Each spider served as its own control, contributing one mean value per stimulus with the ALEs open and with them masked.",
    "Principal eyes scanned stationary objects whether or not the ALEs were masked. Smooth tracking of moving disks occurred only when the ALEs were open; with them masked, a stimulus had to appear directly in front of the principal eyes before it was explored.",
    "Masking demonstrates that ALE input is **necessary** for tracking. It does not identify the neurons that carry ALE information to the principal-eye motor system."],
    "Jakob et al. (2018)", ["jakob18"], layout="figure-right", figure_width=5.6,
    figure=fig("f15_jakob_matrix.png", "Design and outcome of the ALE-masking experiment. Stimulus values and qualitative outcomes from Jakob et al. (2018); summary diagram, not original data."))

add("Primary targets reduce distraction", [
    "Bruce and colleagues asked whether the ALEs redirect the principal eyes whenever something appears. While a spider viewed a primary stimulus with its principal eyes, a distractor oval appeared in the ALE field, and the eye tracker recorded whether the principal retinae moved to it.",
    "Spiders shifted their gaze to the distractor significantly less often when the primary stimulus was a cricket than when it was a different stimulus.",
    "Gaze shifts therefore depend on the properties of both stimuli. The authors interpreted this as evidence for higher-order control of principal-eye attention, a process that weighs the current target against a new one.",
    "**Attention** here is defined operationally as selective allocation of the principal eyes. The experiment measures behavior; it does not identify the neural basis of the selection."],
    "Bruce et al. (2021)", ["bruce21"], layout="figure-right", figure_width=5.4,
    figure=fig("f16_bruce.png", "Distractor paradigm. Schematic of the design and main result in Bruce et al. (2021)."))

add("ALEs alone mediate responses to looming", [
    "In a second experiment, Bruce and colleagues presented a black circle that rapidly expanded (**looming**) or contracted (**receding**). Looming mimics an approaching object; receding provides a control with the same edges moving inward.",
    "Intact spiders and spiders with masked principal eyes were significantly more likely to back away from a looming stimulus than spiders with masked ALEs.",
    "The authors concluded that, for objects in front of the spider, the ALEs alone mediate the looming response. Defensive withdrawal does not require identifying the object.",
    "Looming detection also appeared in the amphibian avoidance circuits of Lecture 10. In salticids, the same secondary eyes that select prey for inspection also trigger escape from an approaching object."],
    "Bruce et al. (2021)", ["bruce21"], layout="table", text_height=3.0,
    table={"header": ["Condition", "Backing away from looming", "Inference"],
           "rows": [["Intact", "frequent", "normal defensive response"],
                    ["Principal eyes masked", "frequent", "AMEs not required"],
                    ["ALEs masked", "significantly reduced", "ALEs required"]]})

add("Attention is allocated separately in each eye system", [
    "Loconsole and colleagues used a cue–target design. A spatial cue appeared on one side of a screen; a target dot moving vertically then appeared either on the same side or on the opposite side.",
    "One experiment tested whether a cue presented to the secondary eyes enhanced principal-eye responses on the cued side. A second tested whether the direction of principal-eye focus enhanced secondary-eye detection on that side.",
    "In both experiments spiders detected targets faster and more accurately on the side opposite the cue. The hypothesis that both eye systems attend jointly to one location was not supported.",
    "The authors proposed that attention is segregated across the eye systems, with each covering locations the other is not attending. This is an interpretation of behavioral performance; the underlying neural mechanism is unknown."],
    "Loconsole et al. (2024)", ["loconsole24"], layout="figure-right", figure_width=5.4,
    figure=fig("f17_loconsole.png", "Cue–target design and main result. Schematic summarizing Loconsole et al. (2024)."))

# ------------------------------------------------------------------ neural
add("Two visual pathways reach separate brain centers", [
    "In the wandering spider _Cupiennius salei_, Strausfeld and Barth traced the principal and secondary eyes into the brain. Secondary-eye photoreceptors project to three laminae, then to separate medullae, and converge on a single neuropil called the **mushroom body**.",
    "Principal-eye axons pass through successive neuropils to a midline structure then called the central body, now generally termed the **arcuate body**. A **neuropil** is a dense region of axons, dendrites, and synapses.",
    "Steinhoff and colleagues found the same principal-eye connectivity in the jumping spider _Marpissa muscosa_. Each secondary eye has its own first-order neuropil, and secondary-eye pathways reach the mushroom body.",
    "Neither the spider mushroom body nor the arcuate body is established as homologous to the similarly named structures in insects. Shared names do not imply shared evolutionary origin."],
    "Strausfeld & Barth (1993); Steinhoff et al. (2020)", ["sb93", "swb93", "steinhoff20"], layout="figure-right", figure_width=5.6,
    figure=fig("f18_brain_pathways.png", "Simplified wiring of the principal- and secondary-eye pathways in Marpissa muscosa. Diagram drawn from Steinhoff et al. (2020) and Strausfeld & Barth (1993)."))

add("A shared second-order neuropil links lateral eyes", [
    "In _Marpissa muscosa_, the first-order neuropils of the ALEs and PLEs each connect to their own second-order neuropil and also to an additional shared second-order neuropil, termed **L2**.",
    "Steinhoff and colleagues proposed that L2 acts as an upstream integration center. Combining forward-facing ALE input with lateral PLE input early in processing could support faster movement decisions, such as choosing the direction of a turn.",
    "The posterior median eyes differ. Their first-order neuropils project directly to the arcuate body rather than through second-order neuropils, which led the authors to suggest that the PMEs do not contribute to motion detection.",
    "These conclusions are based on neuroanatomy: tracing, staining, and three-dimensional reconstruction. Functional roles proposed for L2 and the PMEs have not yet been tested with recordings or targeted lesions."],
    "Steinhoff et al. (2020)", ["steinhoff20"])

add("Recording from a pressurized brain", [
    "Spiders extend their legs partly by **hydraulic pressure** in the body fluid. Opening the cuticle wide enough for conventional electrophysiology lets fluid escape, and for decades this prevented recordings from the salticid brain.",
    "Menda and colleagues made a very small opening that the spider’s own tissues sealed around a hair-thin tungsten microelectrode. The preparation kept the animal alive while extracellular spikes were recorded from visual brain regions of _Phidippus audax_.",
    "They reported single-unit recordings from visual interneurons in a jumping spider brain, the first published. Stimuli included white noise and images of flies and other jumping spiders.",
    "**Single-unit** recording isolates the spikes of one neuron from background activity. It identifies response properties but not the cell’s morphology unless the neuron is also filled with dye."],
    "Menda et al. (2014)", ["menda14"])

add("Visual neurons combine input from several eyes", [
    "When only one eye type viewed a stimulus, responses in the recorded visual regions were weak. The same image evoked stronger activity when several eye types viewed it together, evidence of **nonlinear interactions** between eyes: the response to combined input could not be predicted by adding the responses to each eye alone.",
    "Responses to a small, moving, prey-like target were strong and consistent across trials. Spikes became linked to the stimulus within a window of about 80–160 ms after onset.",
    "The recordings show that principal- and secondary-eye information converges on single neurons somewhere in the visual system. They do not yet establish where, or whether this convergence underlies the tracking and attention effects measured behaviorally."],
    "Menda et al. (2014)", ["menda14"], layout="figure-right", figure_width=5.4,
    figure=fig("f19_menda_latency.png", "Time window in which spiking became linked to the prey-like stimulus. Values from Menda et al. (2014); schematic timeline, not a recorded trace."))

# ------------------------------------------------------------------ cognition-level behavior
add("Spiders discriminate biological motion with secondary eyes", [
    "De Agrò and colleagues presented **point-light displays** to the secondary eyes of _Menemerus semilimbatus_. These displays show only dots placed on the joints of a moving animal; shape is absent, but the coordinated motion of the dots specifies a living walker.",
    "Spiders stood on a sphere and chose between displays on either side. The comparisons were biological motion versus random dot motion, and biological motion versus scrambled displays that preserve local dot trajectories but not their arrangement.",
    "Spiders discriminated biological from random motion but turned preferentially toward the random display. They showed no preference between biological and scrambled displays.",
    "Discrimination shows that the secondary-eye pathway extracts more than the presence of motion. The direction of the preference is unexplained; the authors did not propose a confirmed functional reason for it."],
    "De Agrò et al. (2021)", ["deagro21"], layout="figure-right", figure_width=5.4,
    figure=fig("f20_biomotion.png", "Comparisons and outcomes in the point-light experiment. Summary of De Agrò et al. (2021); not original data."))

add("Innate recognition of prey uses local features", [
    "_Evarcha culicivora_ preferentially captures blood-fed _Anopheles_ mosquitoes, the vectors of human malaria. The spiders recognize this prey by its distinctive resting posture and engorged abdomen.",
    "Dolev and Nelson presented lures in which body parts were rearranged or separated. Spiders identified _Anopheles_ correctly from the angle formed between discontinuous elements, even when those elements were not connected as in a real mosquito.",
    "This angle, rather than the overall resting posture, was the key cue. The authors concluded that recognition relies on **local feature processing**, combining specific elements, rather than on a holistic representation of the whole body.",
    "Because the spiders were reared without experience of the prey, the preference is innate. Recognition criteria of this kind constrain which features the principal eyes must extract during scanning."],
    "Dolev & Nelson (2014)", ["dolev14"])

add("Discrimination distance varies across species", [
    "Harland and colleagues tested adult males of 37 salticid species. Each spider walked up a ramp toward either a mirror, which shows a rival, or a prey insect in a transparent dish. Spiders displayed only to mirrors, never to insects.",
    "The distance at which display began was taken as the distance at which a species can tell rivals from prey. Lyssomanines and spartaeines generally had shorter distances than salticines, but _Portia_ species matched the longest salticine distances; the longest of all belonged to _Mogrus neglectus_.",
    "Discrimination distance is a behavioral estimate of principal-eye performance under natural viewing. It integrates optics, receptor spacing, and recognition criteria in one measure.",
    "Comparative data of this kind show that acuity evolves with lineage and lifestyle, not as a fixed property of the salticid eye plan."],
    "Harland et al. (1999)", ["harland99"])

add("Portia selects detour routes that lead to prey", [
    "_Portia_ is **araneophagic**: it preys on other spiders, often in webs it cannot approach directly. Reaching such prey frequently requires a **detour**, an indirect route that temporarily leads away from the target.",
    "Tarsitano and Jackson let _Portia_ view two possible routes, only one of which led to a prey lure. Spiders chose the correct route more often than the incorrect one.",
    "During many detours the prey is out of view. Selecting and completing the correct route therefore requires using information gathered by the principal eyes before departure.",
    "The study demonstrates route discrimination from visual inspection. How the route is represented in the spider’s brain, and whether this represents planning in the sense used for vertebrates, remain open questions."],
    "Tarsitano & Jackson (1997)", ["tj97"])

# ------------------------------------------------------------------ motor, development, state
add("The jump: hydraulics or muscle", [
    "Parry and Brown estimated pressures in the leg joints of _Sitticus pubescens_ before a jump: 65.3–144.0 kPa at the femur–patella joint and 17.3–46.7 kPa at the tibia–metatarsus joint of leg IV. Because spider legs lack extensor muscles at some joints, they concluded that hydraulic pressure extends the legs.",
    "Nabawy and colleagues filmed trained _Phidippus regius_ with high-speed cameras. Take-off velocity ranged from 0.52 to 0.97 m/s, and time to take-off from 18.1 to 31.6 ms.",
    "From these measurements they calculated that leg muscle could supply the required power, so hydraulic augmentation may be present but is not energetically essential. Short jumps used low trajectories that minimized flight time; long jumps used steeper angles near the energetic optimum.",
    "The two studies differ in species, method, and inference, so they illustrate competing explanations rather than a settled answer."],
    "Parry & Brown (1959); Nabawy et al. (2018)", ["pb59", "nabawy18"], layout="figure-right", figure_width=4.9,
    figure=fig("f21_jump.png", "Joint pressures (Parry & Brown 1959) and take-off kinematics (Nabawy et al. 2018). Ranges re-plotted from the values reported in each paper."))

add("Small eyes trade sensitivity for acuity", [
    "Small eyes collect little light. Cerveira and colleagues tested whether _Cyrba algerina_ and _C. ocellata_, which hunt under stones, can identify prey and rivals in dim light.",
    "Both species performed proficiently at 234 and 1.35 cd/m². At 0.54 cd/m² only a minority succeeded, and at 0.24 cd/m² none did. Performance therefore failed over a narrow range of luminance.",
    "The principal eyes of _C. algerina_ have a short focal length and wide paired receptors that pool light, raising sensitivity at the cost of acuity (12.4 arcmin).",
    "**Luminance** measures the light reaching the eye from a surface, in candelas per square meter."],
    "Cerveira et al. (2019, 2021)", ["cerveira19", "cerveira21"], layout="figure-right", figure_width=5.4,
    figure=fig("f22_dim_light.png", "Prey and rival identification at four luminances. Values from Cerveira et al. (2019), re-plotted on a log scale."))

add("Juveniles keep adult acuity with small eyes", [
    "Goté and colleagues measured the ALEs of _Phidippus audax_ from early juveniles to adults using morphology, histology, ophthalmoscopy, and optical measurements.",
    "Juveniles have proportionally larger lenses for their body size. As the eyes grow, lens focal length increases together with retinal size, so ALE spatial acuity and field of view stay nearly constant across life stages.",
    "Photoreceptor number does not change during growth. Early in life the receptors are narrow, elongated cylinders packed into a small space, which keeps receptor spacing fine but reduces rhabdom volume and therefore light capture.",
    "Young spiders therefore see with near-adult acuity but lower sensitivity. The authors predicted that juveniles should be most limited in visually demanding tasks under low light, a prediction that remains to be tested."],
    "Goté et al. (2019)", ["gote19"])

add("Retinal movements reveal an REM sleep–like state", [
    "Rößler and colleagues filmed 34 juvenile _Evarcha arcuata_ overnight with infrared video. Juvenile cuticle is thin enough that the principal retinae can be seen moving inside the eye tubes.",
    "During nocturnal rest, spiders showed regular bouts of retinal movement. Each bout was accompanied by twitching of single limbs or spinnerets and by stereotyped leg curling, and bouts lengthened as the night progressed.",
    "The authors proposed an **REM sleep–like state**, defined by analogy with the rapid-eye-movement phase of vertebrate sleep, in a terrestrial invertebrate. Whether these periods constitute sleep depends on showing reduced responsiveness to stimuli during the bouts, which was not established.",
    "The study demonstrates that the six-muscle retinal motor system is active during rest as well as during hunting. It does not demonstrate dreaming or any particular cognitive content during the bouts."],
    "Rößler et al. (2022)", ["rossler22"])

add("Detection and inspection are separated by eye type", [
    "Across these studies, detection and inspection are performed by different eyes. The ALEs detect motion and looming, set the size of body turns, and guide principal-eye tracking. The PLEs localize single objects at the sides.",
    "The principal eyes inspect. Their telephoto optics and fine receptor spacing provide high acuity in a narrow strip; six muscles move that strip in saccades, tracking, and scanning; tiered receptors supply color and depth from defocus.",
    "The two systems project to different brain centers, the mushroom body and the arcuate body, yet single visual neurons respond best when several eye types are stimulated together.",
    "How detection and inspection are coordinated, and where attention is allocated between them, are now the central experimental questions in salticid neuroethology."],
    "Land (1969b); Jakob et al. (2018); Menda et al. (2014)", ["land69b", "jakob18", "menda14", "steinhoff20"],
    layout="table", text_height=2.85,
    table={"header": ["Eye", "Main role", "Key evidence"],
           "rows": [["Principal (AME)", "acuity, color, depth, scanning", "Land 1969; Nagata 2012"],
                    ["Anterior lateral", "motion, looming, guiding AMEs", "Zurek 2010; Jakob 2018"],
                    ["Posterior lateral", "object localization at sides", "Duelli 1978"]]})

add("Methods determine what each conclusion can claim", [
    "Each experimental approach supports a different kind of claim. Optics and anatomy show what an eye **could** resolve; intracellular recordings show what individual receptors **do** respond to; masking shows what an eye is **necessary** for in a given task.",
    "Tethered preparations permit precise stimulus control and eye tracking but remove normal visual feedback. Freely moving animals behave naturally but make retinal position hard to measure.",
    "Opsin localization and spectral recordings can disagree, as in Land’s predicted red receptors and the later discovery that layer 1 is green-sensitive. Agreement among independent methods is strongest when anatomy, physiology, and behavior point to the same mechanism, as for depth from defocus.",
    "The main gap is the neural circuit. Few neurons have been recorded, and none has yet been linked to a specific step in turning, tracking, or scanning."],
    "Land (1969a); Nagata et al. (2012); Jakob et al. (2018); Menda et al. (2014)",
    ["land69a", "nagata12", "jakob18", "menda14"])

assert len(S) == 44, len(S)

TAKEAWAYS = {
    "cite": "Land (1969a, b; 1971); Nagata et al. (2012); Jakob et al. (2018); Steinhoff et al. (2020)",
    "refs": [R[k] for k in ("land69a", "land69b", "land71", "nagata12", "zurek15", "jakob18", "bruce21", "steinhoff20", "menda14")],
    "items": [
        {"lead": "Two eye systems, two jobs.",
         "text": "Secondary eyes (wide field, ~0.5–1.5° spacing) detect and localize movement; principal eyes (narrow, ~0.04–0.1° acuity) inspect identity."},
        {"lead": "Telephoto optics plus a movable retina.",
         "text": "A diverging pit lengthens focal length; six muscles (six axons) translate and rotate a narrow retina in saccades, tracking, and scanning."},
        {"lead": "Tiers give color and depth.",
         "text": "UV (~360–370 nm) and green (~520–532 nm) receptors; green-pigmented layer 2 receives a defocused image that signals absolute distance — red light causes short jumps."},
        {"lead": "ALEs are necessary for tracking and looming.",
         "text": "Masking ALEs abolishes smooth principal-eye tracking but not scanning of still objects, and abolishes backing away from looming stimuli."},
        {"lead": "Turns are open-loop.",
         "text": "Image position on a lateral eye at first sighting sets turn size; the ring experiment shows accurate turns without visual feedback."},
        {"lead": "Separate brain pathways, convergent neurons.",
         "text": "Principal eyes → arcuate body; secondary eyes → mushroom body; recorded neurons respond best to combined input from several eyes."},
    ],
}

spec = {
    "lecture": 12,
    "theme": "cobalt-white",
    "content_slides": 44,
    "slides": S,
    "takeaways": TAKEAWAYS,
}
Path(__file__).with_name("lecture.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))
print("wrote lecture.json with", len(S), "content slides")
