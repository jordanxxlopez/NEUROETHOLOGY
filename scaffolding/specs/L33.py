"""Scaffold spec for Lecture 33 (Drive deck Neuroethology_Lecture33_FA2026.pptx). Body rewrites are in body_L33.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L33 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, notes, refs):
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Spectrograms separate juvenile calls from adult calls", [
        "Juvenile begging and location calls differ in acoustic form from adult calls. The spectrogram of each vocalization shows its frequency structure over time, so each vocal category can be identified before any learning is tested.",
        "Adult calls and the adult song are measured with the same spectrographic display. Keeping the call and song categories separate prevents developmental results about song from being applied to calls.",
        "Sorting each recording into its category at the start of the analysis keeps the learning experiments focused on song. A result about song structure then describes the song repertoire, while the calls are described on their own terms.",
    ], "Marler (1970)", [
        "Vocal categories are identified from their acoustic form.",
        ["Juvenile calls.", "Begging and location calls are produced by young birds.", "Their spectrograms differ from adult calls."],
        ["Adult calls.", "Adult calls form a separate category from song.", "Each category is measured with the same display."],
        ["Separation.", "Categories are sorted at the start of the analysis.", "Song results do not carry over to calls."],
        ["Meaning.", "The spectrogram gives a reliable basis for classification.", "Learning is tested within the song category."],
    ], ["Marler 1970"]),
    ins(6, "Isolate songs keep a record of abnormal development", [
        "A **developmental series** is a set of recordings made at successive ages from the same bird. Marler recorded the isolates repeatedly, so each song can be compared with the songs that came before it. The series shows the path to the final form.",
        "Syllable structure in the isolates changed over the course of development before reaching its abnormal mature state. Each stage of that change is visible when the recordings are arranged by age. Final songs alone would hide the stages.",
        "The isolates' developmental records show how the abnormal pattern was built. Tracking the record from earlier to later stages links the mature song to its origin in isolation, rather than treating it as a fixed endpoint.",
    ], "Marler (1970)", [
        "A developmental series shows how the adult song was built.",
        ["Recordings.", "Each isolate was recorded at successive ages.", "The same bird is followed through development."],
        ["Stages.", "Syllable structure changed before the abnormal mature state.", "Each stage is visible when recordings are ordered by age."],
        ["Final songs.", "The final song alone hides the stages.", "The series makes the origin of the pattern visible."],
        ["Meaning.", "The abnormal adult song has a developmental history.", "The history links the mature song to isolation."],
    ], ["Marler 1970"]),
    ins(9, "Tutoring intervals set which copies are retained", [
        "A **tutoring interval** is the span of ages during which a pupil hears the model. Both of Marler's windows, days 8–28 and days 35–56, produced good copies in otherwise isolated males. Tutoring within either interval was therefore sufficient for detailed copying.",
        "The copies followed the training recordings closely, and the recordings stopped before the mature song appeared. The copied material must therefore have been retained through the interval rather than sung back during the tutoring itself.",
        "The retention pattern separates the timing of tutoring from the timing of performance. A model heard in one interval can shape a song that emerges far later, which makes the tutoring interval the key variable.",
    ], "Marler (1970)", [
        "The tutoring interval controls what the pupil retains.",
        ["Windows.", "Two age windows were tested, from days 8–28 and days 35–56.", "Both produced good copies."],
        ["Copies.", "The copies matched the training recordings closely.", "The recordings ended before the mature song."],
        ["Retention.", "Material was kept through the interval.", "It was later used in the mature song."],
        ["Timing.", "Learning and performance occur at different times.", "The interval is the key variable."],
    ], ["Marler 1970"]),
    ins(12, "Playback timing decides whether detailed copying occurs", [
        "Marler compared playback at several ages to ask when a recording can be stored as a song model. Early intervals produced detailed copies, whereas playback around or after 100 days did not. The **age of playback** is therefore the variable that changes the outcome.",
        "Developmental age changed the effect of the same kind of acoustic model. Each age group heard a conspecific model that was otherwise suitable for the species, so the difference lies in the bird's developmental stage rather than in the recording. The age groups were compared under the same playback schedule, which keeps the stimulus constant across the contrast.",
        "The contrast shows a window in which detailed song copying is possible. Recognizing that window makes it possible to compare early and late playback under the same procedure.",
    ], "Marler (1970)", [
        "Playback timing changes the outcome of song copying.",
        ["Early playback.", "Early intervals produced detailed copies.", "Copies matched the training model."],
        ["Late playback.", "Playback around or after 100 days produced no detailed reproduction.", "The model was otherwise suitable."],
        ["Stage.", "The difference reflects the bird's developmental stage.", "The recording itself is the same kind."],
        ["Window.", "A window for detailed copying can be identified.", "Early and late playback can be compared under one procedure."],
    ], ["Marler 1970"]),
    ins(15, "Two phases connect a model to later singing", [
        "The **sensory phase** is the period in which a pupil acquires information from its tutor. The **sensorimotor phase** follows, in which the bird uses that stored information to shape its own vocal output. The two phases can be separated by a long interval, and each one can be measured on its own terms.",
        "Marler's delayed imitation shows that the retained information can guide singing months after the tutor was heard. The review by Brainard and Doupe (2000) supports a separate requirement for auditory feedback during refinement.",
        "Each phase has its own requirement. Acquisition depends on the tutor's song, while refinement depends on the bird's ability to hear its developing output.",
    ], "Marler (1970); Brainard & Doupe (2000)", [
        "Acquisition and refinement are separate phases of learning.",
        ["Sensory phase.", "The pupil acquires information from its tutor.", "The information is kept for later use."],
        ["Sensorimotor phase.", "The bird uses stored information to shape its output.", "The phase follows a long interval."],
        ["Delayed imitation.", "Retained information guides singing months later.", "The model was heard well before singing."],
        ["Feedback.", "Hearing one's own output supports refinement.", "Each phase has its own requirement."],
    ], ["Marler 1970", "Brainard 2000"]),
    ins(18, "Swamp sparrows learn from recordings made in infancy", [
        "A **syllable** is a single discrete sound unit in the song. Marler and Peters used recordings whose syllable arrangements were known, which made the tutor material measurable. Each later syllable could then be compared with a specific training syllable, and the arrangement of the syllables in each training recording was known in advance.",
        "Later songs were compared with the training recordings and with an untrained comparison group. The same spectrographic procedure was applied to every bird, which keeps the comparison consistent across pupils.",
        "A match between a later syllable and a known training syllable supports storage of the training material. That correspondence links the adult song to the infant recordings instead of to a fixed species template.",
    ], "Marler & Peters (1981)", [
        "Known training syllables make the tutor material measurable.",
        ["Syllables.", "A syllable is a single discrete sound unit.", "Training recordings had known syllable arrangements."],
        ["Comparison.", "Later songs were compared with the training material.", "An untrained group served as the baseline."],
        ["Procedure.", "The same spectrographic procedure was used for every bird.", "Results are comparable across pupils."],
        ["Storage.", "A match supports storage of the training material.", "The adult song links to the infant recordings."],
    ], ["Marler 1981"]),
    ins(21, "Plastic syllables are refined into stable adult song", [
        "**Syllable stability** is the consistency of a syllable's form across repeated renditions. Marler and Peters judged stability by comparing renditions over time, so a syllable counts as stable only when it recurs in a consistent form.",
        "Crystallization narrows the repertoire to syllables that recur reliably. Mature songs contained defined syllables that emerged from earlier, less organized vocalizations, and those forms can be traced through the recordings.",
        "Longitudinal recordings show how the plastic repertoire becomes the adult repertoire. The transition uses material already present in development, so the adult song reflects refinement of earlier forms.",
    ], "Marler & Peters (1981)", [
        "Stability is judged across repeated renditions.",
        ["Stability.", "A syllable is stable when its form recurs consistently.", "Single renditions are not enough."],
        ["Crystallization.", "The repertoire narrows to reliable syllables.", "Mature songs contain defined syllables."],
        ["Origin.", "Adult syllables emerged from plastic-song forms.", "The forms can be traced through recordings."],
        ["Refinement.", "Adult song refines material already present.", "The change is gradual rather than sudden."],
    ], ["Marler 1981"]),
    ins(24, "Own song and the tutor model are separable stimuli", [
        "**Playback stimuli** are recordings presented to a bird while its neural responses are measured. Margoliash and Konishi used own-song recordings, dialect songs and a training model as separate stimuli, so each source can be compared directly.",
        "Birds reared in the laboratory produced final songs that differed from the model they had heard. Their own song and the tutor recording therefore remained separable acoustic stimuli.",
        "A neuron that prefers own song responds to the bird's output rather than to the tutor target. Keeping the two stimuli separate allows the study to test each one on its own terms.",
    ], "Margoliash & Konishi (1985)", [
        "Playback stimuli are kept separate in the comparison.",
        ["Stimuli.", "Own song, dialect songs and a training model were tested.", "Each was a separate recording."],
        ["Laboratory birds.", "Final songs differed from the model heard.", "Own song and the tutor recording stayed distinct."],
        ["Preference.", "A preference for own song reflects the bird's output.", "It is not the same as the tutor target."],
        ["Design.", "Separate stimuli allow each to be tested on its own terms.", "The comparison stays clear."],
    ], ["Margoliash 1985"]),
    ins(27, "Learned abnormal sound shapes HVC selectivity", [
        "**Abnormal song components** are unusual sounds produced by a bird that differ from the natural species song. In this study, the laboratory birds' unusual components were absent from the natural songs used for comparison.",
        "Their HVC responses still favored their own vocalizations. A response that follows the bird's own abnormal pattern indicates that selectivity can track acquired acoustic material.",
        "The training included an unnatural upward-sweeping trill. Selectivity for the bird's own abnormal components therefore shows how experience can shape the neural response.",
    ], "Margoliash & Konishi (1985)", [
        "Abnormal learned sounds can acquire selective responses.",
        ["Components.", "The birds produced unusual song components.", "These were absent from the natural comparison songs."],
        ["Responses.", "HVC responses favored the bird's own vocalizations.", "The preference followed the abnormal pattern."],
        ["Training.", "The paradigm included an upward-sweeping trill.", "The trill was unnatural for the species."],
        ["Meaning.", "Experience can shape neural selectivity.", "Acquired acoustic material can drive the response."],
    ], ["Margoliash 1985"]),
    ins(30, "Deafening leaves song-timed HVC activity intact", [
        "A **deafened bird** has had its cochlea removed, so it no longer hears its own song. McCasland and Konishi recorded HVC activity in such birds during singing to separate auditory input from the motor timing of song.",
        "Song-related HVC activity continued after deafening. The temporal pattern matched the song's elements, which indicates that the discharge was not driven by hearing each syllable.",
        "Recording before and after deafening holds the bird's song and electrode placement constant. The comparison attributes the persistent pattern to the nucleus's own activity during singing.",
    ], "McCasland & Konishi (1981)", [
        "Song-timed HVC activity persists after deafening.",
        ["Deafening.", "The cochlea was removed in the deafened bird.", "Hearing of the bird's own song was lost."],
        ["Discharge.", "Song-related discharge continued after deafening.", "Its timing matched the song's elements."],
        ["Comparison.", "Recordings were made before and after deafening.", "The song and electrode placement stayed constant."],
        ["Meaning.", "The persistent pattern reflects the nucleus's own activity.", "It is not a direct echo of each syllable's sound."],
    ], ["McCasland 1981"]),
    ins(33, "Suppression of responses follows vocal behavior", [
        "**Auditory suppression** is a temporary reduction in the response to sound. McCasland and Konishi measured it in HVC during and after singing, when a playback stimulus was presented.",
        "The suppression decayed over seconds after the song ended, which links its time course to the preceding vocal behavior. A simple response to each sound would instead follow the stimulus itself.",
        "This timing shows that auditory responsiveness depends on what the bird has just produced. A recovery curve after singing therefore reveals the state of the nucleus as well as the sound.",
    ], "McCasland & Konishi (1981)", [
        "Auditory responses are suppressed around singing.",
        ["Suppression.", "A temporary reduction in the response to playback.", "It was measured during and after singing."],
        ["Time course.", "The suppression decayed over seconds.", "Recovery followed the end of the song."],
        ["Comparison.", "A simple response would follow the stimulus.", "Here the response follows the bird's behavior."],
        ["Meaning.", "Auditory responsiveness depends on vocal state.", "Recovery reveals the state of the nucleus."],
    ], ["McCasland 1981"]),
    ins(36, "Forward and reversed song engage LMAN differently", [
        "A **reversed song** plays the recording backward, which keeps the spectral content while changing the temporal order. Doupe and Konishi used reversal to test whether LMAN responds to song organization.",
        "LMAN neurons responded much less effectively to the reversed version than to forward song. The response therefore follows the sequence of sounds rather than the frequencies alone.",
        "This selectivity narrows the stimulus features that LMAN uses. Forward and reversed songs differ only in their arrangement, so the difference isolates temporal structure.",
    ], "Doupe & Konishi (1991)", [
        "Reversal separates temporal order from spectral content.",
        ["Reversal.", "A reversed song keeps its spectral content.", "The temporal order is changed."],
        ["Response.", "LMAN responded much less to reversed song.", "The sequence of sounds drives the response."],
        ["Selectivity.", "Forward and reversed versions differ in arrangement only.", "The difference isolates temporal structure."],
        ["Meaning.", "LMAN is selective for temporal organization.", "Frequency content alone is not sufficient."],
    ], ["Doupe 1991"]),
    ins(39, "Reversible inactivation reveals a dependency in RA", [
        "**Reversible inactivation** temporarily silences a region and then allows its activity to return. Doupe and Konishi used lidocaine in HVC to test whether RA auditory responses depend on HVC input.",
        "RA responses returned after the drug wore off. Recovery shows that the loss came from a temporary block of HVC rather than from damage to RA.",
        "A recorded neuron can be measured before, during and after the same intervention. This design separates a dependency from permanent injury to the recorded neuron.",
    ], "Doupe & Konishi (1991)", [
        "Reversible inactivation shows a dependency on input.",
        ["Inactivation.", "Lidocaine was injected into HVC.", "The block silenced the input region temporarily."],
        ["Recovery.", "RA responses returned after the drug wore off.", "The loss was reversible."],
        ["Design.", "One neuron was measured before, during and after treatment.", "The stimulus was held constant."],
        ["Meaning.", "RA auditory responses depend on HVC input.", "The dependency is separated from damage."],
    ], ["Doupe 1991"]),
    ins(42, "Okanoya and Yamaguchi tracked sequence changes", [
        "**Syntax** in this study means the ordering of vocal units within a song. Okanoya and Yamaguchi tracked the order of recognizable notes before and after deafening, so the sequence can be described as a set of transitions.",
        "Deafened birds showed abnormal sequence organization compared with hearing controls. Their preoperative songs served as each bird's own reference, which makes the change measurable within the individual.",
        "Each transition is judged by how consistently it recurs across recordings. Sequence stability therefore becomes a property that the loss of feedback can alter.",
    ], "Okanoya & Yamaguchi (1997)", [
        "Syntax describes the ordering of vocal units.",
        ["Syntax.", "Syntax here means the order of vocal units.", "It is not the grammar of human language."],
        ["Transitions.", "Notes were followed across recordings.", "Each transition was judged for consistency."],
        ["Controls.", "Hearing controls kept more stable patterns.", "Deafened birds were compared with their own songs."],
        ["Meaning.", "Feedback loss alters sequence stability.", "The preoperative song is the reference."],
    ], ["Okanoya 1997"]),
]

EXTRA_NOTES = [
    ["Source values.", "The published recordings and measurements come from the original paper.", "Each result is reported with the condition used in the source."],
    ["Why the measure matters.", "The result separates the measured property from the mechanism that produces it.", "The comparison stays within the same birds, cells or recordings."],
    ["Interpretation.", "Each result is read within the preparation and the age group that produced it.", "The claim is restricted to the measured birds and conditions."],
    ["Context.", "The parent figure shows the measurement that the paragraphs describe.", "Each claim is tied to the recordings of the original study."],
]
PARAS = {
 "3": [
  "Juvenile begging and location calls differ in acoustic form from adult calls. The **spectrogram** of each vocalization shows its frequency structure over time, which makes it possible to identify each vocal category before any learning is tested. The same display is applied to every recording in the study. Each vocal category is therefore fixed by its measured form.",
  "Adult calls and the adult song are measured with the same spectrographic display. Keeping the call and song categories separate prevents developmental results about song from being applied to calls. Each category is analyzed against its own reference set of recordings, so its acoustic structure is compared only with the correct model.",
  "Sorting each recording into its category at the start of the analysis keeps the learning experiments focused on song. A result about song structure then describes the song repertoire, while the calls are described on their own terms. This ordering makes every later comparison between tutors and pupils easier to follow."
 ],
 "6": [
  "A **developmental series** is a set of recordings made at successive ages from the same bird. Marler recorded the isolates repeatedly, so each song can be compared with the songs that came before it. The series shows the path from early vocal forms to the final abnormal form, and it reveals each step along that path.",
  "Syllable structure in the isolates changed over the course of development before reaching its abnormal mature state. Each stage of that change is visible when the recordings are arranged by age. Final songs alone would hide the stages, so the full series is needed to see how the mature pattern was assembled.",
  "The isolates' developmental records show how the abnormal pattern was built. Tracking the record from earlier to later stages links the mature song to its origin in isolation, rather than treating it as a fixed endpoint. Each bird supplies its own history, and the pattern is read as a sequence of developmental steps."
 ],
 "9": [
  "A **tutoring interval** is the span of ages during which a pupil hears the model. Both of Marler's windows, days 8–28 and days 35–56, produced good copies in otherwise isolated males. Tutoring within either interval was therefore sufficient for detailed copying, and the windows can be compared directly because the rest of the procedure was identical.",
  "The copies followed the training recordings closely, and the recordings stopped before the mature song appeared. The copied material must therefore have been retained through the interval rather than sung back during the tutoring itself. Each male's final song is compared with its own training recording, which makes the match specific to that bird.",
  "The retention pattern separates the timing of tutoring from the timing of performance. A model heard in one interval can shape a song that emerges far later, which makes the tutoring interval the key variable. Each interval therefore sets which information is kept until the adult song develops."
 ],
 "12": [
  "Marler compared playback at several ages to ask when a recording can be stored as a song model. Early intervals produced detailed copies, whereas playback around or after 100 days did not. The **age of playback** is therefore the variable that changes the outcome.",
  "Developmental age changed the effect of the same kind of acoustic model. Each age group heard a conspecific model that was otherwise suitable for the species, so the difference lies in the bird's developmental stage rather than in the recording. The age groups were compared under the same playback schedule, which keeps the stimulus constant across the contrast.",
  "The contrast shows a window in which detailed song copying is possible. Recognizing that window makes it possible to compare early and late playback under the same procedure. The same comparison also tells the reader which age interval produces detailed copies and which does not."
 ],
 "15": [
  "The **sensory phase** is the period in which a pupil acquires information from its tutor. The **sensorimotor phase** follows, in which the bird uses that stored information to shape its own vocal output. The two phases can be separated by a long interval, and each one can be measured on its own terms.",
  "Marler's delayed imitation shows that the retained information can guide singing months after the tutor was heard. The review by Brainard and Doupe (2000) supports a separate requirement for auditory feedback during refinement.",
  "Each phase has its own requirement. Acquisition depends on the tutor's song, while refinement depends on the bird's ability to hear its developing output. The two requirements are therefore measured by different manipulations, and both are needed to explain how a learned song reaches its adult form."
 ],
 "18": [
  "A **syllable** is a single discrete sound unit in the song. Marler and Peters used recordings whose syllable arrangements were known, which made the tutor material measurable. Each later syllable could then be compared with a specific training syllable, and the arrangement of the syllables in each training recording was known in advance.",
  "Later songs were compared with the training recordings and with an untrained comparison group. The same spectrographic procedure was applied to every bird, which keeps the comparison consistent across pupils. Each training syllable is matched against the later syllables, so the pattern of matches is read directly from the recordings.",
  "A match between a later syllable and a known training syllable supports storage of the training material. That correspondence links the adult song to the infant recordings instead of to a fixed species template. The pattern of matches across many syllables gives a stronger case than any single match."
 ],
 "21": [
  "**Syllable stability** is the consistency of a syllable's form across repeated renditions. Marler and Peters judged stability by comparing renditions over time, so a syllable counts as stable only when it recurs in a consistent form. Each syllable's history is followed from its first appearance to its final form.",
  "Crystallization narrows the repertoire to syllables that recur reliably. Mature songs contained defined syllables that emerged from earlier, less organized vocalizations, and those forms can be traced through the recordings. Each adult syllable has a traceable history in the plastic song that preceded it.",
  "Longitudinal recordings show how the plastic repertoire becomes the adult repertoire. The transition uses material already present in development, so the adult song reflects refinement of earlier forms. Each bird's recordings across ages show the same gradual narrowing from many variable forms to a stable set."
 ],
 "24": [
  "**Playback stimuli** are recordings presented to a bird while its neural responses are measured. Margoliash and Konishi used own-song recordings, dialect songs and a training model as separate stimuli, so each source can be compared directly.",
  "Birds reared in the laboratory produced final songs that differed from the model they had heard. Their own song and the tutor recording therefore remained separable acoustic stimuli. Each bird's song was compared with its own training model, so the comparison is specific to the individual.",
  "A neuron that prefers own song responds to the bird's output rather than to the tutor target. Keeping the two stimuli separate allows the study to test each one on its own terms. Each response is assigned to the stimulus that produced it, so the two responses can be compared directly."
 ],
 "27": [
  "**Abnormal song components** are unusual sounds produced by a bird that differ from the natural species song. In this study, the laboratory birds' unusual components were absent from the natural songs used for comparison. Those components came from each bird's own training history, so they reflect what the bird learned.",
  "Their HVC responses still favored their own vocalizations. A response that follows the bird's own abnormal pattern indicates that selectivity can track acquired acoustic material. This result holds for the abnormal components themselves, not only for the normal song features the birds shared with other singers.",
  "The training included an unnatural upward-sweeping trill. Selectivity for the bird's own abnormal components therefore shows how experience can shape the neural response. The same comparison set against natural songs makes the role of experience clear."
 ],
 "30": [
  "A **deafened bird** has had its cochlea removed, so it no longer hears its own song. McCasland and Konishi recorded HVC activity in such birds during singing to separate auditory input from the motor timing of song. Each recording was matched to the bird's own vocal output.",
  "Song-related HVC activity continued after deafening. The temporal pattern matched the song's elements, which indicates that the discharge was not driven by hearing each syllable. The persistence of this pattern in the absence of hearing is the key observation.",
  "Recording before and after deafening holds the bird's song and electrode placement constant. The comparison attributes the persistent pattern to the nucleus's own activity during singing. This control identifies the nucleus rather than the sound as the source of the timed discharge."
 ],
 "33": [
  "**Auditory suppression** is a temporary reduction in the response to sound. McCasland and Konishi measured it in HVC during and after singing, when a playback stimulus was presented. The stimulus was the same in each condition, which isolates the effect of the bird's own vocal behavior.",
  "The suppression decayed over seconds after the song ended, which links its time course to the preceding vocal behavior. A simple response to each sound would instead follow the stimulus itself, rising and falling with the playback. The gradual recovery is the signature of a state rather than a stimulus.",
  "This timing shows that auditory responsiveness depends on what the bird has just produced. A recovery curve after singing therefore reveals the state of the nucleus as well as the sound. The same measurement can be repeated at several delays to map how the suppression changes over time."
 ],
 "36": [
  "A **reversed song** plays the recording backward, which keeps the spectral content while changing the temporal order. Doupe and Konishi used reversal to test whether LMAN responds to song organization. Each comparison uses the same recording, so the only difference between conditions is the direction of playback.",
  "LMAN neurons responded much less effectively to the reversed version than to forward song. The response therefore follows the sequence of sounds rather than the frequencies alone. The contrast was measured for each neuron against its own response to forward song.",
  "This selectivity narrows the stimulus features that LMAN uses. Forward and reversed songs differ only in their arrangement, so the difference isolates temporal structure. The result is a direct test of whether the order of sounds matters to the neuron."
 ],
 "39": [
  "**Reversible inactivation** temporarily silences a region and then allows its activity to return. Doupe and Konishi used lidocaine in HVC to test whether RA auditory responses depend on HVC input. The same song stimulus was presented throughout, so the input region is the only variable changed.",
  "RA responses returned after the drug wore off. Recovery shows that the loss came from a temporary block of HVC rather than from damage to RA. The timing of the return matches the timing of the drug's effect, which strengthens the link between the two.",
  "A recorded neuron can be measured before, during and after the same intervention. This design separates a dependency from permanent injury to the recorded neuron. Each stage of the sequence is compared with the same cell's earlier response, so the recovery is judged against that cell's own baseline."
 ],
 "42": [
  "**Syntax** in this study means the ordering of vocal units within a song. Okanoya and Yamaguchi tracked the order of recognizable notes before and after deafening, so the sequence can be described as a set of transitions. The note labels were kept constant across recordings.",
  "Deafened birds showed abnormal sequence organization compared with hearing controls. Their preoperative songs served as each bird's own reference, which makes the change measurable within the individual. Hearing controls kept stable patterns across the same interval.",
  "Each transition is judged by how consistently it recurs across recordings. Sequence stability therefore becomes a property that the loss of feedback can alter. The same transitions are counted before and after surgery, so each change is a direct comparison."
 ]
}
for _ins in inserts:
    _ins["paragraphs"] = PARAS[str(_ins["after"])]
    _ins["notes"] = [_ins["notes"][0]] + _ins["notes"][1:] + EXTRA_NOTES
spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
