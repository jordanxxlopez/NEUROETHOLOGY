#!/usr/bin/env python3
"""Generate lectures/L9/lecture.json (Lecture 9: toad prey-catching and tectal feature detectors).

Figures are panels cropped by crop_figs.py from the original articles (instructor-uploaded PDFs
of Ewert's papers and open-access articles); the title image is a credited Commons photograph.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

R = {
    "E78": ("Ewert et al. (1978)", "Ewert JP, Borchers HW, von Wietersheim A (1978). Question of prey feature detectors in the toad's Bufo bufo (L.) visual system: a correlation analysis. Journal of Comparative Physiology 126: 43–47", "10.1007/BF01342649"),
    "E79": ("Ewert et al. (1979)", "Ewert JP, Arend B, Becker V, Borchers HW (1979). Invariants in configurational prey selection by Bufo bufo (L.). Brain, Behavior and Evolution 16: 38–51", "10.1159/000121822"),
    "SP81": ("Schürg-Pfeiffer & Ewert (1981)", "Schürg-Pfeiffer E, Ewert JP (1981). Investigation of neurons involved in the analysis of gestalt prey features in the frog Rana temporaria. Journal of Comparative Physiology 141: 139–152", "10.1007/BF01342660"),
    "E97": ("Ewert (1997)", "Ewert JP (1997). Neural correlates of key stimulus and releasing mechanism: a case study and two concepts. Trends in Neurosciences 20(8): 332–339", "10.1016/S0166-2236(96)01042-9"),
    "E01": ("Ewert et al. (2001)", "Ewert JP, Buxbaum-Conradi H, Dreisvogt F, Glagow M, Merkel-Harff C, Röttgen A, Schürg-Pfeiffer E, Schwippert WW (2001). Neural modulation of visuomotor functions underlying prey-catching behaviour in anurans: perception, attention, motor performance, learning. Comparative Biochemistry and Physiology A 128: 417–461", "10.1016/S1095-6433(00)00333-0"),
    "K22": ("Keeffe et al. (2022)", "Keeffe R, Blob R, Blackburn D, Mayerl C (2022). XROMM analysis of feeding mechanics in toads: interactions of the tongue, hyoid, and pectoral girdle. Integrative Organismal Biology 4(1): obac045", "10.1093/iob/obac045"),
    "Y17": ("Yovanovich et al. (2017)", "Yovanovich CAM, Koskela SM, Nevala N, Kondrashev SL, Kelber A, Donner K (2017). The dual rod system of amphibians supports colour discrimination at the absolute visual threshold. Philosophical Transactions of the Royal Society B 372: 20160066", "10.1098/rstb.2016.0066"),
    "FR22": ("Flaive & Ryczko (2022)", "Flaive A, Ryczko D (2022). From retina to motoneurons: a substrate for visuomotor transformation in salamanders. Journal of Comparative Neurology 530(14): 2518–2536", "10.1002/cne.25348"),
    "B11": ("Bianco et al. (2011)", "Bianco IH, Kampff AR, Engert F (2011). Prey capture behavior evoked by simple visual stimuli in larval zebrafish. Frontiers in Systems Neuroscience 5: 101", "10.3389/fnsys.2011.00101"),
    "S14": ("Semmelhack et al. (2014)", "Semmelhack JL, Donovan JC, Thiele TR, Kuehn E, Laurell E, Baier H (2014). A dedicated visual pathway for prey detection in larval zebrafish. eLife 3: e04878", "10.7554/eLife.04878"),
    "BE15": ("Bianco & Engert (2015)", "Bianco IH, Engert F (2015). Visuomotor transformations underlying hunting behavior in zebrafish. Current Biology 25(7): 831–846", "10.1016/j.cub.2015.01.042"),
    "F20": ("Förster et al. (2020)", "Förster D, Helmbrecht TO, Mearns DS, Jordan L, Mokayes N, Baier H (2020). Retinotectal circuitry of larval zebrafish is adapted to detection and pursuit of prey. eLife 9: e58596", "10.7554/eLife.58596"),
    "A19": ("Antinucci et al. (2019)", "Antinucci P, Folgueira M, Bianco IH (2019). Pretectal neurons control hunting behaviour. eLife 8: e48114", "10.7554/eLife.48114"),
    "H19": ("Henriques et al. (2019)", "Henriques PM, Rahman N, Jackson SE, Bianco IH (2019). Nucleus isthmi is required to sustain target pursuit during visually guided prey-catching. Current Biology 29(11): 1771–1786.e5", "10.1016/j.cub.2019.04.064"),
    "M17": ("Muto et al. (2017)", "Muto A, Lal P, Ailani D, Abe G, Itoh M, Kawakami K (2017). Activation of the hypothalamic feeding centre upon visual prey detection. Nature Communications 8: 15029", "10.1038/ncomms15029"),
}


def ref(k):
    return f"{R[k][1]}. https://doi.org/{R[k][2]}"


def fig(k, name, num, caption):
    return {"path": f"figures/{name}.png", "caption": f"{R[k][0]}, Fig. {num}. {caption}",
            "source_url": f"https://doi.org/{R[k][2]}", "kind": "article"}


slides = []


def add(title, refs, body, transcript, figure=None, figures=None, width=None, primary=None):
    assert len(title) <= 62, title
    paras = [p.strip() for p in body.strip().split("\n\n")]
    s = {"title": title, "body": paras, "transcript": transcript,
         "cite": "; ".join(R[k][0] for k in refs[:3]), "refs": [ref(k) for k in refs]}
    if figures:
        s.update(layout="figures-right", figures=figures, figure_width=width or 5.6, primary_figure_height=primary or 2.5)
    else:
        s.update(layout="figure-right", figure=figure)
        if width:
            s["figure_width"] = width
    slides.append(s)


# ------------------------------------------------------------- behavior
add("Common toads catch prey in a fixed sequence of acts", ["E01", "E79"], """
The common toad, _Bufo bufo_, is an active forager. **Prey-catching** proceeds as a sequence of acts: the toad **orients** (turns its head and body toward the object), **approaches** it, **fixates** it binocularly and finally **snaps**, flipping out its sticky tongue. Each act is ballistic, but the chain depends on where the prey moves.

Ewert's laboratory measured the first act under controlled conditions. A toad sat in a glass vessel while a small cardboard object was driven past a window at a fixed distance of about 7 cm, and an observer counted the toad's turning responses.

Frogs such as _Rana esculenta_ hunt differently, as sit-and-wait predators that often orient and snap in one smooth event and accept non-prey items more readily.""",
[
    ["The common toad is an active hunter, and Ewert broke its prey-catching into a sequence of separate acts.",
     ["First it orients, turning toward the object; then it approaches, fixates the object with both eyes, and finally snaps with its tongue.",
      "Each act is fast and ballistic, but which act comes next depends on where the prey is."]],
    ["To measure the behavior, a toad sat in a glass vessel and a small piece of black cardboard was moved past a window about 7 centimeters away.",
     ["Counting how often the toad turned toward the object gives a number for how prey-like that object is."]],
    "Frogs like Rana esculenta wait for prey instead, often turning and snapping in one movement, and they snap at non-prey items more often than toads.",
],
figure=fig("E79", "e79_f1", "1", "Apparatus: a toad (t) in a glass vessel watches a stimulus (s) moved past a window; photos A–C show turning toward it."))

add("Turning toward a circling dummy measures prey value", ["E01"], """
In the standard **dummy test**, the toad sits in a glass vessel at the center of a cylindrical arena. A black cardboard object, the **dummy**, is moved around the vessel at constant angular velocity by a motor-driven holder.

Each time the object passes, a hungry toad turns to follow it. The number of **orienting turns** per 30 s is the measure of how strongly the stimulus releases prey-catching.

Because the object's shape, size, contrast and speed are fully controlled, the dummy test turns a natural behavior into a quantitative stimulus–response relationship. Real prey have other features too; the advantage of the paradigm is that the same measure can be compared with neuronal responses, with lesion effects and with changes produced by learning.""",
[
    ["In the standard test the toad sits in a glass vessel in the middle of a round arena, and a black cardboard object circles around it at a constant speed.",
     ["A hungry toad turns to follow the object each time it passes."]],
    "The number of turns in 30 seconds is the measure of how prey-like the stimulus is.",
    ["The strength of this method is control.",
     ["Shape, size, contrast and speed can each be changed one at a time, and the same number can then be compared with neuron recordings, lesions and learning experiments."]],
],
figure=fig("E01", "e01_f2a", "2A", "Arena for the dummy test: the toad in a glass vessel (GV) and the stimulus object (SO) driven around it by a motor (MD)."),
width=4.6)

add("A worm is long along its direction of motion", ["E01", "E97"], """
Ewert varied two dimensions of a black rectangle. **ep** is its edge length **parallel** to the direction of movement and **ea** its edge length **across** the direction of movement.

Lengthening a 2.5-mm bar along ep, which produces a **worm-like** stripe, increased the turning rate steeply, to about 40 turns per 30 s at 20–40 mm. Lengthening the same bar along ea, an **antiworm**, abolished turning. Squares (ep = ea) became more effective up to about 10 mm and then lost their prey value as they grew larger.

The toad therefore does not respond to size alone. It relates the two extensions to each other, a computation Ewert called a **features-relating algorithm**: extension along ep signals prey, and extension along ea, the most decisive feature, reduces prey value. Large squares, which extend in both dimensions, resemble threats.""",
[
    ["Ewert used black rectangles and changed two dimensions separately.",
     ["ep is the length along the direction of movement and ea is the length across it."]],
    ["The results were clear.",
     ["Making a 2.5 millimeter bar longer along its direction of motion, a worm, raised the turning rate to about 40 turns per 30 seconds.",
      "Making the same bar longer across its direction of motion, an antiworm, abolished turning.",
      "Squares worked best around 10 millimeters and then stopped working as they grew."]],
    ["So the toad compares the two extensions instead of judging size.",
     ["Length along the movement direction signals prey, length across it reduces prey value, and a large square that is big in both directions resembles a threat."]],
],
figure=fig("E01", "e01_f2bc", "2B–C", "Stimuli a (worm), b (antiworm) and c (square) and turning rate as each edge length increases (n = 20 toads)."),
width=4.6)

add("Worm preference holds for vertical motion and contrast", ["E79"], """
Ewert, Arend, Becker and Borchers asked whether the worm–antiworm distinction depends on how the stimulus moves. Stripes 3.5 mm wide were moved up and down in front of the toad at 16°/s.

When the stripe was elongated along its vertical path (worm), turning increased with length. When it was elongated perpendicular to its path (antiworm), turning decreased toward zero. The rule was the same as for horizontal motion: the axis that matters is defined by the direction of movement, not by gravity or the horizon.

The discrimination also held when white stripes moved on a black background, although black stripes on white produced stronger responses. Contrast direction therefore changes the overall level of prey-catching but not the configurational preference.""",
[
    ["The next question was whether the worm rule depends on horizontal movement.",
     ["Stripes were moved up and down in front of the toad instead of sideways."]],
    ["The answer was no.",
     ["A stripe long along its vertical path was still a worm and drew more turning as it lengthened.",
      "A stripe long across its path was still an antiworm and was rejected."]],
    "The same held for white stripes on a black background. Black on white gave stronger responses overall, but the worm–antiworm preference was the same.",
],
figure=fig("E79", "e79_f2", "2", "Turning to vertically moving stripes: worm-like (A) and antiworm-like (B), white on black (left) and black on white (right)."),
width=4.2)

add("Prey selection is invariant to movement direction", ["E79"], """
Ewert et al. then moved the stimuli horizontally, diagonally at 30°, 60°, 120° and 150°, and vertically, always at 20°/s. A **2.5 × 30 mm stripe** oriented along its direction of motion (a) was compared with the same stripe oriented across it (b) and with a small 2.5 × 2.5 mm square (c).

At every direction the worm released about 30 turns per 30 s, while the antiworm and the small square released almost none. The toad made essentially no errors in classifying worm against antiworm at any angle.

An **invariant** is a property of recognition that does not change when other stimulus parameters change. The worm–antiworm discrimination is invariant to the direction of movement in the visual field, to contrast direction and, within limits, to velocity and distance.""",
[
    ["Here the stimuli moved in many directions: sideways, diagonally and up and down.",
     ["The worm, the antiworm and a small square were each tested at every angle."]],
    ["At every angle the worm drew about 30 turns in 30 seconds, while the antiworm and the small square drew almost none.",
     ["The toad essentially never mistook one for the other."]],
    "An invariant is a feature of recognition that stays the same when other things about the stimulus change. For the toad, the worm–antiworm decision is invariant to movement direction, contrast direction and, within limits, speed and distance.",
],
figure=fig("E79", "e79_f3", "3A", "Turning to a worm stripe (a), antiworm stripe (b) and small square (c) moved at different angles to the horizon."),
width=4.4)

add("A nearby square reduces the prey value of a worm", ["E79"], """
Ewert et al. tested how a second element changes recognition. A 2.5 × 30 mm worm stripe was moved alone (a) or together with a 2.5 × 2.5 mm square placed 10 mm from it (b).

Adding the square reduced prey-catching from about 26 turns per 30 s to about 8–10 turns, at horizontal, diagonal and vertical directions alike. When the stripe was tested alone again (a'), responses returned to their original level.

The square adds extension across the direction of movement of the whole configuration, which the toad treats as an antiworm feature. The inhibitory effect therefore follows the same configurational rule, and it too is independent of movement direction.""",
[
    ["This experiment added a small square next to a worm stripe.",
     ["The square sat 10 millimeters from the stripe and moved with it."]],
    ["The square sharply reduced turning, from about 26 to about 8 to 10 turns per 30 seconds, whatever the direction of movement.",
     ["When the stripe was shown alone again, the toad responded normally."]],
    "The square adds extent across the direction of motion, an antiworm feature, so the combined object looks less like prey.",
],
figure=fig("E79", "e79_f4", "4", "Turning to a worm stripe alone (a, a') and to the stripe with a small square 10 mm away (b), at 0°, 45° and 90°."),
width=4.0)

add("Recognition invariants resemble human object recognition", ["E79"], """
Ewert et al. compared the toad's prey recognition with how humans recognize a symbol. A person identifies the letter A whether it is tilted, small or large, or drawn in white on black. In the same way, a toad identifies a worm whether it moves horizontally or vertically, and whether it is black on white or white on black.

Ewert proposed that such invariants make the toad a useful model for the mechanism of object recognition. Neurons in the optic tectum and the thalamic–pretectal region respond to configurational features of moving stimuli, and their receptive fields are approximately radially symmetrical, so their selectivity must come from the way information about extension along and across the direction of movement is combined.""",
[
    ["Ewert compared the toad's worm recognition with how we recognize the letter A.",
     ["We recognize the A when it is tilted, smaller or larger, or white on black."]],
    "The toad recognizes a worm when it moves in any direction and in either contrast, so its recognition also has invariants.",
    ["That makes the toad a model for how a brain recognizes objects.",
     ["The relevant neurons in the tectum and pretectum have roughly circular receptive fields, so their preference for worms has to come from how the brain combines information about length along and across the movement direction."]],
],
figure=fig("E79", "e79_f6", "6", "Invariants in pattern recognition: the letter A for a human and worm versus antiworm for Bufo bufo."),
width=5.6)

add("Frogs and toads differ in how sharply they reject antiworms", ["SP81", "E01"], """
Schürg-Pfeiffer and Ewert compared configurational selectivity in the frog _Rana temporaria_ and the toad _Bufo bufo_. They used a **discriminant value**, D(W,A), which equals +1 when only the worm releases a response, −1 when only the antiworm does and 0 when both are equally effective.

In both species D(W,A) rose with stripe length, so both prefer worms. The toad's curve rose steeply and reached +1 at short lengths, whereas the frog's rose gradually and reached +1 only for long stripes.

This difference fits the species' hunting strategies. The actively hunting toad is relatively selective, whereas the sit-and-wait frog, which depends on a low snapping threshold, also catches non-prey items occasionally.""",
[
    ["Schürg-Pfeiffer and Ewert compared the common frog and the common toad with one number, the discriminant value.",
     ["It is plus one if only the worm gets a response, minus one if only the antiworm does, and zero if they are equal."]],
    ["Both species prefer worms, but the toad is much sharper.",
     ["The toad's value reaches plus one with short stripes, while the frog needs long stripes to discriminate completely."]],
    "That matches how they hunt. The toad searches actively and is selective; the frog waits and snaps at more things, including non-prey.",
],
figure=fig("SP81", "sp_f12", "12", "Discriminant value for worm versus antiworm during prey-catching in R. temporaria and B. bufo as stripe length increases."),
width=4.6)

# ------------------------------------------------------------- retina and tectum
add("Retinal ganglion cells encode size, not configuration", ["E78", "E97", "F20"], """
In the 1950s Barlow and Lettvin proposed that a class of frog retinal ganglion cell acts as a "bug detector". **Retinal ganglion cells** are the output neurons of the retina. Toad ganglion cells fall into classes **R1–R4**, with excitatory receptive fields of about 2–3°, 4–6°, 8–10° and 12–16° respectively, each surrounded by an inhibitory zone.

Ewert, Borchers and von Wietersheim recorded R2, R3 and R4 cells while worm-like (W) and antiworm-like (A) stripes crossed their receptive fields. R2 cells responded best to small stimuli of either configuration and declined as stripes lengthened in both orientations.

No retinal class reproduced the toad's behavior, which rose for worms and fell for antiworms. Grüsser concluded from such data that no ganglion cell type is specific to prey; the retina parcels the image by size, contrast and movement.""",
[
    ["Barlow and Lettvin in the 1950s suggested that a type of frog retinal ganglion cell was a bug detector.",
     ["Ganglion cells are the output neurons of the retina, and in the toad they come in four classes, R1 to R4, with progressively larger receptive fields."]],
    ["Ewert's group tested R2, R3 and R4 cells with worm and antiworm stripes.",
     ["R2 cells fired best to small objects of either kind and fired less as stripes got longer in either orientation."]],
    "No retinal class matched the toad's behavior, which goes up for worms and down for antiworms. The retina reports size, contrast and movement, but it does not identify prey.",
],
figures=[fig("E78", "e78_f1", "1", "Turning (B) and firing of tectal T5(1), T5(2), pretectal TH3 and retinal R2–R4 neurons to worm (W) and antiworm (A) stripes."),
         fig("F20", "forster_f3c", "3C", "Zebrafish retinal axon terminals in the tectum colored by functional class; 5°-dot and 30°-dot inputs by depth.")],
width=5.0, primary=3.0)

add("Only tectal T5(2) neurons match the toad's discrimination", ["E78"], """
Ewert et al. computed the discriminant value D(W,A) for behavior and for each neuron class, and correlated the stimulus–response curves.

The behavioral curve rose to +1. Retinal R2 and R3 values were negative for short stripes and rose only at long lengths; R4 stayed near zero. Tectal **T5(1)** neurons were sensitive to configuration but hardly discriminated, and pretectal **TH3** neurons had negative values, preferring antiworms.

Only tectal **T5(2)** neurons had a curve resembling the behavior. Ewert classed neurons as **sensitive** (responding to configurational stimuli), **selective** (responding differentially in the same way as behavior) or **specific** (responding to one configuration only). T5(2) neurons were selective, but no neuron was specific: no single "worm detector" cell was found.""",
[
    ["Ewert's group then compared every neuron class with behavior using the discriminant value.",
     ["Behavior went to plus one; the retinal classes were negative or near zero for most stripe lengths."]],
    ["In the tectum, T5(1) neurons responded to the stimuli but barely told worm from antiworm.",
     ["Pretectal TH3 neurons had negative values, meaning they preferred antiworms."]],
    ["Only tectal T5(2) neurons followed the behavior.",
     ["Ewert called them selective, because they discriminate the way the toad does.",
      "But none were specific, responding only to worms, so there is no single worm-detector neuron."]],
],
figure=fig("E78", "e78_f2", "2", "Discriminant value D(W,A) for behavior (B) and for retinal (R2–R4), tectal (T5(1), T5(2)) and pretectal (TH3) neurons."),
width=4.6)

add("Frog tectal neurons show the same division of labor", ["SP81"], """
Schürg-Pfeiffer and Ewert recorded 63 single neurons in the frog _Rana temporaria_: retinal classes R1–R3 and tectal classes T5(1), T5(2), T5(3) and T7.

Retinal cells preferred antiworms when stripes were shorter than their excitatory receptive field and worms only when stripes were longer, as expected from a centre–surround organization. Tectal **T5(1)** neurons showed almost no configurational preference, **T5(2)** neurons preferred worms, and **T5(3)** neurons preferred antiworms, resembling pretectal TH3 cells.

Plotted side by side, frog and toad neuron classes have similar shapes, but the toad's retinal (R2, R3) and tectal (T5(1), T5(2)) selectivities are sharper. This parallels the sharper discrimination of the toad's behavior.""",
[
    ["The same analysis was done in the frog with 63 neurons from the retina and tectum.",
     ["Retinal cells preferred antiworms for short stripes and worms for long stripes, which follows from their centre–surround receptive fields."]],
    ["In the tectum, three classes had three different preferences.",
     ["T5(1) cells barely cared about configuration, T5(2) cells preferred worms, and T5(3) cells preferred antiworms, much like pretectal TH3 cells in the toad."]],
    "Frog and toad have the same neuron classes, but the toad's are more selective, which matches its more selective behavior.",
],
figure=fig("SP81", "sp_f11", "11", "Discriminant values of retinal and tectal neuron classes in R. temporaria (above) and B. bufo (below) versus stripe length."),
width=6.4)

add("Retina, tectum and pretectum feed visual prey-catching", ["E97", "E01"], """
The **optic tectum (T)**, in the roof of the midbrain, is the main target of the retina (R). It is homologous to the mammalian **superior colliculus**. The **pretectal thalamic** region (TH), at the boundary of diencephalon and midbrain, also receives retinal input. Both contain **retinotopic maps**, in which neighboring points in the visual field are represented by neighboring neurons.

Outputs from tectum and pretectum descend to **premotor and motor structures (PMS)** in the medulla oblongata and spinal cord that generate orienting and snapping.

Forebrain structures modulate this pathway: the **striatum (S)** and the **lateral anterior thalamic nucleus (LA)** take part in response gating, and the **medial pallium (MP)**, the amphibian homolog of the hippocampus, takes part in learning.""",
[
    ["The main structures are the retina, the optic tectum and the pretectal thalamus.",
     ["The tectum is in the roof of the midbrain and corresponds to the mammalian superior colliculus; the pretectum lies just in front of it.",
      "Both have retinotopic maps, where neighboring points in space map onto neighboring neurons."]],
    "Their output goes down to premotor and motor structures in the medulla and spinal cord that produce turning and snapping.",
    "Forebrain areas modulate this pathway: the striatum and lateral anterior thalamus help gate responses, and the medial pallium, the amphibian hippocampus, is involved in learning.",
],
figure=fig("E97", "t97_f1a", "1A", "Anuran brain: retina (R), optic tectum (T), pretectal thalamus (TH), striatum (S), medial pallium (MP) and premotor–motor structures (PMS)."),
width=5.4)

add("Tectal neurons collect input across retinal layers", ["E97"], """
Retinal ganglion cell axons end in different layers of the superficial tectum: **R2** in laminae B–C, **R3** in C–F and **R4** in F–G. Neuropeptide-Y fibers from the pretectum end mainly in laminae B and C.

Intracellular recordings followed by cobalt-lysine filling revealed tectal neurons whose dendrites span several of these laminae. A pear-shaped **T5.1** cell (yellow) arborizes from lamina B through G and can integrate inputs from several retinal classes. Another T5.1 subtype (green) spreads laterally, suited to interactions across the tectal map. A large neuron (violet) responds to any moving stimulus. The **T5.2** pyramidal cell (blue) integrates inputs from layers 8 and 9 and sends its axon toward the medulla oblongata.

This anatomy allows each tectal output neuron to combine several retinal channels with pretectal input.""",
[
    ["Each retinal class ends in its own layers of the tectum.",
     ["R2 axons end in laminae B and C, R3 in C to F, and R4 in F and G, and inhibitory fibers from the pretectum end mainly in B and C."]],
    ["Tectal neurons reach across these layers.",
     ["The yellow T5.1 cell has dendrites from lamina B to G, so it can combine several retinal classes.",
      "The blue T5.2 cell collects input from layers 8 and 9 and sends its axon down to the medulla."]],
    "Because the dendrites cross layers, each tectal output neuron can mix several retinal channels and pretectal input.",
],
figure=fig("E97", "t97_f2a", "2A", "Cobalt-filled tectal neurons (T5.1 yellow and green, large neuron violet, T5.2 blue) spanning tectal laminae A–G."),
width=6.0)

add("T5(2) neurons fire to worms but weakly to antiworms", ["SP81"], """
Schürg-Pfeiffer and Ewert showed the spike trains of a frog **T5(2)** neuron to squares, worm-like stripes and antiworm-like stripes of increasing length.

For squares (left column), firing increased up to 8° and then fell. For stripes extended along the direction of movement (right column), firing remained strong as the stripe lengthened. For stripes extended across the direction of movement (middle column), firing weakened progressively as the stripe became longer.

The excitatory receptive field of these cells averaged about 18° in diameter and is roughly circular, so the worm preference is not simply a matter of receptive-field shape. It depends on interactions between the stimulus's extension along and across its path, the same relation the toad's behavior expresses.""",
[
    ["These are spike trains from one frog T5(2) neuron.",
     ["Squares drove it best at about 8 degrees, and larger squares drove it less."]],
    ["Worm-like stripes kept driving it strongly as they got longer, but antiworm stripes drove it less and less.",
     ["That is the same preference the animal shows in behavior."]],
    "Its receptive field is round, about 18 degrees across, so the preference cannot come from the shape of the field; it comes from how the cell's inputs combine length along and across the motion.",
],
figure=fig("SP81", "sp_f8", "8", "Spike trains of a T5(2) neuron to squares, antiworm (middle) and worm (right) stripes of 4–20° length; time scale 1 s."),
width=4.8)

add("Retina, tectum and pretectum code ep and ea differently", ["E97"], """
Ewert summarized responses to ep, ea and square size in a color-coded table, with each response scaled to the optimal stimulus.

Prey-catching rose with ep, fell with ea and peaked for intermediate squares. Avoidance behavior showed the reverse, rising for large squares. Retinal **R2, R3 and R4** cells responded to ea and to square area according to their receptive-field size. Pretectal **TH3** and tectal **T5.3** neurons responded best to large ea and large squares.

Tectal **T5.1** neurons coded ep. Only **T5.2** neurons combined strong responses to ep with weak responses to ea, the pattern of prey-catching, and **T5.4** neurons responded to large extensions in both dimensions, like avoidance. Ewert proposed that ensembles of such neurons define perceptual categories: prey (T5.1, T5.2), predator (T5.3, TH3, T5.4).""",
[
    ["This color table puts behavior and neurons on the same scale.",
     ["Red means the strongest response and dark gray almost none."]],
    ["Prey-catching rises with length along the motion, falls with length across it, and peaks for medium squares; avoidance is the opposite.",
     ["Retinal cells mainly track area, and pretectal TH3 and tectal T5.3 cells like large extensions across the motion."]],
    ["T5.2 neurons have the same pattern as prey-catching, and T5.4 neurons the pattern of avoidance.",
     ["Ewert proposed that groups of such neurons define categories like prey and predator."]],
],
figure=fig("E97", "t97_f3", "3", "Relative responses to changes in ep (A), ea (B) and square size (C): behavior and R, T and TH neuron classes (color-coded %)."),
width=4.4)

add("T5.2 activity precedes orienting in freely moving toads", ["E97", "E01"], """
To link neurons to behavior directly, Ewert's group implanted microelectrodes in the tectum of freely moving toads and recorded a **T5.2** neuron while bars moved through its receptive field.

A 2.5 × 20 mm bar moving in **prey configuration** produced a strong burst of spikes that preceded and "predicted" the toad's orienting movement toward the stimulus (arrow). The same bar moving at the same speed in **non-prey configuration** produced almost no activity, and the toad did not respond.

The coupling between the neuron's burst and the behavior supports the proposal that T5.2 neurons contribute to releasing prey-catching. The data are correlational; the burst could reflect prey recognition, its consequence or a premotor signal.""",
[
    ["The strongest link came from recordings in toads that could move freely.",
     ["An electrode in the tectum recorded a T5.2 neuron while a bar moved through its receptive field."]],
    ["When the bar moved as a worm, the neuron fired a strong burst, and that burst came just before the toad turned toward it.",
     ["When the same bar moved as an antiworm, the neuron was almost silent and the toad did nothing."]],
    "This ties the neuron's activity to the behavior, though by itself it is a correlation, not proof that the neuron causes the turn.",
],
figure=fig("E97", "t97_f4", "4A–C", "A freely moving toad's T5.2 neuron: bar in prey (A) and non-prey (B) configuration before, and non-prey (C) after a pretectal lesion."),
width=3.8)

add("Pretectal lesions abolish the worm–antiworm distinction", ["E01", "E97"], """
After a **pretectal lesion** delivered through a second implanted electrode, the same T5.2 neuron fired strongly to the non-prey bar, and the toad oriented toward it (Fig. 4C). The neuron's receptive field also enlarged and it developed resting discharge.

In behavior, toads with bilateral pretectal lesions turned toward worms, antiworms and squares at similar rates. Antiworms, which normally abolish turning, became as effective as worms.

Lesioned toads showed a wider syndrome: tectal neurons responded more strongly and to large objects and textures; toads snapped at stationary objects, at targets far out of reach and at self-induced image motion. The pretectum therefore supplies inhibition that sharpens tectal responses.""",
[
    ["After a lesion of the pretectum, the same T5.2 neuron fired strongly to the antiworm bar, and the toad turned toward it.",
     ["The neuron's receptive field also got bigger and it started firing spontaneously."]],
    ["Behaviorally, toads without a pretectum turned toward worms, antiworms and squares about equally.",
     ["The antiworm, normally ignored, became as good as a worm."]],
    "They also snapped at non-moving objects, at things too far away and at image motion caused by their own movement. The pretectum normally provides the inhibition that makes the tectum selective.",
],
figure=fig("E01", "e01_f2d", "2D", "Turning to worm (a), antiworm (b) and square (c) stimuli after bilateral pretectal thalamic lesions (n = 20 toads)."),
width=4.6)

add("Neuropeptide Y carries pretecto-tectal inhibition", ["E01", "E97"], """
**Neuropeptide Y (NPY)** is a 36-amino-acid peptide transmitter. NPY-immunoreactive fibers in the superficial tectum originate in ipsilateral pretectal nuclei that match the recording sites of TH3 and TH4 neurons, which project to the tectum.

Schwippert et al. measured the **tectal surface field potential** in cane toads, evoked by diffuse light-on and light-off, before and after NPY was applied to the tectum. NPY reduced the excitatory **N1 wave**, which reflects retinal input, by about half within minutes, and the effect lasted more than an hour.

The fragment NPY 13–36, which activates **Y2 receptors**, had the same effect, whereas NPY 18–36 did not. Y2 receptors are often presynaptic, consistent with the proposal that pretectal NPY reduces transmission from retinal terminals in the tectum.""",
[
    ["Neuropeptide Y is a peptide transmitter used by the pretectal neurons that project to the tectum.",
     ["NPY fibers in the tectum come from the same pretectal areas where TH3 and TH4 neurons are recorded."]],
    ["The experiment measured the tectal field potential evoked by turning a light on or off.",
     ["Putting NPY on the tectum cut the first excitatory wave, the retinal input, roughly in half for over an hour."]],
    ["A fragment that activates Y2 receptors did the same, and a fragment that does not had no effect.",
     ["Y2 receptors are often on presynaptic terminals, which fits the idea that NPY turns down retinal input to the tectum."]],
],
figure=fig("E01", "e01_f5", "5", "N1 amplitude of the tectal field potential to light-on (a) and light-off (b) after NPY (A), NPY 13–36 (B) and NPY 18–36 (C)."),
width=6.2)

add("Sensorimotor codes combine many processing streams", ["E97"], """
Ewert proposed that behavior is released not by single detector neurons but by **sensorimotor codes**: combinations of activity across distributed processing streams.

At least seven physiologically distinct types of tectal neurons, and several pretectal types, project to the medulla, as shown by antidromic stimulation. Each stream carries information about several stimulus properties (convergence), and each property is represented in several streams (divergence).

Particular combinations activate the motor-pattern circuits for snapping, turning toward prey, avoiding, jumping or ducking. Motivation selects among them: T5.2 responses are very weak in satiated toads during the hunting season and in unfed toads during the mating season, when approach to a mate takes priority.""",
[
    ["Ewert's model replaces a single worm detector with combinations of active neuron types, which he called sensorimotor codes.",
     ["At least seven types of tectal neurons and several pretectal types send axons down to the medulla."]],
    ["Each type carries information about several features, and each feature is carried by several types.",
     ["A particular combination activates the motor circuit for snapping, turning, avoiding, jumping or ducking."]],
    "Motivation filters these codes. T5.2 neurons respond weakly in a well-fed toad, and in the mating season, when toads approach mates instead of prey.",
],
figure=fig("E97", "t97_f5", "5", "Combinations of tectal (T) and pretectal (TH) streams, gated by feeding and mating motivation, select motor pattern circuits."),
width=5.6)

add("Medullary neurons converge inputs for snapping", ["E97"], """
Tectal and pretectal projection neurons send axons to premotor and motor structures in the **medulla oblongata**, the most caudal part of the brainstem.

In the medullary motor nucleus of the **trigeminal nerve**, which controls the jaw muscles, some neurons respond best to prey-like visual stimuli. A cobalt-filled medullary neuron has a richly branched dendritic tree extending into the lateral and medial reticular formation and into vestibular and spinocerebellar regions.

Such dendritic trees can collect inputs from many descending streams. Ewert suggested that the precise timing of these inputs could allow coincidence detection, binding distributed activity into the command for a ballistic act. Neurophysiological data suggest di- or polysynaptic connections between the tectal snapping-evoking area and medullary motor neurons for snapping.""",
[
    ["The final steps happen in the medulla, the lowest part of the brainstem.",
     ["Some neurons in the trigeminal motor nucleus, which drives the jaw muscles, respond best to prey-like visual stimuli."]],
    ["This filled medullary neuron has a huge dendritic tree reaching into several brainstem regions.",
     ["That allows it to collect signals from many descending streams at once."]],
    "Ewert suggested that the timing of those inputs, arriving together, could select the motor command. Recordings suggest only one or two synapses between the tectal snapping area and the medullary motor neurons.",
],
figure=fig("E97", "t97_f2ab", "2A–B", "Tectal neurons converging inputs (A) and a cobalt-filled medullary neuron with dendrites spanning reticular and vestibular regions (B)."),
width=5.0)

add("Without forebrain and pretectum, prey-catching is crude", ["E01", "FR22"], """
Ewert ablated both telencephalic hemispheres together with the dorsal diencephalon, which contains the pretectum, sparing the eyes, optic chiasm, preoptic area, hypothalamus, pituitary and ventral thalamus. These toads readily oriented and snapped toward moving objects. Removing the telencephalon alone, by contrast, abolished prey orienting.

The remaining **retino–tecto/tegmento–bulbar/spinal** pathway, from retina to tectum, then through tegmentum and medullary reticular formation (MRF) to spinal and cranial motor nuclei, is therefore sufficient to release orienting and snapping. Without the pretectum, however, any moving image elicited prey-catching, and toads collided with obstacles and misjudged distance.

Flaive and Ryczko traced a homologous route in salamanders, from retina through tectum to reticulospinal neurons of the middle reticular nucleus that steer the body.""",
[
    ["Two lesions give opposite results.",
     ["Removing only the cerebral hemispheres abolished prey orienting.",
      "Removing the hemispheres together with the dorsal diencephalon, which includes the pretectum, left toads that readily turned and snapped at moving objects."]],
    ["So the core pathway, retina to tectum to tegmentum and medulla to the motor nuclei, is enough to produce turning and snapping.",
     ["But without the pretectum it is indiscriminate: any moving image triggers prey-catching, and the toads bump into obstacles and misjudge distance."]],
    "Flaive and Ryczko found a matching chain in salamanders, from retina through tectum to reticulospinal neurons that steer the body toward prey.",
],
figures=[fig("E01", "e01_f3", "3", "Retino–tecto–tegmento–bulbar/spinal pathway (bold) that remains after forebrain lesion."),
         fig("FR22", "flaive_f8", "8", "Salamander visuomotor circuit: retina, tectum, middle reticular nucleus and motoneurons for orienting.")],
width=5.4, primary=2.9)

add("The tongue is flipped out and the hyoid swallows the prey", ["K22", "E01"], """
The consummatory act, **snapping**, launches the tongue. Keeffe and colleagues used **XROMM** (X-ray Reconstruction of Moving Morphology), in which radio-opaque markers implanted in skeleton and tongue are tracked in biplanar X-ray video, to follow the cane toad, _Rhinella marina_, through the feeding cycle.

The mouth opened at about 9% of the cycle, the tongue reached maximal protrusion at 13% and maximal gape at 16%, and the mouth closed with the prey at 23%. During transport and swallowing the **hyoid apparatus** moved dorsally and anteriorly, and the tongue stretched behind the skull, often more than during protrusion.

Kinematics were similar across individuals, and unsuccessful strikes resembled successful ones, consistent with snapping being a ballistic motor pattern.""",
[
    ["Snapping is the final act, and Keeffe and colleagues filmed it with X-ray video in the cane toad.",
     ["Markers in the bones and tongue let them reconstruct movements in three dimensions."]],
    ["The whole strike is quick and ordered.",
     ["The mouth opens, the tongue is fully out by about 13 percent of the cycle, and the mouth closes on the prey by about 23 percent.",
      "Then the hyoid, the cartilage frame under the tongue, moves the prey back for swallowing."]],
    "Strikes looked the same from toad to toad, and misses looked like hits, which fits the idea that once launched, the strike runs to completion.",
],
figure=fig("K22", "xromm_f8", "8", "Phases of a cane toad feeding event from X-ray video, ventral and lateral views, with tongue (pink) and hyoid (blue)."),
width=5.6)

# ------------------------------------------------------------- forebrain modulation
add("Visual neurons in the caudal ventral striatum", ["E01"], """
The amphibian **striatum** is homologous to part of the basal ganglia of amniotes, which in mammals participate in initiating and controlling orienting responses. Small lesions of the toad's caudal striatum, but not of the ventral medial pallium, produced **prey neglect**: visually guided prey-catching decreased.

Electrical stimulation of the striatum in freely moving toads did not elicit orienting, but it facilitated orienting toward a subliminal prey stimulus. There was even a retinotopic relation between stimulation sites and the parts of the visual field in which orienting was facilitated.

Buxbaum-Conradi and Ewert recorded visually responsive neurons in the cane toad's caudal ventral striatum. Their recording sites (symbols) extended from the striatal gray matter into the lateral forebrain bundle.""",
[
    ["The striatum in amphibians corresponds to part of the mammalian basal ganglia, which help start orienting movements.",
     ["Small lesions of the toad's caudal striatum produced prey neglect, a drop in prey-catching."]],
    ["Stimulating the striatum did not cause turning by itself, but it made the toad more likely to turn toward a weak prey stimulus.",
     ["The effect was even mapped to parts of the visual field, depending on where the electrode was."]],
    "Recordings found visually responsive neurons in the caudal ventral striatum, marked by the symbols on this section.",
],
figure=fig("E01", "e01_f6", "6", "Recording sites of visually responsive striatal neurons (symbols) on a transverse section of the cane toad telencephalon."),
width=5.6)

add("Striatal neurons signal motion, prey and threat", ["E01"], """
Buxbaum-Conradi and Ewert classified striatal neurons by their responses to a large square (S16°), a small square (S4°), an antiworm (A16°) and a worm (W16°).

**STR2** neurons (about 32%) increased firing to any moving stimulus, behaving like motion detectors. **STR3** neurons (15%) preferred moving squares. **STR4a** neurons responded well to the large threatening square, and **STR4b** neurons preferred prey-like worms and small squares. **STR5** neurons (15%) had resting activity that was reduced by moving stimuli, especially threat. STR1 neurons were uninfluenced.

The receptive fields of these neurons covered the whole visual field of the opposite eye or both eyes, and most habituated to repeated stimulation. Antidromic stimulation showed that striatal output in the lateral forebrain bundle is carried mainly by motion detectors and compact-object neurons.""",
[
    ["Striatal neurons fell into several types depending on what moving stimuli excited them.",
     ["About a third, STR2, fired to any moving object, like motion detectors.",
      "STR3 preferred squares, STR4a responded to a large threatening square, and STR4b preferred worm-like prey."]],
    "STR5 neurons had ongoing activity that moving stimuli, especially threats, turned down.",
    ["Their receptive fields covered the whole visual field, and most stopped responding with repetition.",
     ["This looks less like detailed shape analysis and more like signaling that something relevant has appeared, which fits a role in attention."]],
],
figure=fig("E01", "e01_f7", "7", "Firing of STR2, STR3, STR4a, STR4b and STR5 neurons to a large square (S16°), small square (S4°), antiworm (A16°) and worm (W16°)."),
width=3.6)

add("A striato-pretecto-tectal loop gates prey-catching", ["E97", "E01"], """
Ewert proposed a **gating loop** for directed attention, the translation of prey recognition into action. Retinal output reaches both tectum (T) and pretectum (TH), and pretecto-tectal inhibition distinguishes prey from non-prey.

The striatum (S) receives tectal visual information through the **lateral anterior thalamic nucleus (LA)**. It projects through the lateral forebrain bundle, which contains enkephalinergic fibers, to the pretectum, where it inhibits pretectal neurons. By reducing pretecto-tectal inhibition, the striatum **disinhibits** the tectum and releases tectal output to the motor systems.

This model explains both lesion results: without the striatum, unopposed pretectal inhibition overrides tectal responses and prey-catching fails; without the pretectum, the tectum is released indiscriminately. In the intact toad, partial inhibition allows a cautious approach.""",
[
    ["Ewert's gating loop ties the forebrain to the tectum.",
     ["The tectum's visual information reaches the striatum through the lateral anterior thalamus.",
      "The striatum projects back to the pretectum and inhibits it."]],
    ["Because the pretectum inhibits the tectum, inhibiting the pretectum releases the tectum, which is disinhibition.",
     ["A recognized prey can then trigger orienting."]],
    "This explains both lesions. Without the striatum, the pretectum's inhibition wins and prey-catching fails; without the pretectum, the tectum responds to everything.",
],
figure=fig("E97", "t97_f1b", "1B", "Gating loop: striatum (S) receives tectal (T) input via lateral anterior thalamus (LA) and inhibits pretectum (TH), which inhibits tectum."),
width=5.0)

add("Apomorphine shifts toads from hunting to waiting", ["E01"], """
**Apomorphine (APO)** is an agonist at dopamine D1 and D2 receptors. Glagow and Ewert injected it into the lymph sac of common toads and measured prey-catching 20 min later.

As the dose increased, prey-oriented turning fell from about 29 to near zero responses per minute, while snapping rose from about 7 to about 20. Toads that had been hunting sat motionless and "watched" for prey, snapping at items that came close: a shift from a **hunting strategy** to a **waiting strategy**, like that of _Rana_.

The basic pattern of prey discrimination was maintained, but its acuity dropped because of the low snapping threshold. Effects peaked 15–35 min after injection; after 70–90 min turning returned with a short rebound. Pretreatment with the D2 antagonist **haloperidol** prevented the APO effects.""",
[
    ["Apomorphine activates dopamine receptors, and it changed how toads hunt.",
     ["With higher doses, turning toward prey dropped to almost nothing, while snapping roughly tripled."]],
    ["The toads stopped pursuing and sat still, snapping at anything that came close.",
     ["That is a switch from an active hunting strategy to a sit-and-wait strategy, like the frog's."]],
    "They still preferred prey-like objects, but less sharply. The effect peaked 15 to 35 minutes after injection, and haloperidol, which blocks D2 receptors, prevented it.",
],
figure=fig("E01", "e01_f9", "9", "Prey-oriented turning (black) and snapping (white) per minute 20 min after apomorphine at 0–100 mg/kg (n = 15 toads)."),
width=5.0)

add("Apomorphine changes glucose use across the toad brain", ["E01"], """
The **¹⁴C-2-deoxyglucose (2DG)** method measures local glucose utilization: 2DG is taken up like glucose but trapped in active cells, and autoradiography maps its accumulation in brain sections.

Glagow and Ewert compared APO-treated and untreated toads, both shown a moving prey-like stimulus, across 41 brain structures. In APO-treated toads, 2DG uptake increased in retinal projection fields, the dorsal tectal layers, pretectal Lpd and anterior thalamus. It decreased in the medial tectal layers, which contain T5.1 and T5.2 output neurons.

Uptake also rose in structures for snapping (medial reticular formation, hypoglossal nucleus) and in mesolimbic and limbic structures (nucleus accumbens, ventral tegmentum, ventral medial pallium, medial septum). These changes match the distribution of dopaminergic cells and fibers in the anuran brain.""",
[
    ["The 2-deoxyglucose method shows which brain regions are working harder.",
     ["The tracer is taken up like glucose but gets trapped in active cells, so autoradiography of brain sections maps activity, from blue for low to red for high."]],
    ["Apomorphine raised activity in the areas that receive retinal input, including the pretectum, and lowered it in the deep tectal layers that hold the output neurons.",
     ["That fits stronger pretectal inhibition and weaker tectal output for turning."]],
    "Activity also rose in snapping circuits in the medulla and in limbic and mesolimbic structures, all regions with dopamine fibers.",
],
figure=fig("E01", "e01_f10", "10", "Color-coded 2DG uptake in transverse sections (a–d) of an untreated (A) and an apomorphine-treated (B) toad; blue low, red high."),
width=3.6)

add("Dopamine enlarges retinal receptive fields", ["E01"], """
Glagow and Ewert recorded single retinal ganglion cell fibers in the tectum before and after APO, using a 2° × 16° bar moving across the receptive field in antiworm orientation.

R2 neurons (excitatory receptive field 6°) and R3 neurons (8°) fired strongly increasing discharge 10–25 min after APO. In R2 neurons, the size-tuning curve shifted: the stimulus size that drove the strongest response moved from 6° before APO to about 12° after APO, so the excitatory receptive field diameter roughly doubled.

In the retina, dopamine uncouples the gap junctions of horizontal cells, which carry the inhibitory surround. Weakening the surround is consistent with larger excitatory fields and greater retinal output. Ewert et al. proposed that this enhanced retinal input drives the pretectal inhibition that reduces tectal output.""",
[
    ["Recordings from retinal ganglion cells showed that apomorphine made them more active.",
     ["The same bar drove much more firing 10 to 25 minutes after the drug."]],
    ["The receptive fields also grew.",
     ["For R2 cells, the best stimulus size moved from about 6 degrees to about 12 degrees, so the excitatory field roughly doubled."]],
    "Dopamine in the retina uncouples the horizontal cells that create the inhibitory surround, which fits larger excitatory fields. More retinal input then feeds more pretectal inhibition onto the tectum.",
],
figure=fig("E01", "e01_f12", "12", "R2 (A) and R3 (B) discharges before (a) and 10–25 min after apomorphine (b–d); (e) R2 size tuning before and after."),
width=3.4)

add("Apomorphine lowers T5.2 output but keeps its preference", ["E01"], """
At 35 min after APO, the **tectal reduction phase**, prey-selective T5.2 neurons fired less to a worm bar (A), an antiworm bar (B) and an 8° square (C), even though their retinal input had increased. T5.1 neurons were reduced as well. Their configurational preference was preserved: the worm still drove more spikes than the antiworm.

At about 75 min, during the **tectal rebound phase**, T5.2 responses increased again, matching the return of orienting behavior.

The reduction in T5.2 firing parallels the drop in prey-oriented turning, and the medial tectal layers containing these output neurons showed lower 2DG uptake. Ewert et al. proposed that APO-enhanced pretectal activity, from TH3 and TH4 neurons whose responses rose under APO, suppresses tectal output to the orienting circuits.""",
[
    ["Thirty-five minutes after apomorphine, T5.2 neurons fired less to all stimuli, even though their retinal input was larger.",
     ["They still preferred the worm over the antiworm."]],
    "By about 75 minutes their responses came back, at the same time as turning behavior returned.",
    "The time course matches behavior: less tectal output, less turning. Pretectal TH3 and TH4 neurons fired more under apomorphine, which fits the idea that extra pretectal inhibition reduces tectal output.",
],
figure=fig("E01", "e01_f13", "13", "A T5.2 neuron's responses to worm (A), antiworm (B) and square (C) before (a), 35 min (b) and 75 min (c) after apomorphine."),
width=4.0)

add("Apomorphine boosts pretectal TH3 and TH4 responses", ["E01"], """
Glagow and Ewert recorded pretectal **TH3** and **TH4** neurons, whose axons project to the tectum, and compared them with a tectal T5.2 neuron in the same stimulus condition: a 2° × 16° bar moving at 10°/s in prey configuration.

Before APO, TH3 and TH4 neurons responded only weakly to the prey-configured bar, while the T5.2 neuron responded strongly. About 35 min after APO, TH3 and TH4 discharges to the same bar increased markedly, and the T5.2 neuron's response decreased.

The opposite changes in pretectal and tectal neurons fit the gating model: dopaminergic enhancement of retinal input increases pretecto-tectal inhibition, reducing tectal output for prey-oriented turning. Striatal disinhibition of the pretectum may also be weakened under APO, which would act in the same direction.""",
[
    ["This recording compared pretectal TH3 and TH4 neurons with a tectal T5.2 neuron, all shown the same prey-like bar.",
     ["Before the drug, the pretectal neurons barely responded and the T5.2 neuron responded strongly."]],
    ["After apomorphine, the pretectal neurons fired much more and the T5.2 neuron fired less.",
     ["The pretectum gets stronger while the tectum gets weaker."]],
    "That fits the gating model: more retinal input drives more pretectal inhibition, which turns down the tectal output for turning toward prey.",
],
figure=fig("E01", "e01_f14", "14", "Responses of pretectal TH3, TH4 and tectal T5.2 neurons to a prey-configured bar before (A) and 35 min after apomorphine (B)."),
width=4.8)

# ------------------------------------------------------------- learning
add("Habituation to prey dummies is stimulus-specific", ["E01"], """
**Habituation** is a decrease in response with repeated stimulation. When a prey dummy circles repeatedly, the toad's orienting gradually stops. Responding recovers if the stimulus is withheld, presented to another part of the visual field, or altered.

Ewert and Kehl habituated toads to a black triangle moving with its narrow side leading (A). Immediately afterward the mirror-image triangle (B) elicited full responding, and it too habituated. The response decrement is therefore specific to stimulus features, which places the change in sensory and modulatory structures rather than in the motor system.

Testing many pairs revealed a **dishabituation hierarchy**: one pattern dishabituates all those below it but not vice versa, even though before habituation all were about equally effective. The toad can thus discriminate configurational cues, such as leading versus trailing edges, beyond the worm–antiworm rule.""",
[
    ["Habituation is a drop in responding to a repeated stimulus.",
     ["A toad shown the same prey dummy over and over eventually stops turning toward it."]],
    ["The decline is specific to the stimulus.",
     ["After habituating to one triangle, the toad responded fully to its mirror image.",
      "That means the change lies in recognition, not in fatigue of the motor system."]],
    "Testing many pairs produced a hierarchy: some patterns renewed responding to others but not the reverse. So toads can tell apart features like leading and trailing edges that the basic worm rule does not capture.",
],
figure=fig("E01", "e01_f16", "16", "Stimulus-specific habituation to triangles A and B (A) and the dishabituation hierarchy of moving patterns (B); inset: beetle Carabus."),
width=4.0)

add("Hand-feeding teaches toads to treat a threat as prey", ["E01", "E97"], """
In the **hand-feeding paradigm**, a toad was allowed to catch a mealworm from the experimenter's hand once daily. The moving hand is a threatening stimulus, and naive toads hesitate. After about 7 weeks, toads oriented and snapped about eight times per minute toward the hand alone: the hand (conditioned stimulus) had been associated with prey (unconditioned stimulus).

The effect generalized: antiworm bars and large moving squares were included in the prey schema. Controls exposed to hand and mealworm without contingency kept normal selectivity. Trained toads thus behaved like pretectally lesioned toads.

In 2DG experiments with a large moving square, trained toads showed increased uptake in the ventral medial pallium (vMP) and tectal structures and decreased uptake in the pretectal Lpd and Lpv nuclei. Ewert proposed that the pallium inhibits pretecto-tectal inhibition via the anterior thalamus.""",
[
    ["In the hand-feeding experiment, toads took a mealworm from the experimenter's hand once a day.",
     ["A moving hand is normally a threat, but after about seven weeks the toads turned and snapped at the hand alone."]],
    ["The learning spread.",
     ["Trained toads also treated antiworms and large squares as prey, much like toads without a pretectum, while controls given hand and mealworm separately stayed normal."]],
    "Brain activity mapping showed more activity in the ventral medial pallium and less in the pretectum. Ewert proposed that the pallium, through the anterior thalamus, switches off the pretectal inhibition.",
],
figures=[fig("E01", "e01_f18", "18", "2DG uptake in trained versus untrained toads viewing a large square; filled bars significant."),
         fig("E97", "t97_f1c", "1C", "Proposed learning loop: medial pallium (MP) inhibits pretecto-tectal inhibition via anterior thalamus (A).")],
width=5.8, primary=2.5)

add("A prey-associated odor activates the hippocampal pallium", ["E01"], """
Merkel-Harff and Ewert paired the odor **cineol** with visual prey in repeated training sessions. In naive toads, cineol presented with prey reduced prey-catching; after training, the prey-associated odor facilitated prey-catching and reduced prey selectivity, and the odor alone elicited orienting movements in arbitrary directions.

2DG autoradiography located a key structure. In a binocularly enucleated (blinded) toad without odor stimulation, the **caudal ventral medial pallium (vMP)** showed no 2DG uptake. In a blinded toad stimulated with the prey-associated cineol, vMP uptake was strong.

The vMP, the amphibian homolog of the hippocampus, thus responds to a learned olfactory prey cue even without vision. Ewert et al. proposed that vMP output disinhibits tectal T5.1 and T5.2 neurons through hypothalamic pathways, raising conditioned prey-catching motivation.""",
[
    ["Here the cue was a smell.",
     ["Toads learned that the odor cineol came with prey.",
      "Before training cineol reduced prey-catching, but afterward it increased prey-catching and made toads less choosy."]],
    ["Brain mapping showed where the learned odor acts.",
     ["In blinded toads, the ventral medial pallium was silent without the odor and strongly active with the prey-associated odor."]],
    "The ventral medial pallium is the amphibian hippocampus. Ewert proposed that it raises prey-catching motivation by releasing the tectal prey neurons from inhibition.",
],
figure=fig("E01", "e01_f22", "22", "Caudal telencephalon (A); 2DG uptake in vMP of a blinded toad without (Ba) and with (Bb) prey-associated cineol."),
width=4.4)

add("Toads use color when choosing prey", ["Y17"], """
Yovanovich and colleagues tested whether toads (_Bufo bufo_) and frogs (_Rana temporaria_) use color in prey-catching. Moving prey dummies of different colors and brightness were presented at controlled light levels.

At 40 cd/m², toads chose green dummies over blue ones about three times out of four, a significant color preference, whereas frogs showed no significant color preference but strongly preferred darker stimuli.

As luminance decreased, the toads' green preference persisted down to dim light but disappeared at the lowest intensities, where vision depends on rods. The authors found no evidence of rod-based color discrimination in prey-catching or mate choice. By contrast, frogs jumping toward lit windows could discriminate blue from green down to the absolute visual threshold. Color processing therefore depends on the task.""",
[
    ["Ewert's dummies were black and white, but toads also see color.",
     ["Yovanovich and colleagues offered toads and frogs colored moving dummies."]],
    ["In good light, toads chose green over blue about three times out of four.",
     ["Frogs did not show a color preference in prey-catching but strongly preferred darker objects."]],
    "The toads' preference faded in very dim light, where only rods work. Frogs jumping toward light could tell blue from green even at the visual threshold, so whether color is used depends on the behavior.",
],
figure=fig("Y17", "yov_f2", "2", "Prey choices by color (a) and brightness (b) in Bufo and Rana at 40 cd/m²; toad color choices across luminance (c)."),
width=6.0)

add("Retinal input reaches salamander reticulospinal neurons", ["FR22"], """
Flaive and Ryczko used an isolated salamander brain with eyes attached. They stimulated the retina electrically and imaged calcium in **reticulospinal (RS) neurons** of the middle reticular nucleus, which control steering movements.

Retinal stimulation evoked calcium responses in RS neurons, and response size grew with stimulus intensity. Responses on the side ipsilateral to the stimulated retina were larger than contralateral ones, a bias suited to turning toward one side.

Microinjection of glutamate receptor antagonists into the **optic tectum** reduced the RS responses, and tracing showed tectal projections onto RS neurons, which in turn contact spinal motoneurons. This establishes a cellular substrate, retina → tectum → reticulospinal neurons → motoneurons, for the visually guided orientation that Ewert studied behaviorally in toads.""",
[
    ["Flaive and Ryczko kept a salamander brain alive with the eyes attached.",
     ["They stimulated the retina and watched calcium signals in reticulospinal neurons that control steering."]],
    ["The neurons responded more as the stimulus got stronger, and more on one side than the other, which is what a turning command needs.",
     ["The colors in the heat maps show the size of the calcium response."]],
    "Blocking glutamate receptors in the tectum reduced the responses, and tracing showed the connections. That gives a cell-by-cell route from eye to motoneurons for orienting toward prey.",
],
figure=fig("FR22", "flaive_f7", "7", "Retinal stimulation evokes graded calcium responses in ipsilateral and contralateral reticulospinal neurons of the middle reticular nucleus."),
width=4.8)

# ------------------------------------------------------------- zebrafish
add("Zebrafish larvae converge their eyes to hunt prey", ["B11", "S14"], """
Larval zebrafish begin hunting paramecia at about 5 days after fertilization, and the accessibility of their brains makes them a modern model for the circuits Ewert studied.

Bianco, Kampff and Engert found that every prey-capture routine begins with **eye convergence**: both eyes rotate nasally, and vergence stays high during tracking and the capture swim before relaxing after the strike. Convergence enlarges the region of binocular overlap in front of the fish, which the authors proposed allows stereoscopic targeting of prey.

In a virtual-reality assay, small moving spots (about 1°) evoked low-amplitude orienting turns toward the spot, whereas larger spots (10°) evoked high-amplitude turns away. As in toads, the response category depends on stimulus size. Semmelhack and colleagues distinguished the hunting **J-turn**, a bend that holds the tail in a J shape, from spontaneous swims.""",
[
    ["Zebrafish larvae hunt small paramecia from about five days old, and their transparent brains let us image the circuits.",
     ["Every hunt starts with both eyes turning inward, called eye convergence."]],
    ["The eyes stay converged during tracking and capture.",
     ["That increases the area seen by both eyes, which the authors suggest helps judge distance to the prey."]],
    "Small moving spots drew small turns toward them, while large spots drew big turns away. Just like the toad, size decides between prey and threat.",
],
figures=[fig("B11", "bianco11_f2", "2", "A larva hunting a paramecium (arrowhead), eye vergence at each stage (B–D), J-turn tail shapes (E–F) and prey distance at strike (G)."),
         fig("S14", "semm_f1", "1A–C", "Prey-capture forward swim, J-turn and spontaneous swim to virtual stimuli, with tail-position traces.")],
width=5.4, primary=3.2)

add("Small moving dots release zebrafish prey capture", ["S14", "BE15"], """
Semmelhack and colleagues presented virtual prey to semi-restrained larvae whose tails were free to move. They distinguished prey-capture **J-turns**, in which the tail is held in a J shape to turn toward prey, and forward swims from spontaneous swims, using a machine-learning classifier of tail kinematics.

A prey-capture score was tuned to stimulus size and speed: it peaked for dots of about 3° moving at about 90–100°/s, and fell sharply for dots of 10° or more.

Bianco and Engert combined such a virtual hunting assay with two-photon calcium imaging of the tectum. Hunting responses depended on combinations of features: size, speed and contrast polarity. The tuning parallels the toad's preference for small, elongated objects moving along their axis.""",
[
    ["Semmelhack and colleagues showed virtual dots to larvae held in agarose with the tail free.",
     ["A computer classifier separated hunting movements, like J-turns, from ordinary swimming."]],
    ["Hunting was tuned to the dot.",
     ["It peaked for dots about 3 degrees across moving at about 90 to 100 degrees per second and dropped off for big dots."]],
    "Bianco and Engert imaged the tectum during the same kind of task and found that hunting depends on combinations of size, speed and contrast, a modern version of Ewert's configurational rules.",
],
figures=[fig("S14", "semm_f2", "2", "Prey-capture score versus dot diameter (A) and speed (B) in semi-restrained larvae."),
         fig("BE15", "be15_f1", "1", "Two-photon imaging during virtual hunting: setup, eye positions before and after convergence, and tectal imaging field.")],
width=5.8, primary=2.6)

add("Pretectal area AF7 responds to prey-sized dots", ["S14"], """
Retinal ganglion cell axons in zebrafish end in ten **arborization fields (AF1–AF10)**; AF10 is the tectum. Semmelhack and colleagues imaged calcium in retinal axons while presenting the optimal prey stimulus.

Only **AF7**, a small pretectal field, responded strongly to a 2° dot. AF9 responded to a 10° dot instead. AF7's size tuning matched the behavioral prey-capture curve, whereas AF9's increased with size, and both were tuned to speed.

AF7 is innervated by two types of retinal ganglion cells that also send collaterals to the tectum. A dedicated pretectal channel for prey-sized objects therefore exists in fish, at the same level of the visual system as the toad's pretectal region.""",
[
    ["In zebrafish, retinal axons end in ten areas called arborization fields, and AF10 is the tectum.",
     ["Imaging calcium in the retinal axons showed which areas respond to prey."]],
    ["Only AF7, in the pretectum, responded strongly to a small 2-degree dot.",
     ["AF9 responded to larger dots instead, and AF7's size tuning matched the hunting behavior."]],
    "So fish have a pretectal channel tuned to prey-sized objects, fed by retinal cells that also send branches to the tectum.",
],
figure=fig("S14", "semm_f3", "3A–G", "Retinal arborization fields; AF7 responds to a 2° dot but AF9 to a 10° dot (color ΔF/F); size and speed tuning."),
width=4.4)

add("AF7 ablation impairs prey capture, not optomotor turning", ["S14"], """
To test whether AF7 is needed, Semmelhack and colleagues laser-ablated the retinal axons in AF7 or, as a control, in AF9.

After AF7 ablation, prey-capture bouts (shaded in the tail traces) were greatly reduced, and the time spent in prey capture fell to about 40% of pre-ablation levels. AF9 ablation left prey capture unchanged.

The **optomotor response**, swimming in the direction of moving gratings, was unaffected by AF7 ablation but reduced after AF9 ablation. AF7 is therefore selectively required for prey capture. Semmelhack and colleagues also found neurons with arbors in AF7 that projected to the tectum, the nucleus of the medial longitudinal fasciculus and the hindbrain.""",
[
    ["Next, the AF7 axons were destroyed with a laser, and AF9 was destroyed in other fish as a control.",
     ["Losing AF7 cut prey capture to about 40 percent, while losing AF9 had no effect on it."]],
    ["The optomotor response, swimming with moving stripes, showed the reverse.",
     ["It was spared after AF7 ablation and reduced after AF9 ablation."]],
    "So AF7 is specifically needed for hunting, and neurons reading out AF7 project to the tectum and to premotor areas.",
],
figure=fig("S14", "semm_f6", "6", "AF7 before and after ablation (A–B); tail traces with prey-capture bouts (C–D); prey capture and optomotor response after AF7 or AF9 ablation (E–H)."),
width=4.6)

add("Tectal neurons combine features nonlinearly", ["BE15"], """
Bianco and Engert imaged thousands of tectal neurons with GCaMP while larvae responded to moving spots that varied in size, speed, contrast polarity and direction.

They identified neurons tuned like the behavior: responsive to small, dark or bright, moving spots at hunting speeds, either regardless of direction or selective for left-to-right or right-to-left motion. These neurons showed **nonlinear mixed selectivity**: they responded strongly only to particular combinations of features, rather than summing feature preferences independently.

Comparing trials with and without a hunting response, they found small tectal assemblies whose activity preceded eye convergence. Bianco and Engert proposed that such neurons mediate prey recognition and that their premotor activity releases hunting. This parallels Ewert's T5.2 neurons, whose bursts predicted orienting.""",
[
    ["Bianco and Engert imaged thousands of tectal neurons at once while fish watched moving spots.",
     ["Some neurons were tuned like the behavior, to small spots moving at hunting speeds, some in any direction and some in one direction only."]],
    ["These cells needed the right combination of features, not just one.",
     ["That is called nonlinear mixed selectivity, and it is the kind of combining Ewert inferred for T5.2 neurons."]],
    "Small groups of tectal neurons became active just before the fish converged its eyes, which suggests they help trigger the hunt, much like the T5.2 bursts before orienting in toads.",
],
figure=fig("BE15", "be15_f5", "5A", "Calcium responses of tectal neurons selected by behavioral tuning regressors, grouped by direction and speed selectivity."),
width=5.6)

add("Anterior tectum is tuned to prey at close range", ["F20"], """
Prey is first seen in the peripheral visual field, which maps to the posterior tectum. As the larva turns and approaches, the prey image moves into the central binocular field, mapped to the anterior tectum, and appears larger.

Förster and colleagues imaged tectal neurons and found that cells responding to a small 5° dot, especially direction-selective ones, were concentrated in posterior and medial tectum. Cells tuned to a larger 30° dot were concentrated anteriorly, and anterior neurons were frequently not direction-selective.

The tectal map is therefore specialized by location for different stages of the hunt. Ablating tectal neurons tuned to large objects impaired hunting, indicating that the close-range representation is needed for capture.""",
[
    ["Prey is first seen off to the side, which maps onto the back of the tectum, and as the fish approaches, the prey moves to the front of the visual field and looks bigger.",
     ["Förster and colleagues asked whether the tectum is organized for this."]],
    "Cells for small dots, especially direction-selective ones, sat in the posterior tectum, while cells for larger dots sat in the anterior tectum and were often not direction-selective.",
    "Killing the large-object cells impaired hunting, so the tectal map is laid out for distant prey in one place and close prey in another.",
],
figure=fig("F20", "forster_f6", "6", "Positions of 30°-dot (blue), 5°-dot (red) and direction-selective 5°-dot (yellow) cells along the tectum; their neurite traces."),
width=5.8)

add("Single pretectal neurons can command hunting", ["A19"], """
Antinucci, Folgueira and Bianco imaged neurons across the larval brain during virtual hunting. A discrete region near AF7, the **AF7-pretectum**, contained a high density of neurons active specifically when larvae initiated hunting.

Using the KalTA4u508 line, they labeled two classes of these pretectal neurons, projecting to the ipsilateral tectum or to the contralateral tegmentum. **Optogenetic** stimulation of a single neuron of either class, using the light-gated channel CoChR, induced sustained hunting sequences, with eye convergence and J-turns, in the absence of prey.

Laser ablation of these neurons impaired prey-catching and prevented hunting evoked by stimulating the anterior-ventral tectum. The authors proposed that they form a **command system** for predatory behavior, a pretectal role unlike the inhibitory one Ewert described for non-prey.""",
[
    ["Antinucci and colleagues found a small pretectal region whose neurons became active when fish started to hunt.",
     ["Two classes project to the tectum or to the tegmentum."]],
    ["Activating just one of these neurons with light was enough to start a full hunting sequence, eye convergence and J-turns, with no prey present.",
     ["Removing them reduced prey-catching and blocked hunting triggered from the tectum."]],
    "These pretectal cells work like a command system for hunting. In toads, the pretectum mainly vetoes non-prey; in fish, part of it starts the hunt.",
],
figures=[fig("A19", "antin_f2", "2A–B", "Brain maps of prey-responsive and hunting-initiation neuron clusters; the AF7-pretectum is outlined."),
         fig("A19", "antin_f5", "5A–C", "Optogenetic stimulation of a single KalTA4u508 pretectal neuron (B) induces hunting with eye convergence (C).")],
width=5.8, primary=2.6)

add("The nucleus isthmi sustains pursuit after hunting starts", ["H19"], """
The **nucleus isthmi (NI)** is a cholinergic nucleus reciprocally connected with the tectum; in amphibians its homolog has long been implicated in tectal function. Henriques and colleagues traced two types of NI projection neuron in zebrafish: type I projects ipsilaterally to retinorecipient laminae of tectum and pretectum, including AF7, and type II projects to both tectal hemispheres.

After laser ablation of NI, larvae detected prey and initiated hunting as often as controls, but they failed to sustain prey-tracking sequences: the abort rate rose from 0.60 to 0.80 and the capture rate fell from 0.36 to 0.16. Ablated larvae consumed fewer paramecia.

NI neurons became more active after hunting began. The authors proposed that NI provides state-dependent feedback facilitation to tectum and pretectum during pursuit.""",
[
    ["The nucleus isthmi is a cholinergic nucleus wired in loops with the tectum.",
     ["One type of isthmic neuron projects to the tectum and pretectum on the same side, and another to both tectal halves."]],
    ["Without the nucleus isthmi, fish still noticed prey and started hunting.",
     ["But they gave up more often: aborted hunts went from 60 to 80 percent and captures from 36 to 16 percent."]],
    "So this nucleus helps keep the pursuit going once it has started, by boosting tectal and pretectal activity during the hunt.",
],
figure=fig("H19", "henriques_f2", "2", "Traced type I and type II nucleus isthmi projection neurons and their targets in tectum and pretectum (AF7)."),
width=5.2)

add("Pretectal prey detectors drive a hypothalamic feeding center", ["M17"], """
Muto and colleagues imaged calcium in freely swimming larvae. The **inferior lobe of the hypothalamus (ILH)**, a feeding center, became active when a larva converged its eyes on prey and rose further after capture.

Pretectal neurons were activated by paramecia: their activity rose as a larva approached prey, and in restrained larvae they responded best to virtual spots about 2–5° in size moving at intermediate speeds, matching the sizes and speeds of captured prey.

Single labeled pretectal neurons sent axons to the ILH, and pretectal and ILH activity were correlated. Ablation of the pretectum completely abolished prey capture, and silencing ILH neurons reduced feeding. The authors proposed that this pretecto-hypothalamic pathway converts visual prey detection into feeding motivation, linking recognition to the motivational state that, in toads, gates T5.2 responses.""",
[
    ["Muto and colleagues watched the hypothalamic feeding center, the inferior lobe, in swimming larvae.",
     ["It switched on when the larva converged its eyes on prey and rose further after the catch."]],
    ["Pretectal neurons responded to paramecia and to virtual spots of prey size and speed.",
     ["Single pretectal neurons sent axons to the feeding center, and their activity was correlated with it."]],
    "Removing the pretectum abolished prey capture. The authors proposed that this pathway turns seeing prey into the motivation to feed, the same kind of motivational state that in toads controls how strongly T5.2 neurons respond.",
],
figure=fig("M17", "muto_f2", "2a–h", "Pretectal (PT) calcium responses to paramecia during hunting; tuning to spot diameter (g) and speed (h)."),
width=5.0)

assert len(slides) == 44, len(slides)
for s in slides:
    w = len(" ".join(s["body"]).split())
    assert 85 <= w <= 175, (s["title"], w)

items = [
    ("Prey is defined by configuration.", "Toads prefer objects elongated along their direction of movement (worms) and reject the same objects moving across it (antiworms); the rule is invariant to direction, contrast and, within limits, speed."),
    ("No single cell is a worm detector.", "Retinal ganglion cells (R2–R4) encode size and contrast; tectal T5(2) neurons are selective in the same way as behavior, but no neuron is specific to one configuration."),
    ("Pretectal inhibition sharpens tectal selectivity.", "Pretectal TH3 neurons prefer large and antiworm stimuli; pretectal lesions or NPY block make T5.2 neurons and behavior respond to non-prey."),
    ("Forebrain loops gate and modify recognition.", "The striatum disinhibits the tectum via the pretectum to release prey-catching; the ventral medial pallium (hippocampus) alters prey selectivity after learning; dopamine shifts hunting to waiting."),
    ("Behavior emerges from sensorimotor codes.", "Combinations of tectal and pretectal streams, filtered by motivation, select turning, snapping or avoidance in medullary motor circuits."),
    ("Fish reveal the same logic at cellular level.", "Zebrafish prey detection uses a pretectal AF7 channel, tectal neurons with nonlinear mixed selectivity and pretectal command neurons that can start hunting."),
]

spec = {
    "lecture": 9,
    "content_slides": 44,
    "theme": "sapphire-silver",
    "title_image": {
        "path": "figures/title_toad.jpg",
        "caption": "Photo: Common toad (Bufo bufo), the species used in Ewert's prey-catching studies.",
        "credit": "George Chernilevsky",
        "license": "Public domain",
        "source_url": "https://commons.wikimedia.org/wiki/File:Bufo_bufo_2009_G1.jpg",
        "kind": "web",
    },
    "slides": slides,
    "takeaways": {"items": [{"lead": l, "text": t} for l, t in items],
                  "cite": "Ewert et al. (1978); Ewert (1997); Ewert et al. (2001); Semmelhack et al. (2014)",
                  "refs": [ref(k) for k in R]},
}
(HERE / "lecture.json").write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n")
print("Wrote", len(slides), "content slides")
