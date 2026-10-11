"""Scaffold spec for Lecture 38 (Drive deck Neuroethology_Lecture38_FA2026.pptx). Body rewrites are in body_L38.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L38 as _body  # noqa: E402

SEY = ["Seyfarth 1980", "Seyfarth 1980|Animal"]


def ins(after, title, paragraphs, citation, notes, refs):
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Leopard alarms draw monkeys into trees", [
        "Leopards hunt by ambush on the ground, so a monkey that is feeding or moving low is exposed to attack. In Amboseli, vervet monkeys answered leopard alarms by running into trees. The destination of the escape distinguishes the leopard response from a general reaction to alarm sounds.",
        "Playback used a concealed speaker, and no leopard was present during the trials. Investigators filmed the same recipients before and after each call. Monkeys on the ground ran into trees more often after leopard alarms than after the other alarm categories.",
        "An alarm can therefore start an appropriate escape before any visual identification of the predator. The call guides where the monkey goes as well as how soon it moves. Escape location mattered in these observations, so the sound carried information about refuge as well as danger.",
    ], "Seyfarth et al. (1980a); Seyfarth et al. (1980b)", [
        "Leopard alarms draw monkeys into trees.",
        ["Ambush.", "Leopards are terrestrial ambush predators, so an attack can approach a monkey feeding or moving across the ground.", "A monkey in the open is exposed, and the escape route matters.", "In Amboseli, leopard-associated alarm calls were followed by movement into trees."],
        ["Playback.", "The calls were broadcast from a concealed speaker.", "No leopard was present during the trials.", "The investigators filmed each recipient before and after the call, so each monkey served as its own baseline."],
        ["Result.", "Ground-dwelling subjects were more likely to run into trees after leopard alarms.", "The other alarm categories produced different movements.", "Escape location therefore mattered, rather than movement alone."],
        ["Visual cue.", "An alarm alone could initiate an appropriate escape.", "The predator did not need to be identified visually first.", "The sound supplied the information that started the movement."],
        ["Meaning.", "The behavior shows an acoustic contribution to defensive action.", "Refuge choice is part of the response that the call organizes.", "The result comes from observed movements of the monkeys in the field."],
    ], SEY),
    ins(6, "Spectrograms separate the three alarm calls", [
        "Leopard, eagle and snake calls from identified monkeys can be displayed on identical time and frequency axes. That shared layout turns each call into a pattern that can be read and compared. Tonal structure, duration and repeated units then stand out in every category.",
        "Eagle alarms showed low-frequency components in these displays. Snake alarms carried a higher-pitched chutter structure, while leopard calls combined short tonal units with repeated sequences. The frequency range shown for the examples ran from 80 to 8000 Hz.",
        "Because the differences are audible, the calls carry acoustic information before any playback begins. Acoustic distinctness gives discrimination a physical basis. Playback experiments then ask how monkeys act once they hear those sounds.",
    ], "Seyfarth et al. (1980b)", [
        "Spectrograms separate the three alarm calls.",
        ["Display.", "A spectrogram shows acoustic energy across time and frequency.", "Each call category leaves its own pattern on the display.", "Tonal structure, duration and repeated units are visible."],
        ["Settings.", "A 300 Hz analysis filter was used for these examples.", "Frequency displays extended from 80 to 8000 Hz.", "The same axes allow the categories to be compared directly."],
        ["Categories.", "Eagle alarms contained low-frequency components.", "Snake alarms had higher-frequency chutter structure.", "Leopard calls included short tonal units or repeated sequences."],
        ["Field listening.", "Listeners in the field detected these differences.", "The distinctions exist in the sounds the monkeys hear.", "Discrimination rests on acoustic cues that are present in the calls."],
        ["Meaning.", "Playback tests the behavioral consequences of hearing the sounds.", "The recordings give the acoustic basis for those tests.", "Both lines of evidence are needed to link sound and response."],
    ], SEY),
    ins(9, "Duration alone leaves category differences intact", [
        "Duration is one property that differs between versions of one call. Natural recordings let investigators build short and long versions while preserving the characteristic structure of each alarm category. A longer call often contains more repeated units than a shorter one.",
        "The short stimuli were about 0.3 s long, with one acoustic unit each. The long stimuli ran about 3.7 s and held roughly five units. Each caller contributed matched recordings, which kept caller identity constant across versions, and playback then measured the response to each length.",
        "The category differences survived the change in length. Length therefore contributes less to the response category than other properties do. Urgency and response size, however, can change with length, separately from which action is chosen.",
    ], "Seyfarth et al. (1980b); Seyfarth et al. (1980a)", [
        "Duration alone leaves category differences intact.",
        ["Duration.", "Duration is the time a vocalization occupies.", "A longer call can also contain more repeated units.", "Natural recordings made both short and long versions possible."],
        ["Stimuli.", "Short versions averaged 0.3 s and held one acoustic unit.", "Long versions averaged 3.7 s and held about five units.", "Each version kept the structure typical of its alarm category."],
        ["Control.", "Matched recordings came from the same caller.", "Caller identity was kept separate from duration.", "The playback measured the defensive response to each version."],
        ["Result.", "The main differences between response categories persisted.", "Duration therefore accounts for little of the category differences.", "The leopard, eagle and snake responses stayed distinct."],
        ["Meaning.", "Urgency and response magnitude still change with duration.", "These measures vary independently of the action selected.", "The type of action is set by other features of the call."],
    ], SEY),
    ins(12, "Infants give eagle alarms to many birds", [
        "Infant monkeys in Amboseli gave eagle alarms to many birds, and sometimes to harmless objects. Adults limited these alarms to dangerous aerial species, including martial eagles. That narrowing with age is the developmental change documented in this study.",
        "Records from the 14-month study tie each infant, juvenile or adult call to the object that triggered it. Infant errors had structure: aerial objects drew eagle calls, terrestrial mammals drew leopard calls, and long thin objects drew snake calls.",
        "Calls become tied to fewer, more dangerous species as monkeys mature. The change refines categories that infants already use, so the broad categories come first and the narrow ones follow with experience. Juveniles fall between the infant and adult patterns along the same path.",
    ], "Seyfarth et al. (1980a)", [
        "Infants give eagle alarms to many birds.",
        ["Ontogeny.", "Ontogeny is change during an individual's development.", "Infant alarms covered a broad range of stimuli.", "Some infant alarms were given to harmless objects."],
        ["Adults.", "Adult callers restricted eagle alarms more strongly.", "The restriction favored dangerous aerial species.", "Martial eagles were among the species that adults alarmed to."],
        ["Errors.", "Infant errors followed a category structure.", "Aerial stimuli tended to draw eagle calls.", "Terrestrial mammals tended to draw leopard calls, and long thin objects drew snake calls."],
        ["Juveniles.", "Juvenile patterns fell between infant and adult patterns.", "Calling became more selective with age.", "The 14-month field records linked each call to its eliciting object."],
        ["Meaning.", "Development refines broad categories.", "Experience narrows the set of stimuli that trigger each call.", "The developmental change is a refinement rather than a new discrimination."],
    ], ["Seyfarth 1980|Animal"]),
    ins(15, "Element duration differs across predator contexts", [
        "Duration and spacing make up the temporal side of a call, and energy spread across frequencies makes up the spectral side. The analysis measured both sides in the same recordings, so no single frequency or duration defined an alarm type.",
        "Individual elements were longest in calls given to terrestrial predators. Their mean duration was 107.7 ms. Aerial encounters averaged 43.9 ms and snake encounters averaged 38.3 ms, values that describe single elements rather than whole bouts.",
        "Each feature contributes part of the information in the call, and no single feature forms a perfect boundary. Attributing the discrimination to one feature requires playback in which that feature alone is changed. Such playback tests connect a specific acoustic change to the behavior that follows it.",
    ], "Price et al. (2015)", [
        "Element duration differs across predator contexts.",
        ["Features.", "Temporal and spectral features were measured together.", "Duration and spacing describe timing.", "Energy distribution describes the spectrum."],
        ["Elements.", "Terrestrial elements were longer than aerial and snake elements.", "Element durations were reported in milliseconds.", "The values refer to elements, not to whole bouts."],
        ["Values.", "Terrestrial encounters averaged 107.7 ms per element.", "Aerial encounters averaged 43.9 ms.", "Snake encounters averaged 38.3 ms."],
        ["Bouts.", "A bout can contain successive vocalizations.", "Element measures are a different unit from the bout.", "Each measure describes a different biological level."],
        ["Meaning.", "Several features support discrimination together.", "Playback manipulations isolate a single feature.", "The combined features give listeners more than one cue."],
    ], ["Price 2015"]),
    ins(18, "Aggressive calls overlap predator call forms", [
        "Price and colleagues looked at aggressive recordings from both within-group and between-group conflicts. When those calls joined the female predator-call set, snake and aerial calls overlapped with them. A single call type therefore no longer matched a single predator.",
        "The chutter-like snake sounds looked acoustically similar to some intergroup calls. The rraup-like aerial sounds also matched sounds from escalated aggression. Between-group and within-group peak frequencies averaged 1715 Hz and 1456 Hz, values inside the predator range.",
        "Recipients therefore need more than the call form to decide what it means. Additional acoustic details and the immediate social situation give them that information. Each source adds a different kind of information to the same call form. The overlap gives listeners ambiguous cues in some cases.",
    ], "Price et al. (2015)", [
        "Aggressive calls overlap predator call forms.",
        ["Aggression.", "Aggression includes antagonistic interactions within and between groups.", "Aggressive recordings were added to the female analysis.", "The added recordings came from the same study system."],
        ["Overlap.", "Snake calls with a chutter-like sound resembled some intergroup calls.", "Aerial calls with a rraup-like sound resembled escalated aggression.", "The overlap weakens a one-call, one-predator description."],
        ["Peaks.", "Between-group aggression had a mean peak of 1715 Hz.", "Within-group aggression had a mean peak of 1456 Hz.", "Both values fall within the range of predator-associated calls."],
        ["Recipients.", "Additional acoustic details shape the response.", "Current circumstances also shape the response.", "Recipients combine several sources of information."],
        ["Meaning.", "Context must be inferred from several features.", "Production context cannot always be read from structure alone.", "The same call form can appear in different settings."],
    ], ["Price 2015"]),
    ins(21, "Male snake and eagle calls share frequencies", [
        "In the male recordings, some low-frequency calls appeared in both eagle and snake encounters. The three published clusters lined up only roughly with the predator categories. Some calls appeared in two categories at once. Some calls were therefore shared across predator contexts.",
        "Male element durations averaged 76.5 ms in aerial calls, 61.1 ms in snake calls and 112.0 ms in terrestrial calls. The corresponding peak frequencies were 1090 Hz, 1639 Hz and 1904 Hz, so the two measures separate the contexts together.",
        "Individual calls can land inside the shared range even when the averages differ. Listeners may weigh several features together, along with other environmental cues, when they respond. Averages alone leave some calls in the overlap. Averages describe the recordings, not each individual call.",
    ], "Price et al. (2015)", [
        "Male snake and eagle calls share frequencies.",
        ["Overlap.", "Some low-frequency calls occurred in eagle and snake encounters.", "The clusters matched the predator categories imperfectly.", "Similar feature ranges arise in different contexts."],
        ["Duration.", "Aerial male elements averaged 76.5 ms.", "Snake elements averaged 61.1 ms.", "Terrestrial elements averaged 112.0 ms."],
        ["Frequency.", "Male peak frequencies averaged 1090 Hz for aerial calls.", "Snake calls averaged 1639 Hz.", "Terrestrial calls averaged 1904 Hz."],
        ["Meaning.", "Averages differ across the contexts.", "Individual calls can fall inside the overlap.", "Listeners may combine several features with environmental information."],
    ], ["Price 2015"]),
    ins(24, "Male barks occur in leopard and social contexts", [
        "Male barks appear in two very different settings, leopard threats and social conflict. Price and colleagues compared real leopard encounters, leopard-model presentations and aggression among males. Each context produced its own acoustic distribution in the analysis.",
        "Acoustic scores for each context form their own distribution, displayed here on a 0.2 s reference scale. The calls from real leopard encounters sit closer to the aggressive barks than the calls from models do. Those distributions overlap in the middle, where the same call form appears in both settings.",
        "The same call form therefore carries information about a social state, not only about a predator. Recipients can use it to learn about either situation. Its meaning therefore depends on the situation in which it is heard. Predator-linked uses are one part of that broader pattern.",
    ], "Price et al. (2015)", [
        "Male barks occur in leopard and social contexts.",
        ["Barks.", "Barks are associated with terrestrial threats.", "They also occur in antagonistic social interactions.", "The same general call form appears in both settings."],
        ["Recordings.", "Real leopard encounters were analyzed.", "Leopard-model presentations were included.", "Social aggression recordings were analyzed in the same study."],
        ["Similarity.", "Calls to real leopards resembled aggressive barks.", "Calls elicited by leopard models were less similar.", "The comparison used the available recordings."],
        ["Meaning.", "A bark can signal a social state.", "Recipients can use the bark as information about either meaning.", "Production specificity must account for this social use."],
    ], ["Price 2015"]),
    ins(27, "Sparse sampling reduces scanner noise", [
        "Functional MRI records blood-oxygenation changes that follow neural activity. The scanner is loud, so the stimulus has to be separated from that noise. Sparse sampling places acquisition after a quiet interval, which keeps the stimulus clear of the scanner sound. The stimulus and the scanner noise therefore occupy separate intervals.",
        "Each stimulus was followed by a 6 s delay before the first volume, and every volume lasted 2.18 s. Sound and silence trials alternated, so each response had a silent baseline in the same session. Acquisition followed the stimulus by a fixed interval.",
        "Sparse sampling makes the auditory response measurable in the first place. Localization is the strength of this method, while the timing of a single decision and synaptic detail require other measurements. The strength of the method lies in tracing where sound-driven activity appears.",
    ], "Ortiz-Rios et al. (2015)", [
        "Sparse sampling reduces scanner noise.",
        ["Signal.", "Functional MRI tracks changes in blood oxygenation.", "The signal is not a spike-level measure.", "Blood oxygenation follows neural activity with a delay."],
        ["Sampling.", "Quiet intervals precede each image volume.", "Stimulation occurs in the gaps between acquisitions.", "The gaps reduce interference from the scanner."],
        ["Timing.", "Acquisition began 6 s after stimulus onset.", "Each image volume took 2.18 s.", "Sound and silence trials alternated."],
        ["Attention.", "One macaque performed an auditory task with eye movements.", "The other listened during maintained fixation.", "Attention therefore differed between the two animals."],
        ["Meaning.", "The signal localizes sound-sensitive regions.", "Synaptic detail needs other methods.", "Sparse sampling makes the auditory response measurable."],
    ], ["Ortiz-Rios 2015"]),
    ins(30, "The right hemisphere shows the larger response", [
        "The two sides of the brain can be compared by anatomical section and by regional blood-oxygenation response. Ortiz-Rios and colleagues did this in both macaque hemispheres, so the result rested on measured responses rather than on one visible patch.",
        "In both animals, complex sounds drove a stronger response on the right side under these conditions. Calibration at about 80 dB sound pressure level set the stimulus strength, and silence provided the baseline for each measured value. Both animals showed the same right-side pattern under this design.",
        "The right-side advantage depends on the sounds and the imaging conditions used. Attention differed between the two animals, so each contrast brings out a different part of auditory processing. Response size and behavioral necessity are separate questions that need separate measures.",
    ], "Ortiz-Rios et al. (2015)", [
        "The right hemisphere shows the larger response.",
        ["Lateralization.", "Lateralization is an unequal response between the two sides.", "Both hemispheres were compared in each macaque.", "The comparison used anatomical sections."],
        ["Measures.", "Regional blood-oxygenation responses were measured.", "A single visible activation patch was not the basis for dominance.", "Each side was assessed by its measured response."],
        ["Result.", "Both animals responded more strongly on the right to complex sounds.", "The sounds were calibrated to about 80 dB.", "Silence trials provided the baseline for each comparison."],
        ["Meaning.", "The response pattern depends on the sound set and imaging conditions.", "Attention differed between the two animals.", "Each contrast emphasizes different components of processing."],
    ], ["Ortiz-Rios 2015"]),
    ins(33, "Anterior temporal regions respond to intact calls", [
        "Converging results carry more weight than a single comparison. Ortiz-Rios and colleagues combined two contrasts, call versus environmental sound and call versus scrambled call, then searched for regions that responded to both in the macaques.",
        "The shared region sat in the anterior temporal cortex, including lateral rostrotemporal areas and the rostrotemporal pole. Stimuli were 8 s sequences, and acquisition began 6 s in, which set the timing of each measured response. The map then places that response on the anatomy.",
        "Convergence across two independent controls narrows the explanation toward vocal processing. Environmental sounds alone would give a broader picture, which is why the two-control design matters. Each control removes a different alternative explanation.",
    ], "Ortiz-Rios et al. (2015)", [
        "Anterior temporal regions respond to intact calls.",
        ["Analysis.", "A conjunction analysis finds regions shared by several comparisons.", "A result must hold across multiple controls.", "The macaques were examined for convergence."],
        ["Comparisons.", "Calls were tested against environmental sounds.", "Calls were also tested against scrambled calls.", "Each comparison isolates a different aspect of the sounds."],
        ["Result.", "The anterior temporal regions were the strongest shared result.", "The rostrotemporal pole was included in that result.", "Stimuli were 8 s sequences with acquisition beginning after 6 s."],
        ["Anatomy.", "Lateral rostrotemporal cortex was part of the convergence.", "The anatomical map localizes the blood-oxygenation response.", "The response was retained across the comparisons."],
        ["Meaning.", "The convergence points to vocal processing.", "The result narrows the explanations for macaque communication.", "Comparative specialization constrains how macaque brains process calls."],
    ], ["Ortiz-Rios 2015"]),
    ins(36, "Leopard chirps are longer, with higher peaks", [
        "Leopard and snake models each elicited chirps in this green-monkey study, and the chirps were analyzed by context. Duration and an early peak-frequency measure together did most of the work of separating the two groups. The chirps were analyzed as continuous measurements rather than as fixed types.",
        "Chirps given to leopard models lasted longer and reached a higher early peak than those given to snake models. Scores were tabulated in milliseconds and Hz, and their distributions formed a continuum between the two groups. Many individual chirps sat in the middle of that range.",
        "The physical variation is present in the sounds themselves. Whether a listener treats a middle chirp as a leopard threat, a snake threat or a reason to inspect depends on reception and decision processes beyond the acoustic analysis. Physical differences set the input, and the listener's processes set the decision.",
    ], "Price & Fischer (2014)", [
        "Leopard chirps are longer, with higher peaks.",
        ["Measures.", "Duration and early peak frequency did most of the separating.", "Both measures were scored for each chirp.", "Durations were in milliseconds and frequencies in Hz."],
        ["Leopard chirps.", "Leopard-associated chirps were longer than snake-associated chirps.", "They had a higher early peak frequency.", "The analysis was run on green-monkey recordings."],
        ["Distributions.", "Scores overlapped across the two contexts.", "The overlap formed a continuum rather than two groups.", "Individual chirps can sit between the two contexts."],
        ["Meaning.", "Physical variation is detectable within one call form.", "Reception determines how a listener responds to intermediate chirps.", "The analysis captures the input rather than the decision."],
    ], ["Price 2014|Fischer"]),
    ins(39, "Prior predator evidence extends time in trees", [
        "Persistence and immediate climbing answer different questions about the same broad alarm. One asks what a monkey does first, and the other asks how long it stays in the tree. Prior evidence can affect the second even when the first follows the acoustics.",
        "When both the leopard model and the leopard chirps signaled terrestrial danger, subjects remained in trees longer. Persistence meant staying more than 200 s, whereas the immediate response meant climbing above 2 m after the broadcast.",
        "Early action follows the call's acoustics, while persistence also reflects earlier information about the threat. The two measures therefore differ in what they reveal about the same call. Each measure adds its own information to that call. Both measures were taken from the same subjects in the same study.",
    ], "Price & Fischer (2014)", [
        "Prior predator evidence extends time in trees.",
        ["Persistence.", "Persistence is the time a defensive state continues after it begins.", "It was measured against a 200 s threshold.", "Subjects that stayed more than 200 s were counted."],
        ["Immediate.", "Immediate climbing was scored above 2 m.", "It followed the broadcast directly.", "It is a different measure from persistence."],
        ["Priming.", "Leopard-model exposure supported terrestrial danger.", "Leopard-associated chirps supported the same danger.", "Both sources were present together in the persistence condition."],
        ["Meaning.", "Prior evidence shapes sustained risk assessment.", "Early action can follow the acoustics alone.", "The two measures carry different information about one call."],
    ], ["Price 2014|Fischer"]),
    ins(42, "Ongoing conflict reduces looking at the caller", [
        "Looking toward a caller can help a listener work out what caused an alarm. Deshpande and colleagues played the same male bark to recipients, with and without an intergroup encounter going on, and timed how long each one looked at the speaker.",
        "Looks were longest when the surrounding situation contained no conflict. Times were recorded in seconds across 10 min of field observation. Social activity already explained the barking during an encounter, which may reduce the need to look toward the speaker.",
        "Integrating the bark with the surrounding social context shapes how long recipients keep looking. Reading the longer looks as uncertainty is a proposed interpretation, and it sits apart from any measured mental state. The social setting alone changes between the two conditions.",
    ], "Deshpande et al. (2023)", [
        "Ongoing conflict reduces looking at the caller.",
        ["Seeking.", "Information seeking involves orienting toward the caller.", "It can yield cues about the cause of an alarm.", "The caller's direction is the target of the look."],
        ["Comparison.", "The same bark was heard with and without an intergroup encounter.", "Looking duration was the measure.", "The bark stayed constant across both conditions."],
        ["Result.", "Looking was longer when no encounter was underway.", "Field observation continued for 10 min after playback.", "Looking time was measured in seconds."],
        ["Context.", "Social activity during an encounter offers an explanation for barking.", "That explanation reduces the need to look toward the caller.", "The reduction is consistent with integration of context."],
        ["Meaning.", "Acoustic and contextual information are integrated.", "Longer looking is a proposed sign of uncertainty.", "The behavior is a reading of the animal's state, not a measured mental state."],
    ], ["Deshpande 2023"]),
]

# Extra speaker-note groups (taken from the source deck's text) so each insert's notes reach the 150-420 word range.
EXTRA_GROUPS = {
    3: ["Field setting.", "The leopard alarms were recorded in the Amboseli habitat of these monkeys.", "Recipients were on the ground, feeding or moving, when the calls were played."],
    6: ["Axes.", "Time runs along the horizontal axis and frequency along the vertical axis.", "The examples extend from 80 to 8000 Hz.", "Matching the axes makes duration and tonal structure comparable across categories."],
    9: ["Repeated units.", "A longer call can contain more repeated units than a shorter one.", "Matched recordings from one caller kept caller identity constant.", "Short and long versions preserved the structure of their category."],
    12: ["Juvenile pattern.", "Juvenile calling sat between the broad infant pattern and the selective adult pattern.", "The eagle-alarm comparison was built from alarms collected over the 14-month study.", "Age-related change is visible within that single data set."],
    15: ["Measurement levels.", "Element duration describes one component of a compound call.", "Bout-level measures describe the full vocalization sequence.", "The source analysis reports both levels for the same female calls.", "Element counts and element durations were reported together for snake and terrestrial calls.", "The two levels were kept separate in the analysis to avoid treating every duration as the same unit."],
    18: ["Source scales.", "The spectrograms of these calls use 0.2 s time scales and kHz axes.", "Mean peak frequencies are reported for between-group and within-group aggression.", "Both values fall inside the spread of predator-associated calls."],
    21: ["Cluster structure.", "Male recordings were analyzed separately from female recordings.", "The male solution had three clusters, while the female solution had four.", "Each cluster's association with predator contexts was not equally exclusive.", "The male clusters differed in repeated-element pattern and in spectral distribution.", "Low-frequency components marked the third male cluster.", "Averages describe the recordings rather than each individual call.", "Cluster boundaries come from the measured features."],
    24: ["Real and model encounters.", "Calls to real leopards came from actual encounters with the predator.", "Calls elicited by leopard models came from presentations of a model.", "Social aggression supplied a third context for the same call form.", "The South African recordings were compared across the three contexts.", "Spectrograms in the source keep a 0.2 s reference scale for all three."],
    27: ["Silence trials.", "Each sound condition alternated with silence trials.", "Silence provides the baseline for each measured response.", "Sparse sampling was chosen to reduce interference from the scanner.", "Each image volume followed a stimulus interval, so the sound and the acquisition were kept apart.", "The method was applied to awake macaques in the scanner."],
    30: ["Anatomical sections.", "Anatomical sections show where each measured activation sits.", "Regional blood-oxygenation responses were compared across the two hemispheres.", "Both animals showed the larger right-side response in this preparation.", "The contrast was built from the same complex-sound and silence conditions for both sides.", "The result describes one sound set and one imaging design."],
    33: ["Scrambling control.", "Scrambling rearranged 200 ms segments across time and frequency.", "The scrambled stimuli kept much of the local acoustic structure.", "Intact calls still produced stronger anterior temporal responses."],
    36: ["Chirp comparison.", "Leopard and snake models elicited chirps from the green-monkey population.", "Duration and early peak frequency contributed most to the separation.", "The two contexts overlapped rather than forming separate groups.", "The early peak frequency is one of the measures used in the score.", "Scores were compared between leopard-associated and snake-associated chirps."],
    39: ["Measurement.", "Persistence asked whether the subject stayed more than 200 s.", "Immediate climbing was scored above 2 m after the broadcast.", "Both measures were recorded in the same subjects.", "The immediate response and the persistence measure answer different questions about the same alarm.", "Both were tested after the same leopard-associated broadcast."],
    42: ["Field observations.", "Observations continued for 10 min after the playback.", "Looking duration was recorded in seconds.", "Recipients looked longer at the speaker when no encounter was underway."],
}
for _ins in inserts:
    _ins["notes"] = _ins["notes"] + [EXTRA_GROUPS[_ins["after"]]]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
