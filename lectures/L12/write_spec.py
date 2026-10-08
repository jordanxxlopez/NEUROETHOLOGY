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
add("Salticids hunt by sight rather than by web", [
    "Jumping spiders (family **Salticidae**) are cursorial predators: they locate, approach, and capture prey by walking and leaping, not by waiting in a web. Land worked on _Phidippus johnsoni_ (8–11 mm long) and two _Metaphidippus_ species (4.5–5.5 mm).",
    "Eight eyes are divided into one forward-facing pair of **principal eyes** (anterior median, AM) and three pairs of **secondary eyes** (anterior lateral, AL; posterior median, PM; posterior lateral, PL). Each AM eye sends its axons to its own **first optic glomerulus** behind the eye.",
    "Earlier behavioral work showed that a jumping spider distinguishes prey from potential mates at least ten body lengths away, 5–10 cm. Land calculated that at such distances the image of a fly or a spider covers at most about 100 receptors.",
    "Pattern recognition from so few receptors is the central problem of this lecture: how the eye is built, how the retina is moved, and how the secondary eyes direct it."],
    "Land (1969a, 1969b)", ["land69a", "land69b"], layout="figure-right", figure_width=5.2,
    figure={"path": "figures/p_land69a_fig1.png", "caption": "Land (1969a), Fig. 1. Frontal section of the cephalothorax of Metaphidippus aeneolus: positions of the eyes, the AM retinae and first optic glomeruli, and fields of view in the horizontal plane. Scale bar 200 µm.", "source_url": "https://doi.org/10.1242/jeb.51.2.443"})

add("Predatory behavior follows a structured sequence", [
    "Forster divided salticid hunting into three **response patterns**, each built from recognizable motor elements. **Orientation** comprises alerting, swiveling the body toward the stimulus, and aligning the principal eyes with it. **Pursuit** comprises following, running, and stalking. **Capture** comprises a pre-crouch, a crouch, and the jump.",
    "The sequence is not a fixed chain. Distance to the prey determines which pattern is expressed: a nearby target may be captured after a brief stalk, whereas a distant one requires extended pursuit.",
    "Before jumping, many salticids attach a silk **dragline** to the substrate. The line acts as a safety tether if the jump misses and can be used to brake during approach.",
    "Each element provides a measurable behavioral output, such as turn angle or jump distance, that later experiments relate to specific eyes and neural pathways."],
    "Forster (1977)", ["forster77"])

add("Two eye systems divide the visual field", [
    "The **secondary eyes** together cover almost the entire horizon around the spider. The ALEs face forward with a field of roughly ±50° and overlap the field of the principal eyes; the PLEs extend coverage to the sides and rear.",
    "The **principal eyes** see a far smaller region. Each retina is a narrow vertical strip, about 20° tall but only about 1° wide at its center, so at any instant it samples a thin slice of the scene. Because the retina can be moved, the principal eyes can survey a forward region of roughly 60°.",
    "This arrangement separates **detection** from **inspection**. Wide-field secondary eyes detect that something has moved; the principal eyes then examine what it is. The division predicts that disabling one eye type should impair one stage of behavior while sparing the other, a prediction tested on later slides."],
    "Land (1985); Zurek & Nelson (2012a)", ["land85", "zn12a", "land69a"])

add("Secondary eyes sample space coarsely but widely", [
    "Land measured the angular spacing between neighboring receptors (the **interreceptor angle**) in the secondary eyes of _Portia_. The spacing sets the finest pattern an eye can resolve: two points closer than about one interreceptor angle fall on the same receptor.",
    "Values were about 0.55–0.97° for the ALEs, almost exactly 1.0° for the PMEs, and about 1.49° for the PLEs. These are coarse compared with the principal eyes, whose best resolution is about 0.04–0.1°.",
    "Coarse sampling is compatible with the main secondary-eye task. Detecting that an object has moved, and where, does not require resolving its shape. The principal eyes trade field of view for acuity; the secondary eyes make the opposite trade.",
    "Salticid secondary eyes have **inverted** retinas and, unlike those of many other spiders, lack a reflective **tapetum**, a layer that returns unabsorbed light through the receptors."],
    "Land (1985)", ["land85"])

# ------------------------------------------------------------------ optics
add("The principal eye is a movable telescope tube", [
    "Each principal eye consists of a fixed **corneal lens** in the carapace, a long tube, and a retina at the tube’s rear. The lens does not move; the tube and retina do. Moving the retina changes which part of the lens image falls on the receptors.",
    "Land’s serial sections showed that the retina contains **four layers (tiers)** of receptors arranged one behind another along the path of light. In the section, layer 4 lies most anterior (nearest the lens) and layer 1 deepest; layers 1 and 2 extend over the whole retina, while layers 3 and 4 are confined to its central region.",
    "In layers 1–3 the light-receiving segments are rod-shaped and parallel to the incident light. In layer 4 they are ovoid and lie roughly at right angles to the light, a structural difference Land used to argue that layer 4 does not resolve an image.",
    "At the front of the retina lies a **pit**, a depression that acts optically as a second, diverging lens (next slide)."],
    "Land (1969a)", ["land69a", "wm80"], layout="figure-right", figure_width=4.8,
    figure={"path": "figures/p_land69a_fig3.png", "caption": "Land (1969a), Fig. 3. Frontal section through the right AM retina of M. aeneolus near its centre, showing the four receptor layers (1–4). Scale bar 20 µm; light enters from the top.", "source_url": "https://doi.org/10.1242/jeb.51.2.443"})

add("A diverging pit adds a telephoto component", [
    "**Spatial acuity** depends on how large the image is relative to receptor spacing. A longer **focal length** spreads a given visual angle over more retinal distance, so more receptors sample it.",
    "Land measured the lens curvatures, refractive indices, and focal lengths of every eye. His scale diagrams show the AM image formed far behind the lens, at roughly the depth of the head, whereas the AL and PL eyes form images only a short distance behind theirs. In _M. aeneolus_ the AM focal length is 512 µm.",
    "Williams and McIntyre later showed that the pit in front of the AM retina acts as a negative (diverging) lens. Combined with the positive corneal lens, it forms a **telephoto system** that magnifies the image before it reaches the receptors, raising the effective focal length beyond the physical length of the tube.",
    "Magnification narrows the field of view, which is why the retina must be moved to inspect a scene."],
    "Land (1969a); Williams & McIntyre (1980)", ["land69a", "wm80"], layout="figure-right", figure_width=5.0,
    figure={"path": "figures/p_land69a_fig10.png", "caption": "Land (1969a), Fig. 10. Scale optical diagrams of the AM, AL and PL eyes of M. aeneolus (top) and P. johnsoni (bottom): lens curvatures, nodal points (N), aperture stops (A) and image positions. Scale bar 500 µm.", "source_url": "https://doi.org/10.1242/jeb.51.2.443"})

add("Receptor spacing sets the limit of resolution", [
    "Land reconstructed every receptor ending in the right AM retina of _P. johnsoni_ from serial sections. Layers 1 and 2 form long, curved strips; layers 3 and 4 occupy only a small central patch.",
    "Receptors are packed most densely at the centre of layers 1 and 2. The minimum separation is 1.7 µm, which, with a 512 µm focal length, corresponds to about 11 arcmin (0.18°) of visual angle.",
    "A **receptor mosaic** sets the finest pattern an eye can resolve: two points closer than about one receptor separation fall on the same receptor. Later work that included the telephoto component reported principal-eye resolution as fine as 0.04°.",
    "The high-acuity centre is tiny. Zurek and colleagues summarize it as covering less than 1° and containing no more than a few hundred receptors, which is why the retina must be moved over a target."],
    "Land (1969a); Zurek et al. (2010)", ["land69a", "zurek10"], layout="figure-right", figure_width=5.2,
    figure={"path": "figures/p_land69a_fig5.png", "caption": "Land (1969a), Fig. 5. Reconstruction of the right AM retina of P. johnsoni from serial sections: receptor endings in layer 1, layer 2, and layers 3 (filled) and 4 (open). Crosses are fiducial marks; angular scale 2°.", "source_url": "https://doi.org/10.1242/jeb.51.2.443"})

add("Four tiers raise a question about wavelength and focus", [
    "Land combined ophthalmoscopy with his optical measurements to find which object distance is focused on each layer. For blue-green light, distant objects are imaged on layer 2; layer 1 is conjugate with a plane about 2 cm in front of the animal (left panel, distance scale in cm).",
    "Because the lens has **chromatic aberration**, red light focuses farther back: for red, layer 1 is conjugate with infinity (right panel, B, G, R).",
    "He proposed two hypotheses: layers examine objects at different distances, or each layer receives the sharpest image for a different wavelength. He favoured the second and predicted red-sensitive receptors in layer 1, blue-green in layer 2, and violet–ultraviolet in layer 3. Layer 4, conjugate with no plane in front of the spider, he suggested might analyse skylight polarization.",
    "These were predictions from optics; later recordings tested them."],
    "Land (1969a)", ["land69a"], layout="figure-right", figure_width=4.6,
    figure={"path": "figures/c_land69a_fig12_13.png", "caption": "Land (1969a), Figs 12 (top) and 13 (bottom). Top: image positions in blue-green light for objects at different distances (cm, outer scales) relative to the four layers, P. johnsoni (left) and M. aeneolus (right). Bottom: image positions for distant objects in blue (B), green (G) and red (R) light.", "source_url": "https://doi.org/10.1242/jeb.51.2.443"})
add("Intracellular recordings found UV and green receptors", [
    "DeVoe recorded intracellularly from photoreceptors in the principal eyes of _Phidippus_ and measured each cell’s **spectral sensitivity**, the relative response to equal-energy flashes across wavelengths.",
    "Three response classes appeared. **UV cells** peaked at about 370 nm. **Green cells** were well fit by visual-pigment templates peaking at 532 nm. A third class showed two peaks, near 370 and 525 nm.",
    "A visual pigment absorbs light over a broad band, so one receptor class cannot distinguish wavelength from intensity. Discriminating color requires comparing at least two classes with different spectral sensitivities.",
    "The data established ultraviolet and green channels in the principal eyes. They did not show which tier each cell belonged to, because the recording electrode does not reveal the cell’s depth in the retina without separate marking."],
    "DeVoe (1975)", ["devoe75", "govardovskii00"])

add("Identified receptors link tiers to spectral classes", [
    "Blest and colleagues combined intracellular recording with dye marking to identify the tier of each recorded receptor. Green cells peaked at about 520 nm and UV cells at about 360 nm, close to DeVoe’s values.",
    "Molecular work in _Hasarius adansoni_ later localized green-sensitive opsin to layers 1 and 2 and ultraviolet-sensitive opsin to the more distal layers 3 and 4. Layer 1 therefore does not contain the red-sensitive pigment Land predicted.",
    "Land’s geometric reasoning about focal planes remained useful, but the pigment assignment changed. The layered design reflects both wavelength sensitivity and focus, without the specific red channel his model proposed.",
    "The result shows how an optical model generates testable predictions, and how direct measurement of identified cells is required to confirm them."],
    "Blest et al. (1981); Koyanagi et al. (2008); Nagata et al. (2012)", ["blest81", "koyanagi08", "nagata12", "land69a"])

add("Opsin genes define the spectral channels", [
    "An **opsin** is the protein part of a visual pigment. It binds a chromophore (a retinal derivative) whose photoisomerization activates the receptor. The amino-acid sequence of the opsin tunes the wavelength of peak absorption.",
    "Koyanagi and colleagues cloned opsin genes from _Hasarius adansoni_. Later work assigned a green-sensitive opsin (**Rh1**), a blue-sensitive opsin (**Rh2**), and ultraviolet-sensitive opsins (**Rh3**, **Rh4**). Rh1 is expressed in most eyes; most eyes use two opsins, in combinations that differ by eye type.",
    "Reports differ on where Rh2 is expressed. Immunolabeling studies have placed it in few or no principal-eye receptors, so its contribution to principal-eye color vision remains uncertain.",
    "Like insect photoreceptors, spider photoreceptors are **rhabdomeric**: the pigment sits in stacks of microvilli, and light depolarizes the receptor. The intracellular steps of the spider cascade have been studied far less than those of _Drosophila_."],
    "Koyanagi et al. (2008); Nagata et al. (2012)", ["koyanagi08", "nagata12"])

add("Layer 2 receives a deliberately defocused image", [
    "Nagata and colleagues found that receptors in both layer 1 and layer 2 of _Hasarius adansoni_ contain the same green-sensitive pigment. Because of chromatic aberration, green light is focused sharply only on layer 1.",
    "Layer 2 therefore always receives a blurred version of the green image. The amount of blur depends on the distance to the object: the object’s image plane shifts as it approaches, changing the blur on layer 2 relative to layer 1.",
    "Comparing a sharp image with a defocused image of the same scene provides **depth from defocus**, a monocular cue to **absolute distance**. It requires neither two eyes nor movement of the head.",
    "The anatomy alone does not prove the brain performs this comparison. The authors tested it behaviorally by manipulating the wavelength of light and measuring the accuracy of the jumps."],
    "Nagata et al. (2012)", ["nagata12"])

add("Changing the color of light shortens the jump", [
    "Nagata and colleagues covered all but one principal eye and filmed spiders jumping at prey under **monochromatic** green or red illumination. With only one principal eye uncovered, **binocular disparity**, the difference between the two eyes’ views, was unavailable.",
    "Under green light the spiders jumped accurately. Under red light they consistently undershot, landing short of the prey.",
    "Red light has a longer focal length in the same lens. A target viewed in red produces the layer-2 blur that a closer target would produce in green. If the spider computes distance from a green-calibrated blur relation, it will underestimate distance in red, exactly as observed.",
    "A mathematical model of the eye’s optics predicted the direction of the error. The experiment supports defocus as a distance cue; it does not exclude other cues, such as motion parallax, being used under natural conditions."],
    "Nagata et al. (2012)", ["nagata12"])

add("A retinal filter adds a red channel in Habronattus", [
    "Most salticid principal eyes have ultraviolet and green receptors and therefore cannot distinguish red from green. Males of _Habronattus pyrrithrix_, however, display red and orange ornaments during courtship.",
    "Zurek and colleagues found a ruby-red **filter pigment** in a restricted region of tier 1. Light passing through the filter reaches green-pigment receptors only at long wavelengths, shifting their effective peak from about 530 nm to a reported 626 nm.",
    "The filtered receptors form a third spectral class, making color vision **trichromatic** without a new opsin. The mechanism changes the light reaching a receptor rather than the receptor’s pigment.",
    "Because the filter covers only part of the retina, red information is available only where the filtered region points. The authors proposed that the spider must scan a scene to accumulate color information, an idea that links color vision to the retinal movements described next."],
    "Zurek et al. (2015)", ["zurek15", "govardovskii00"])

add("Courtship signals combine vision and vibration", [
    "Color vision matters most in salticid social behavior. Males court females with leg waving, body postures, and colored ornaments presented within the female’s principal-eye field.",
    "Elias and colleagues used video and **laser vibrometry**, a non-contact measurement of surface vibration, to record courtship in _Habronattus dossenus_. Each prominent visual display was followed by a seismic signal transmitted through the substrate: thumps, scrapes, or buzzes.",
    "Ablation separated the mechanisms. Preventing abdominal movement silenced seismic signals without changing the visual display; blocking contact between abdomen and cephalothorax silenced thumps and scrapes but not buzzes. At least three mechanisms generate the vibrations.",
    "Visual and seismic components are tightly timed but separately produced. Female choice depends on both, so the principal-eye system is studied within a **multimodal** signaling context."],
    "Elias et al. (2003)", ["elias03"])

# ------------------------------------------------------------------ movement
add("Six muscles move each principal retina", [
    "Land reconstructed the eye muscles of _M. aeneolus_ from serial sections. Four muscles attach the AM eye tube to the carapace and displace the retina side to side and up and down. Two thin bands encircle the tube and twist it, rotating the retina about the visual axis (**torsion**).",
    "The oculomotor nerve to each eye contains only six axons, and each axon ends in one of the six muscles (right panel, numbered 1–6). The full repertoire of retinal movement is therefore driven by six motor neurons per eye.",
    "Because the corneal lens is fixed, moving the retina shifts which part of the lens image is sampled; gaze changes without moving the body. Movements of the two eyes are usually **conjugate**, implying common central control of both motor pools."],
    "Land (1969b)", ["land69b"], layout="figure-right", figure_width=6.0,
    figure={"path": "figures/c_land69b_fig2_4.png", "caption": "Land (1969b), Text-figs 2 and 4. Left: muscles of the left AM eye of M. aeneolus seen from above (1–6; bar 100 µm). Right: paths of the six axons of the oculomotor nerve, with transverse sections of the nerve.", "source_url": "https://doi.org/10.1242/jeb.51.2.471"})
add("Land identified four kinds of retinal movement", [
    "**Spontaneous activity**: bouts of side-to-side movement lasting 1–10 min, with excursions up to 45–50°, frequencies from just above 1 Hz to about 0.05 Hz, and velocities of 2–100°/s. It occurs whether or not anything is in view.",
    "**Saccades**: a small target (e.g. a 3° dot) appearing in the field of an AM or AL eye moves both retinae so their centres land on it. Saccades of 15° are complete within 0.1 s and were not seen to overshoot. Without scanning, the retinae hold the target for 1–2 s and drift back over 10–15 s.",
    "**Tracking**: once acquired, a target moving at under 10°/s is followed smoothly over at least 25°.",
    "**Scanning**: after a saccade the retinae oscillate across a stationary target while rotating (next slides)."],
    "Land (1969b)", ["land69b"], layout="figure-right", figure_width=4.6,
    figure={"path": "figures/p_land69b_fig11.png", "caption": "Land (1969b), Text-fig. 11. The four kinds of eye movement: (i) spontaneous activity, (ii) saccades, (iii) tracking, (iv) scanning. Open arrows: retinal movements; solid arrow: stimulus movement (black square).", "source_url": "https://doi.org/10.1242/jeb.51.2.471"})

add("Scanning combines oscillation and rotation", [
    "During scanning the retinae stay locked on the target while moving side to side across it with a period of 1–2 s. At the same time both retinae rotate in the same sense, 20–30° clockwise and then 20–30° anticlockwise, a full torsion cycle of 40–50°.",
    "The torsion period lengthens during a bout, from 5–8 s for the first cycle to about 15 s by the fourth or fifth. In each cycle the retinae hold one extreme for 2–5 s, then take about 2 s to rotate to the other.",
    "Bouts lasted 5–94 s, mostly 20–40 s. Horizontal oscillation, torsion, and fixation all start and stop together, which indicates a single coordinated motor program rather than three independent movements.",
    "Repeated presentation of the same 3° dot every minute produced progressively shorter bouts until only the initial saccade remained."],
    "Land (1969b)", ["land69b"], layout="figure-right", figure_width=5.6,
    figure={"path": "figures/p_land69b_fig8.png", "caption": "Land (1969b), Text-fig. 8. (a) Movements of the retinal fields during scanning. (b) Horizontal (upper) and torsional (lower) record of a long scanning bout after a 3° stimulus. Scale: 10° horizontal, 50° torsion, 10 s. Male M. harfordi.", "source_url": "https://doi.org/10.1242/jeb.51.2.471"})

add("Scan amplitude follows target width", [
    "Land varied the width of the target from 1.4° to 12.3°. For targets narrower than about 10°, the amplitude of horizontal scanning almost exactly matched the target’s width; it never fell below 2°, even for a 0.5° target.",
    "Scan period changed much less. In _M. harfordi_ each cycle lasted 1.1–1.3 s for targets of 2° or less and 2.0–2.4 s for 11–12° targets: period changed by a factor of 2 while amplitude changed by a factor of 5.",
    "That mismatch rules out the simplest mechanism, a retina moving at constant speed until it meets an edge and then reversing. Scan amplitude and period were unaffected by target height, and torsion was unaffected by target width.",
    "The retina therefore measures the horizontal extent of the target and adjusts its sweep to it, a form of active sensing."],
    "Land (1969b)", ["land69b"], layout="figure-right", figure_width=4.8,
    figure={"path": "figures/p_land69b_fig9.png", "caption": "Land (1969b), Text-fig. 9. Scanning records for targets 1.4°, 4.1°, 7.0°, 9.2° and 12.3° wide: horizontal (upper) and torsional (lower) traces. Scale: 10° horizontal, 50° torsion, 10 s. Adult female M. harfordi.", "source_url": "https://doi.org/10.1242/jeb.51.2.471"})

add("Scanning was proposed as a means of feature analysis", [
    "Drees had found that male _Epiblemum_ court a dark dot only when it carries oblique ‘legs’; the proportion of trials evoking courtship rose from 17% to 85% as leg-like lines were added (left panel). Simple shapes without legs were treated as prey.",
    "Land proposed that each retina contains rows of receptors acting as **line detectors**. Torsion would align the rows at fixed inclinations (about 25° each side of vertical), and horizontal oscillation would sweep them across a stationary contour (right panel). In a resting _P. johnsoni_ many leg contours lie at 25–30° to the vertical.",
    "He listed the problems himself: spiders recognise targets rotated by 90° or 180°, and real leg angles vary from 10° to 45°. No neuron with these properties has been recorded, so the scheme remains a hypothesis."],
    "Land (1969b)", ["land69b"], layout="two-figures", text_height=2.7,
    figures=[{"path": "figures/p_land69b_fig12.png", "caption": "Land (1969b), Text-fig. 12, after Drees (1952). (a) Stimuli evoking courtship, with % of trials; (b) stimuli evoking prey capture.", "source_url": "https://doi.org/10.1242/jeb.51.2.471"},
             {"path": "figures/p_land69b_fig13.png", "caption": "Land (1969b), Text-fig. 13a. Proposed function of scanning: torsion aligns receptor rows (black dots) with contours; horizontal movement sweeps them across the target.", "source_url": "https://doi.org/10.1242/jeb.51.2.471"}])

add("The ophthalmoscope made retinal movement visible", [
    "Land built an **ophthalmoscope** with two light paths sharing one microscope objective, separated by a beam splitter. One path projected targets onto the retina within a uniform 29° field; the other let the observer see the retina through the spider’s own lens.",
    "Only layer 4 of the AM retina reflects light well, so its outline (right panel) was used to infer the position of the whole retina. Field luminance was about 10⁴ cd/m², similar to a white surface in diffuse sunlight.",
    "Spiders were held by a card waxed to the carapace while holding a light card ring they could walk around without moving the body. Horizontal and torsional movements were recorded by keeping a graticule line aligned with the retinal images.",
    "The modern infrared eye tracker used by Jakob and colleagues is built on the same principle."],
    "Land (1969b)", ["land69b", "jakob18"], layout="figure-right", figure_width=6.0,
    figure={"path": "figures/c_land69b_fig1_plate.png", "caption": "Land (1969b), Text-fig. 1 and Plate 1. Left: optical diagram of the ophthalmoscope and the recording device. Right: AM retinae of P. johnsoni seen through the ophthalmoscope (layer 4 visible, outline dashed; bar 5°) and a section at the level of the retinae (bar 50 µm).", "source_url": "https://doi.org/10.1242/jeb.51.2.471"})
# ------------------------------------------------------------------ secondary eyes & orientation
add("ALE input alone can trigger orienting and stalking", [
    "Zurek and colleagues tested 52 _Servaea vestita_ (26 females, 26 males) with every eye except the AL eyes covered. Computer-generated dark dots varying in size (0.5–8°), contrast (1–40%) and speed (1–81°/s) moved across a screen, and the response scored was an **orienting turn**.",
    "Size, contrast, and speed all had significant effects, with a significant three-way interaction. The most effective dot (4°, 40% contrast, 9°/s) produced turns on 90% of presentations (propensity 0.9). The lowest contrast that evoked any turns was 1% (propensity 0.008).",
    "With tethered flies on a ramp, spiders using only their AL eyes still stalked and attacked. Detection and the approach do not require the principal eyes.",
    "These results show what the AL pathway can do alone; they do not show that it acts alone in an intact spider."],
    "Zurek et al. (2010)", ["zurek10"], layout="figure-right", figure_width=5.0,
    figure={"path": "figures/p_zurek10_fig2.png", "caption": "Zurek et al. (2010), Fig. 2. Orientation propensity (colour, 0–0.9) as a function of dot size, speed and contrast, all eyes except the AL eyes covered.", "source_url": "https://doi.org/10.1242/jeb.042382"})

add("Hunger and sex change how readily ALEs trigger turns", [
    "Half of the spiders in each sex were tested the day after feeding and half after a week without food. Overall orientation propensity was 0.263 in females and 0.176 in males, and 0.255 in hungry versus 0.185 in sated spiders (both P < 0.0005).",
    "Hunger raised responsiveness similarly in both sexes (no sex × hunger interaction). Females were more responsive in both states: 0.226 versus 0.142 when sated and 0.305 versus 0.206 when hungry.",
    "In ramp trials, hungry females stalked flies more often than sated females (9 versus 2 of 22; Fisher’s exact P = 0.015); males changed little.",
    "The same visual stimulus therefore produces different behavioral probabilities depending on internal state. Motivation acts on the decision to orient, after detection."],
    "Zurek et al. (2010)", ["zurek10"], layout="figure-right", figure_width=4.4,
    figure={"path": "figures/p_zurek10_fig3.png", "caption": "Zurek et al. (2010), Fig. 3. Overall orientation propensity (mean ± s.e.m.) of females (black) and males (grey), sated versus hungry, all eyes except the AL eyes covered.", "source_url": "https://doi.org/10.1242/jeb.042382"})
add("Lateral eyes detect displacements finer than their mosaic", [
    "Zurek and Nelson presented small target displacements to the ALEs of tethered spiders and measured orienting saccades. Spiders responded to displacements roughly ten times smaller than the ALE interreceptor angle.",
    "Such performance is **hyperacuity**: detecting a change in position more finely than the receptor spacing. A displacement smaller than one receptor still alters how light is shared between neighboring receptors, and comparing their responses can reveal that change.",
    "Hyperacuity therefore depends on the overlap of receptor acceptance angles and on neural comparison between neighbors. It does not mean the ALEs can resolve fine spatial patterns; resolving two separate points remains limited by receptor spacing.",
    "Females again responded to lower contrast than males, consistent with the sex difference in the earlier orienting study."],
    "Zurek & Nelson (2012a); Land (1985)", ["zn12a", "land85"])

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
    "Land (1971)", ["land71"])

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
    "Jakob and colleagues tethered adult female _Phidippus audax_ in an infrared eye tracker. Disks 3, 4 or 5° across appeared at the screen centre and after 10 s moved back and forth for 1 min at 2.77, 7.60 or 15.13°/s. Each spider saw every combination with its ALEs open, then again with them painted over.",
    "With ALEs open, the retinae followed the disk closely, keeping both high-acuity ‘elbows’ together over it (panel D, red). With ALEs masked, retinae stayed relaxed (blue), moving only briefly after the disk passed in front of them; they were farther from the disk and from each other and showed less torsion (MANOVA, P < 0.001).",
    "Scanning of a still cricket or oval did not differ with masking; crickets were examined longer and with more torsion (P < 0.05).",
    "ALE input is therefore necessary for tracking moving targets but not for scanning stationary ones."],
    "Jakob et al. (2018)", ["jakob18"], layout="figure-right", figure_width=5.6,
    figure={"path": "figures/p_jakob18_fig1.png", "caption": "Jakob et al. (2018), Fig. 1. (A) Principal eyes and ALEs of P. audax; (B) eye-tracker images of the retinae; (C) measured variables; (D) disk position (black) and retinal position, ALEs unmasked (red) or masked (blue); 20 px ≈ 1°; (E) retinal tracks over a cricket image.", "source_url": "https://doi.org/10.1016/j.cub.2018.07.065"})

add("Primary targets reduce distraction", [
    "Bruce and colleagues asked whether the ALEs redirect the principal eyes whenever something appears. While a spider viewed a primary stimulus with its principal eyes, a distractor oval appeared in the ALE field, and the eye tracker recorded whether the principal retinae moved to it.",
    "Spiders shifted their gaze to the distractor significantly less often when the primary stimulus was a cricket than when it was a different stimulus.",
    "Gaze shifts therefore depend on the properties of both stimuli. The authors interpreted this as evidence for higher-order control of principal-eye attention, a process that weighs the current target against a new one.",
    "**Attention** here is defined operationally as selective allocation of the principal eyes. The experiment measures behavior; it does not identify the neural basis of the selection."],
    "Bruce et al. (2021)", ["bruce21"])

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
    "Loconsole et al. (2024)", ["loconsole24"])

# ------------------------------------------------------------------ neural
add("Two visual pathways reach separate brain centers", [
    "In _Cupiennius salei_, Strausfeld and Barth traced secondary-eye photoreceptors to three laminae, then to separate medullae, converging on a **mushroom body**. Principal-eye axons pass through successive neuropils to a midline structure now termed the **arcuate body**. A **neuropil** is a dense region of axons, dendrites and synapses.",
    "Steinhoff and colleagues found the same principal-eye connectivity in the jumping spider _Marpissa muscosa_. Each secondary eye has its own first-order neuropil; the AL and PL first-order neuropils connect to their own second-order neuropils and to a shared one, **L2**, which they proposed as an early integration centre for movement decisions. PME axons project directly to the arcuate body.",
    "Land had already seen that receptor fibres from each AM layer end in separate regions of the first optic glomerulus. Shared names with insect brain structures do not imply homology."],
    "Strausfeld & Barth (1993); Steinhoff et al. (2020); Land (1969a)", ["sb93", "swb93", "steinhoff20", "land69a"])

add("Recording from a pressurized brain", [
    "Spider legs are extended partly by **hydraulic pressure** in the haemolymph, so a large opening in the cuticle causes fatal fluid loss. Earlier neural work on salticids was limited to recordings from the eyes.",
    "Menda and colleagues made an opening only 100–200 µm wide, small enough for the spider’s clotting to seal it, and advanced a glass-insulated tungsten electrode into the brain in or just behind the arcuate body of _Phidippus audax_.",
    "Recordings were stable for hours: 53 sites in 33 animals, with a mean of 2 h between the first and last recording per animal. Spikes were separated into **single units** by amplitude threshold and wavelet-based clustering (panels B–D).",
    "Extracellular single-unit recording reports one neuron’s spikes but not its shape or identity; confocal imaging confirmed only the electrode position."],
    "Menda et al. (2014)", ["menda14"], layout="figure-right", figure_width=4.4,
    figure={"path": "figures/p_menda14_fig1.png", "caption": "Menda et al. (2014), Fig. 1. (A) Fields of view, electrode site and confocal verification near the arcuate body (Arc; bar 100 µm); (B–C) extracellular traces; (D) two sorted units (n = 774 and 2243 spikes).", "source_url": "https://doi.org/10.1016/j.cub.2014.09.029"})

add("A single neuron follows a prey-like target", [
    "A 1.5° black target moved along a fly-like path for 64 s; the sequence was repeated 22 times over 24 min. The unit fired in bursts locked to particular stretches of the path (A, warm colours), with a strikingly consistent pattern from trial to trial (B, C).",
    "A generalized linear model based on target position, velocity and direction explained only a small percentage of the response: the neuron encodes the moving target, but not as a simple function of where it is or how fast it moves."],
    "Menda et al. (2014)", ["menda14"], layout="figure-below", text_height=1.6,
    figure={"path": "figures/p_menda14_fig2.png", "caption": "Menda et al. (2014), Fig. 2. (A) Target path in 10 s segments, dot colour/size = firing rate; (B) smoothed firing rate across 22 presentations; (C) spike rasters.", "source_url": "https://doi.org/10.1016/j.cub.2014.09.029"})

add("Fly images drive a neuron more than scrambled flies", [
    "Lateral and dorsal images of a fly, a conspecific and a heterospecific jumping spider were shown at natural size at six positions. One unit preferred the dorsal fly: median 14.9 spikes/s, versus 7.2 for the shuffled baseline and 5.9 for a **scrambled fly** with the same parts rearranged (Wilcoxon, P < 0.05, Bonferroni-corrected).",
    "The scrambled control, borrowed from face-recognition studies, shows sensitivity to the arrangement of parts. Two further units responded similarly; three units do not establish a fly-detector cell type."],
    "Menda et al. (2014)", ["menda14"], layout="figure-below", text_height=1.75,
    figure={"path": "figures/p_menda14_fig3.png", "caption": "Menda et al. (2014), Fig. 3. (A) Images (bar 3°); (B) responses at six locations; (C) spike scores (+, different from shuffled; *, different from scrambled fly); (D) baseline firing.", "source_url": "https://doi.org/10.1016/j.cub.2014.09.029"})

add("Principal and secondary eyes interact nonlinearly", [
    "To map **spatiotemporal receptive fields (STRFs)**, sequences of 16 × 16 random black-and-white checks were flashed (100 ms per frame) and spikes were reverse-correlated with the check pattern, with eyes selectively covered.",
    "In one unit, no STRF appeared when only the secondary eyes or only the principal eyes could see; with all eyes uncovered a clear, localized STRF appeared. Because reverse correlation is linear, this means the unit’s response depended on a nonlinear combination of input from both eye types.",
    "The STRF emerged 80–160 ms after stimulus onset, a delay suggesting several synapses between retina and recording site. Nine units from six animals had significant STRFs; others showed different interactions.",
    "This is the first direct evidence that principal- and secondary-eye signals converge on single neurons, though so far in one clearly documented cell."],
    "Menda et al. (2014)", ["menda14"], layout="figure-right", figure_width=5.0,
    figure={"path": "figures/p_menda14_fig4.png", "caption": "Menda et al. (2014), Fig. 4. (A) Check sequences; (B) responses; (C) STRFs 60–180 ms after onset with secondary eyes only, principal eyes only, or all eyes; (D) significant pixels, all eyes.", "source_url": "https://doi.org/10.1016/j.cub.2014.09.029"})

# ------------------------------------------------------------------ cognition-level behavior
add("Spiders discriminate biological motion with secondary eyes", [
    "De Agrò and colleagues presented **point-light displays** to the secondary eyes of _Menemerus semilimbatus_. These displays show only dots placed on the joints of a moving animal; shape is absent, but the coordinated motion of the dots specifies a living walker.",
    "Spiders stood on a sphere and chose between displays on either side. The comparisons were biological motion versus random dot motion, and biological motion versus scrambled displays that preserve local dot trajectories but not their arrangement.",
    "Spiders discriminated biological from random motion but turned preferentially toward the random display. They showed no preference between biological and scrambled displays.",
    "Discrimination shows that the secondary-eye pathway extracts more than the presence of motion. The direction of the preference is unexplained; the authors did not propose a confirmed functional reason for it."],
    "De Agrò et al. (2021)", ["deagro21"])

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
    "Parry & Brown (1959); Nabawy et al. (2018)", ["pb59", "nabawy18"])

add("Small eyes trade sensitivity for acuity", [
    "Small eyes collect little light. Cerveira and colleagues tested whether _Cyrba algerina_ and _C. ocellata_, which hunt under stones, can identify prey and rivals in dim light.",
    "Both species performed proficiently at 234 and 1.35 cd/m². At 0.54 cd/m² only a minority succeeded, and at 0.24 cd/m² none did. Performance therefore failed over a narrow range of luminance.",
    "The principal eyes of _C. algerina_ have a short focal length and wide paired receptors that pool light, raising sensitivity at the cost of acuity (12.4 arcmin).",
    "**Luminance** measures the light reaching the eye from a surface, in candelas per square meter."],
    "Cerveira et al. (2019, 2021)", ["cerveira19", "cerveira21"])

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

assert len(S) == 44, len(S)

TAKEAWAYS = {
    "cite": "Land (1969a, b; 1971); Nagata et al. (2012); Jakob et al. (2018); Steinhoff et al. (2020)",
    "refs": [R[k] for k in ("land69a", "land69b", "land71", "nagata12", "zurek15", "jakob18", "bruce21", "steinhoff20", "menda14")],
    "items": [
        {"lead": "Two eye systems, two jobs.",
         "text": "Secondary eyes (wide field, ~0.5–1.5° spacing) detect and localize movement; principal eyes (narrow, ~0.04–0.1° acuity) inspect identity."},
        {"lead": "Telephoto optics plus a movable retina.",
         "text": "Receptors 1.7 µm (11 arcmin) apart; six muscles, six axons. Saccades of 15° in < 0.1 s; scanning sweeps 1–2 s with 40–50° torsion every 5–15 s."},
        {"lead": "Tiers give color and depth.",
         "text": "UV (~360–370 nm) and green (~520–532 nm) receptors; green-pigmented layer 2 receives a defocused image that signals absolute distance — red light causes short jumps."},
        {"lead": "ALEs are necessary for tracking and looming.",
         "text": "Masking ALEs abolishes smooth principal-eye tracking but not scanning of still objects, and abolishes backing away from looming stimuli."},
        {"lead": "Turns are open-loop.",
         "text": "Image position on a lateral eye at first sighting sets turn size; the ring experiment shows accurate turns without visual feedback."},
        {"lead": "Separate pathways, first evidence of convergence.",
         "text": "Principal eyes → arcuate body; secondary eyes → mushroom body. One recorded unit showed a receptive field only when both eye types could see (80–160 ms latency)."},
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
