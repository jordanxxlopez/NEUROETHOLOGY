"""Build Lecture 57 from verified source text and unmodified article crops."""
import json,re,html
from pathlib import Path
B=Path(__file__).resolve().parent
R=json.loads((B/'research.json').read_text());F=json.loads((B/'figure_sources.json').read_text());S=[]
def ref(k):return html.unescape(re.sub('<[^>]*>','',R[k]['reference']))
def author(k):return R[k]['crossref']['author'][0]['family']
def year(k):return R[k]['crossref']['published']['date-parts'][0][0]
def figure(n):
 x=F[n];k=x['paper']
 return {'path':'figures/'+n+'.png','kind':'article','caption':f"{author(k)} et al. ({year(k)}), Fig. {x['figure']}. {x['description']}",'source_url':'https://doi.org/'+R[k]['doi']}
def add(title,k,imgs,text,note):
 body=[p.strip() for p in text.strip().split('\n\n')];assert len(body)==3,title
 keys=list(dict.fromkeys([k]+[F[n]['paper'] for n in imgs]))
 sd={'title':title,'body':body,'transcript':[re.sub(r'\*\*|(?<!\w)_(?=\w)|(?<=\w)_(?!\w)','',p) for p in body]+[note],'refs':[ref(x) for x in keys],'cite':'; '.join(f'{author(x)} et al. ({year(x)})' for x in keys),'figure_width':5.8}
 if len(imgs)==1:sd.update(layout='figure-right',figure=figure(imgs[0]))
 else:sd.update(layout='figures-right',figures=[figure(n) for n in imgs],primary_figure_height=2.8)
 if len(imgs)==2 and imgs[0] in {'pitch_tuning','pitch_masking','rat_neural','rat_click','sea_fit'}:sd.update(figure_arrangement='side-by-side',primary_figure_width=3.8)
 S.append(sd)

add('Pitch follows periodicity rather than one spectral component','marmoset',['pitch_raster','pitch_map'],'''
**Pitch** is the perceived height of a sound, related to its repetition rate. **Fundamental frequency**, or f₀, is the rate of a periodic waveform; **harmonics** are frequency components at integer multiples of that rate. A harmonic complex combines several such components. A sound’s **spectrum** describes energy across its frequencies.

Bendor and Wang recorded individual neurons in awake common marmosets while presenting pure tones and harmonic complexes. Some neurons responded to a tone and to a complex with the same fundamental frequency, even when that fundamental component was absent from the complex.

The cortical response can therefore preserve a common pitch-related value across different spectra. A neuron’s response to a complex reflects more than the presence of one sound-frequency component, because the components actually present can lie outside its pure-tone response range.
''','A spectrum specifies which sound frequencies contain energy. A waveform’s repetition rate specifies how often its temporal pattern recurs. These properties can be experimentally separated by removing the fundamental component while retaining higher harmonics. The recordings identify a cortical response shared by the resulting complex and a tone at its fundamental frequency.')
add('A missing fundamental still drives pitch-selective cells','marmoset',['pitch_example','pitch_map'],'''
A **missing-fundamental complex** contains higher harmonics but no acoustic energy at f₀. Its periodic pattern can support the pitch associated with f₀. The investigators used these complexes to distinguish pitch-related responses from ordinary responses to individual frequencies.

An example marmoset neuron had a characteristic frequency of 182 Hz, meaning the pure-tone frequency to which it was most sensitive. Harmonics presented individually outside its excitatory range produced little activity, whereas combinations of those harmonics elicited firing when their fundamental frequency matched the cell’s preferred value.

**Pitch selectivity** was defined by the joint response to the pure tone and the missing-fundamental complex, with each complex component outside the neuron’s excitatory frequency range. Combining components restored a response associated with their shared periodicity, rather than with any one component alone.
''','The criterion excludes a neuron responding simply to an audible harmonic that happens to fall within its ordinary frequency-response area. The complex is compared with its constituent tones at the same component levels. The pitch-cell recordings and the cortical map come from the same marmoset experiment.')
add('Pitch-selective activity clusters in auditory cortex','marmoset',['pitch_map'],'''
The **auditory cortex** is the cerebral cortical tissue that processes sound. Its frequency map assigns different preferred sound frequencies to neighboring recording sites. Bendor and Wang mapped this organization in awake marmosets and located neurons responsive to missing fundamentals within it.

Pitch-selective neurons clustered near the anterolateral low-frequency border of primary auditory cortex. Most occupied a region smaller than 1 mm², and their characteristic frequencies were predominantly below 800 Hz. Their location was restricted rather than uniformly distributed across the sampled cortex.

The cluster lies near neighboring auditory fields with different frequency organizations. Mapping both ordinary pure-tone tuning and missing-fundamental responses distinguished the local sound-frequency representation from a specialized population that responded to a common pitch value across different acoustic spectra.
''','Primary auditory cortex is labeled AI in the source map. The adjacent rostral field is labeled R. The colored map encodes characteristic frequency, and the marked recording sites identify pitch-selective neurons. The anatomical distribution and the functional response criterion are separate measurements made in the same preparation.')
add('Tone and complex sounds share a cortical pitch preference','marmoset',['pitch_tuning','pitch_map'],'''
A **tuning curve** describes how neuronal firing changes as a stimulus parameter varies. For a pure tone, the investigators varied its sound frequency. For a missing-fundamental complex, they varied f₀ while shifting all harmonic components with it.

Pitch-selective neurons commonly had similar tuning peaks for both sound types. A complex could therefore activate the cell at its preferred fundamental frequency even though its actual frequency components were higher than the pure tone that activated the same cell.

The shared tuning links two acoustically different stimuli through their pitch-related value. The pure-tone curve identifies sensitivity to a frequency component; the complex curve identifies sensitivity to a relationship among components. Their overlap provides a cellular representation that can remain stable when a sound’s harmonic composition changes.
''','The horizontal axis for the complex represents fundamental frequency rather than the frequencies of its individual harmonics. Reading those values as harmonic-component frequencies would change the meaning of the comparison. Each tuning function was measured with stimuli presented directly to the same recorded neuron.')
add('Temporal regularity changes pitch-cell discharge','marmoset',['pitch_salience','pitch_map'],'''
**Pitch salience** is the strength or clarity of a pitch percept. Bendor and Wang varied acoustic properties associated with salience while recording pitch-selective cells. Jittering the intervals in a click train reduced its regular temporal repetition without replacing the train with a different average rate.

Increasing click-time jitter from 5% toward 50% reduced the neurons’ discharge. Iterated rippled noise, produced by repeatedly adding delayed copies of noise, strengthened temporal regularity as the number of iterations increased; neuronal discharge increased with it.

Harmonic composition also mattered. Lower-order harmonics produced stronger responses than complexes composed only of high-order harmonics. The pitch-selective population was therefore sensitive both to temporal regularity and to which harmonics supplied the periodic sound, linking its activity to more than a nominal f₀ label.
''','An iteration adds another delayed copy to the noise, enhancing the repeated pattern. The two stimulus manipulations approach periodicity from opposite directions: jitter weakens regularity, whereas repeated delay-and-add operations strengthen it. The harmonic-order experiment separately changes the spectral ingredients that support the response.')
add('Masking separates pitch responses from distortion tones','marmoset',['pitch_masking','pitch_map'],'''
**Combination tones** are distortion products that can arise when the auditory periphery processes multiple sound components. A missing-fundamental response could otherwise be mistaken for ordinary sensitivity to a distortion product at f₀. Bendor and Wang tested this alternative directly.

Missing-fundamental responses persisted at component levels where the estimated distortion tone would fall below the cell’s pure-tone threshold. The investigators also added a noise masker centered on f₀, spanning approximately one to two octaves, to reduce access to any such low-frequency distortion product.

The neurons continued responding to the harmonic complexes in the masking condition. The response depended on the complex’s harmonic relationship even when a component at f₀ was absent and a peripheral distortion cue was masked. Pitch-related cortical firing thus survived controls directed at the most immediate frequency-based explanation.
''','A threshold is the lowest sound level that evokes the defined neuronal response. Masking adds competing sound energy in a chosen frequency band. The combination of threshold comparisons and targeted noise tests whether a hidden peripheral tone is sufficient to explain the firing evoked by the harmonic complex.')

add('Regular and jittered rhythms isolate temporal predictability','monkey',['rhythm_stimuli'],'''
**Isochrony** means equal spacing between sound onsets. **Beat** refers to a recurring pulse that can be perceived within a rhythm, including rhythms with unequal accents. Honing and colleagues separated these properties while rhesus monkeys listened passively to sequences of percussion sounds.

Regular streams had a 225 ms inter-onset interval, the time between successive sound beginnings. Jittered streams used intervals ranging from 150 to 300 ms while preserving the same average interval and ordering of sound types. Accented sounds could support an inferred pulse every 450 ms in the regular stream.

The comparison changed temporal regularity while retaining the sequence’s sound identities and accent relationships. Sensitivity to equally spaced events could therefore be distinguished from sensitivity to the stronger and weaker positions of an inferred beat.
''','The sounds included a bass-drum and hi-hat combination and a softer hi-hat. A regular event stream can support prediction through equal intervals alone. The accent pattern introduces an additional proposed pulse level, so event timing and metrical position must be tested separately rather than treated as synonyms.')
add('Unexpected intensity decreases evoke mismatch responses','monkey',['monkey_regular','monkey_electrodes'],'''
**Electroencephalography**, or EEG, records electrical voltage differences at the scalp. An **event-related potential** is the average voltage response aligned to repeated events. The monkeys’ scalp recordings were compared for ordinary sounds and unexpectedly attenuated sounds in the rhythmic streams.

An attenuated deviant retained the accented sound’s duration and timbre but was 25 dB softer. **Timbre** is the sound quality associated with its spectral and temporal composition. Comparing a deviant with an ordinary accented event controlled which sound preceded the event being analyzed.

Deviants evoked a **mismatch negativity**, a more negative response relative to the standard event. The response identified detection of an unexpected intensity change while the animals listened without a tapping task. Auditory prediction was therefore measurable through neural responses as well as through overt movement.
''','The present experiment uses attenuated sounds, not omissions. Earlier work discussed in the article used omitted events, but the main data here arise from unexpected decreases in amplitude. The scalp locations identify where voltages were measured; they do not provide a direct image of the neural generator of the mismatch response.')
add('Temporal regularity strengthens the mismatch response','monkey',['monkey_regular','monkey_jitter'],'''
The same intensity deviant occurred in both regularly spaced and jittered sound streams. A response to the unexpected sound therefore could be compared across predictable and unpredictable event timing without changing the deviant’s acoustic identity.

Mismatch responses were larger in the isochronous condition than in the jittered condition. The monkeys were sensitive to equal spacing even though both streams preserved the ordering of accented and unaccented sounds. Regular intervals increased the neural response to an event that violated the established intensity pattern.

Temporal prediction can be supported by repeated intervals. When onset timing varies from event to event, the next sound’s timing is less precisely specified by the preceding interval. The regular-versus-jittered comparison links event-time predictability to detection of an unexpected change in sound intensity.
''','The published traces include both the standard and deviant responses, as well as their difference. A larger difference response can arise from the relationship between these conditions rather than from an isolated voltage peak. Regularity is the manipulated property; the auditory sequence remains passive and requires no motor synchronization.')
add('Isochrony sensitivity and beat-position sensitivity differ','monkey',['monkey_comparison'],'''
**Metrical position** is an event’s placement on or between the recurring beats of a rhythm. Honing and colleagues compared identical attenuated sounds at beat and offbeat positions, in both regular and jittered streams, to test whether the monkeys represented that distinction.

The monkeys detected the intensity changes and responded more strongly in regular streams, but their mismatch responses lacked the beat-position pattern previously measured in humans with the same stimulus design. Equal event spacing and the inferred metrical pulse produced different outcomes in this comparison.

A repeated interval supplies a prediction of when the next event arrives. A metrical representation additionally assigns events to stronger and weaker pulse positions. The monkey recordings supported the first form of temporal organization, while the human comparison contained an additional sensitivity to position within the inferred beat pattern.
''','The human data reproduced in this published comparison come from the matched unattended condition in Bouwer and colleagues. The figure uses different voltage scales for human and monkey responses. The consequential distinction concerns which stimulus property changes the response, rather than the absolute size of voltage across species.')

add('Budgerigars learn pecking timed to a metronome','budgie',['budgie_task','budgie_photo'],'''
**Operant conditioning** changes behavior through its consequences. Hasegawa and colleagues trained budgerigars to peck an illuminated key during an accepted time window surrounding audiovisual metronome cues. Successful sequences produced a food reward, allowing timing to be studied in a controlled task.

Each cue lasted 300 ms. Regular cue intervals ranged from 450 to 1,800 ms, and the birds completed sequences of successive accepted pecks. **Asynchrony** is the time difference between a peck and the associated stimulus onset; it distinguishes a response before the cue from one after it.

The reward window permitted several possible strategies, including reacting to each cue or anticipating its arrival. Measuring the actual peck times separated successful task completion from a specific timing mechanism, because a rewarded response could occur at different phases within the accepted interval.
''','The accepted response period extended before and after the stimulus presentation. The task therefore rewarded a range of response times rather than requiring an exact zero-latency peck. Birds could learn the contingency while expressing different relationships between their internal timing and the external metronome.')
add('Peck phases distinguish anticipation from reaction','budgie',['budgie_phase'],'''
**Phase** describes a movement’s position within one cycle of a repeating stimulus. A consistent peck phase means that responses maintain the same temporal relationship to the metronome across successive cues. Matching phase to cue onset is different from merely producing regular pecks.

Randomly varying cue intervals provided an estimated reaction time of about 150 ms. In regular conditions, some birds pecked near cue onset or before it rather than remaining delayed by that reaction time. Mean response times preceding the stimulus are called **negative mean asynchrony**.

A response that occurs before an expected cue must use information from preceding timing, since the upcoming cue has not yet arrived. The combination of stable phase and anticipatory pecks links repeated external timing to prediction of the next event, rather than to a fixed reaction after every sound.
''','The random-interval condition disrupts a stable prediction of the next cue and estimates responding after an unpredictable event. The phase distributions retain the accepted reward window as well as stimulus onset and estimated reaction time. These are distinct temporal landmarks, so task success alone does not specify anticipation.')
add('Peck timing changes across fast and slow cue rates','budgie',['budgie_asynchrony','budgie_intervals'],'''
At fast metronome rates, with 450 or 600 ms between cues, budgerigars produced especially regular response intervals. At slower rates, mean peck timing shifted closer to cue onset than the reaction-time estimate obtained from unpredictable cues.

**Interresponse interval** is the time between consecutive pecks. During slower sequences, early intervals tended to be shorter than the required cue interval and later intervals lengthened toward it. The birds adjusted their own response period over the sequence instead of maintaining one unchanged pecking rate.

Different timing measures therefore capture different features of performance. Regular spacing describes the consistency of a movement series, whereas asynchrony describes its alignment with an external event. The budgerigars’ tempo-dependent pattern combined precise fast repetition with stronger anticipatory alignment under several slower cue conditions.
''','The source compares the first and last intervals within successful sequences. A change toward the target interval indicates adjustment within the sequence. The birds’ natural warble-song element intervals were mostly below 200 ms, and the authors proposed a relationship between vocal timing and the preference for rapid repetition; that relationship is a hypothesis.')
add('Sound alone can support trained rhythmic pecking','budgie',['budgie_models','budgie_photo'],'''
The original training combined light and sound at each metronome event. The investigators subsequently tested auditory cues alone at 600 and 1,500 ms intervals. Previously trained birds maintained peck alignment after the visual cue was removed, without special retraining for the sound-only condition.

Alternative timing models tested random pecking, constant repetition, memorized intervals and a simple reaction after each cue. None reproduced the full combination of the birds’ phase relationships and anticipatory responses across the tested conditions. A stable response rate alone was insufficient to match the complete behavioral pattern.

Auditory timing can therefore guide the learned movement independently of the flashing key. The sound-only transfer links successful pecking to an acoustic sequence, while the comparison with simpler response strategies identifies the role of adapting movement to expected cue times.
''','The plotted model distributions are original published analyses, not newly generated curves. The auditory-only tests followed audiovisual training, so the task establishes transfer of learned timing to sound rather than spontaneous dancing to unfamiliar music. The behavioral alternatives explain why phase and response intervals were both measured.')

add('A cockatoo synchronizes head bobs to musical playback','patel',['snowball','snowball_phase'],'''
**Auditory-motor synchronization** is alignment of movement with a recurring acoustic pulse. Patel and colleagues tested Snowball, a sulphur-crested cockatoo, while he moved to a familiar Backstreet Boys song. His movements included head bobs whose downward events could be compared with musical beat times.

The original recording had a tempo of 108.7 beats per minute, or bpm. The investigators presented pitch-preserving tempo modifications and recorded the bird without rewarding particular movements. Human observers were instructed to avoid dancing, reducing visual rhythmic cues during playback.

During synchronized bouts, head-bob phases clustered around the musical beat rather than drifting freely through it. The behavior combined a periodic motor action with a stable relationship to the ongoing song, linking movement timing to an auditory pulse under conditions without explicit beat-training rewards.
''','Snowball had a prior history of moving to music, so absence of formal rewards during testing is different from absence of experience. The downward head-bob event was tracked against an independently measured musical beat. A consistent relationship across many beats distinguishes synchronized movement from occasional coincidental alignment.')
add('Tempo changes test flexible musical synchronization','patel',['snowball_tempo'],'''
Moving at one preferred rate can occasionally coincide with music played at that rate. The investigators therefore changed the song’s tempo while preserving its pitch, asking whether Snowball would change his head-bob period along with the musical pulse.

Synchronized bouts occurred across tested tempi from 97.8 to 130.4 bpm. A bout required at least twelve successive head bobs with a stable phase relationship to the beat. The bird adjusted movement rate across this range rather than synchronizing only to the original 108.7 bpm recording.

Changing tempo alters the time available between successive beats while retaining the song’s identity. Flexible synchronization across tempo versions therefore requires adjustment of the repeating movement itself. The bird’s response linked familiar musical material to more than one motor period.
''','Two of the slowest tested tempo conditions lacked synchronized bouts. The observed range describes the conditions in which bouts were found, rather than a continuous estimate of every possible tempo the bird could follow. The source’s erratum corrects trial counts in Table 1; those counts are not used in the slide claims.')
add('Beat phase describes when each head bob occurs','patel',['snowball_phase'],'''
Phase expresses movement timing relative to the duration of a musical beat cycle. Zero degrees places the measured downward head bob at the beat; a positive angle places it afterward, while a negative angle places it beforehand. The sign describes timing, rather than the direction of physical movement.

Across synchronized bouts, Snowball’s mean head-bob phase was about 3.9°. His movements therefore clustered near the beat rather than maintaining a long response delay after every pulse. Both movements slightly before the beat and movements slightly after it occurred within the distribution.

Synchronization combines two requirements: the movement period must follow the beat period, and movement phase must stay aligned. A bird can move rhythmically without meeting the second requirement, because a small persistent rate mismatch causes its movements to drift through successive phases of the musical cycle.
''','The phase histogram pools head bobs from identified synchronized bouts. It is not a histogram of all movement during every playback. The concentration near the beat describes the temporal relationship during those bouts; the proportion of total dancing devoted to bouts is a separate measurement.')
add('Synchronization occurs in bouts during sustained dancing','patel',['snowball_tempo','snowball'],'''
Snowball often continued moving while his head-bob rate diverged from the music. The investigators distinguished sustained dancing from synchronized bouts, so movement during playback was not automatically classified as beat synchronization.

Synchronized bouts accounted for about 25% of head bobs in trials containing synchronization. Their median length was sixteen bobs, with bouts ranging from twelve to thirty-six. At 130.4 bpm, the bird could temporarily match the pulse and then move at another rate while playback continued.

Intermittent alignment and ongoing movement are compatible behaviors. The motor series changes its rate and phase relationship over time, creating periods of stable coordination embedded within a more variable dance. This temporal organization explains why identifying movement alone gives a different description from identifying sustained alignment with the beat.
''','The source uses short moving averages to quantify instantaneous dance tempo. Rectangular intervals in the published time series mark the identified synchronized bouts. The percentage applies to trials with synchronization and should not be converted into a fraction of all listening time or a general rate for the species.')

add('Different parrot movements can align with music','schachner',['avian_motion'],'''
Schachner and colleagues analyzed an African grey parrot and a sulphur-crested cockatoo presented with rhythmic music without continuous visual dancing cues. Neither had been explicitly trained to produce the analyzed movements in response to the stimuli.

The African grey produced periodic head bobs at 120 bpm but did not produce periodic movement to the 150 bpm stimuli. The cockatoo aligned head movement across music ranging from 108 to 132 bpm and also produced foot-lifting movements with a consistent musical relationship.

Movement rate and phase were measured separately. Speed traces described the changing motion, frequency analysis identified dominant repetition rates, and phase analysis measured alignment to beats established by human tapping or automated tracking. Converging measurements tied the periodic movement to the external rhythm rather than simply labeling visible motion as dance.
''','A movement can have a dominant frequency without aligning its phase to the sound. The source treats consistency of frequency, matching of modal movement frequency, and consistency of phase as distinct evidence. The African grey’s response depended on the presented tempo, reinforcing that spontaneous movement is not uniform across musical rates.')
add('Vocal mimicry motivated a comparative rhythm hypothesis','schachner',['vocal_comparison'],'''
**Vocal mimicry** is production of learned sounds resembling sounds heard from other individuals or species. The vocal-learning hypothesis proposes that adaptations linking heard sounds to learned vocal actions also support aligning nonvocal movement with an auditory pulse.

A systematic video survey found evidence suggestive of entrainment among parrot species and an Asian elephant, all categorized as vocal mimics. Vocal nonmimics were well represented among the available videos but lacked the same measured evidence under the survey’s criteria.

The distribution motivated a hypothesis about shared auditory-motor capacities, rather than a claim that every vocal mimic dances. Controlled parrot experiments supplied direct timing measurements, while the broader survey supplied a comparative pattern across species and recording situations. Later trained mammalian tasks test rhythmic capabilities under more standardized sensory and motor demands.
''','Online recordings differ in exposure, recording quality and motivation, so an absent behavior in a video collection is not equivalent to failure in a standardized task. The sea-lion studies measure trained rhythmic behavior in a separate experimental setting. The survey’s positive species pattern is the observation; the proposed evolutionary relationship is the hypothesis.')

add('A trained sea lion follows novel metronome rates','sea2016',['sea_phase'],'''
Ronan, a California sea lion, learned to move her head in time with repeated sounds through food-reinforced training. Rouse and colleagues then tested novel metronome rates and unexpected timing changes while the trainer and reward-delivering assistant remained concealed from view.

At a base tempo of 85 bpm, events were spaced about 706 ms apart. Each click combined brief tones at 659 and 1,319 Hz. Ronan rapidly aligned her head bobs with the stream, stabilizing within the first few beats and maintaining a concentrated phase relationship.

The controlled pulse separated the acoustic timing signal from the richer structure of a song. Novel rates tested adjustment of movement period beyond practiced training rates, and hidden humans reduced access to visible rhythmic guidance. The learned head movement could be coordinated using the timing of the sounds themselves.
''','Ronan’s earlier training used 80 and 120 bpm. The 85 bpm base condition in this experiment was therefore a transfer condition. Training supplied a movement repertoire and its acoustic contingency; successful transfer tested how that repertoire responded to a pulse rate outside the initial training set.')
add('A phase shift requires correction of movement alignment','sea2016',['sea_fit'],'''
A **phase perturbation** moves an event earlier or later within the pulse cycle while leaving the later repetition rate unchanged. It creates a timing error between an already repeating movement and the shifted acoustic pulse without requiring a new sustained tempo.

Ronan encountered unpredictable phase changes of 3% to 25% of the original inter-onset interval. She adjusted the timing of subsequent head bobs and recovered a concentrated relationship to the shifted pulse. Both advances and delays in the acoustic stream produced recovery.

**Phase correction** changes when the movement occurs relative to the stimulus. Because the new stream resumes the previous interval, an enduring change in movement rate would generate continuing drift. Recovery instead requires correction of the displaced alignment while preserving an appropriate repetition period for the ongoing pulse.
''','Perturbations occurred after different numbers of initial beats, preventing a fixed learned correction at one expected trial location. The published traces compare recorded behavior with the article’s original model fit. The fit is a description of recovery dynamics, rather than a recording of a neural oscillator.')
add('A tempo shift changes the required movement period','sea2016',['sea_summary'],'''
A **tempo perturbation** changes the spacing of every subsequent acoustic event. Unlike a single phase displacement, it establishes a different continuing repetition rate. Ronan therefore had to align her next movement and adapt the period of the repeating head-bob sequence.

At the 85 bpm base rate, increasing the interval by 25% produced a 68 bpm pulse; decreasing it by 25% produced about 113.3 bpm. Ronan followed both slower and faster streams after the change, with strongly concentrated phases across perturbation conditions.

Movement phase nevertheless varied systematically with the changed tempo. Following the correct average period and centering each movement exactly on the beat are different properties. The sea lion’s concentrated but tempo-dependent alignment separates stable entrainment from perfect coincidence at every stimulus rate.
''','The percentage manipulation is defined in terms of the interval, so increasing that interval slows the tempo. The mean phase measures the center of the head-bob distribution; phase concentration measures how consistently the animal returns to that center. The plotted conditions preserve this distinction.')
add('Coupled timing models describe sea-lion error correction','sea2016',['sea_fit','sea_parameters'],'''
**Coupled oscillation** describes interacting repeating processes whose timing can adjust to each other. The published model treated the acoustic pulse and Ronan’s repeating head movement as coupled cycles, allowing a timing error at one beat to influence the following movement.

The model included **phase coupling**, adjustment of cycle alignment, and **period coupling**, adjustment of the ongoing repetition interval. Phase coupling alone fit much of Ronan’s recovery; adding period adaptation improved the fit across the phase and tempo perturbations.

The fitted phase-correction component was stronger than the period-correction component. Behavior therefore combined rapid alignment changes with a smaller adjustment of the internal period. A hypothesis in the article links these dynamics to neural resonance, interaction among neural rhythms, while the direct experimental measurements remain the timing of head movements.
''','The plotted curves are cropped from the published paper and retain the original model and observed data. Model parameters describe the strength of timing adjustment in this formulation. The experiment did not record the neural populations proposed to implement the coupled cycles, so the neural implementation is a hypothesis rather than an anatomical result.')

add('An experienced sea lion maintains precise pulse matching','sea2025',['sea2025_early'],'''
Cook and colleagues reassessed Ronan after years of intermittent rhythmic experience. At fifteen years of age, her head-bob timing was more consistent and better aligned with the pulse than in the earlier measurements obtained when she was three.

The comparison used familiar metronome rates of 80, 96, 108 and 120 bpm. Ronan produced one head bob per beat throughout the tested trials, without inserting extra bobs between pulses. Her earlier tendency to lead or trail different tempi was substantially reduced.

Repeated experience and development can change the expression of a timing capacity. The later performance combined accurate rate matching with more stable phase, rather than merely increasing the amount of movement. Longitudinal measurements therefore describe a trained individual’s changing sensorimotor performance across years of exposure.
''','Age and accumulated rhythmic experience changed together between the early and later assessments. The measured result is improved performance in the same animal under comparable familiar tempo conditions. Assigning the improvement entirely to maturation or entirely to practice would require separating those histories experimentally.')
add('Novel rates test timing beyond the practiced pulse','sea2025',['sea2025_humans'],'''
Ronan was tested at novel metronome rates of 112 and 128 bpm, surrounding the familiar 120 bpm rate. **Sensorimotor synchronization** coordinates sensory timing with repeated movement, so transfer requires both listening to the new interval and changing the movement sequence accordingly.

At 112 bpm, her performed average rate was 113.1 bpm; at 128 bpm, it was 129.0 bpm. Her mean phase shifted from about 34° before the beat at the slower novel rate to about 7° after the beat at the faster novel rate.

Matching tempo and matching phase remain separable even in an experienced performer. The movement series can follow a newly presented rate closely while retaining a small lead or lag relative to each pulse. Flexible transfer is expressed in the rate of the entire movement sequence as well as its beat-by-beat alignment.
''','The reported rates and phase angles are source values, with the uncertainty terms omitted from teaching prose. The familiar 120 bpm condition anchors the comparison between the two previously unexposed rates. All three conditions use the same kind of simple metronomic acoustic stimulus.')
add('Matched movements compare sea-lion and human timing','sea2025',['sea2025_motion'],'''
Human button presses and sea-lion head bobs differ in amplitude and mechanical demands. The investigators instead asked humans to make downward arm movements comparable to Ronan’s large head movements.

The sea lion and humans followed the same 112, 120 and 128 bpm metronomes. Ronan’s timing matched or exceeded that of most participants across the tested measures of tempo, phase and consistency. No human participant outperformed her on every measured dimension of the task.

Motor requirements influence auditory timing performance. A large movement must be accelerated and reversed across a substantial distance; a small finger action has different physical constraints. Matching response scale compares species on a shared task with comparable movement demands.
''','The source compares head displacement with downward arm displacement and marks the lowest point of each movement. The direct comparison concerns these gross movement responses. It should not be treated as a universal ranking across instruments, finger-tapping tasks, dance styles or all members of either species.')
add('Timing precision reflects the task and the animal’s history','sea2025',['sea2025_model'],'''
The investigators used the human measurements to generate a published distribution of plausible performance on the same task. Ronan’s measured timing fell within or beyond the more precise portions of those distributions across the tested rates, reinforcing the direct comparison with human participants.

Her experience included initial reward-based learning and later intermittent practice. The article also describes human rhythmic exposure as extensive and often informal, including childhood participation in songs and movement games. Familiarity with coordinating sound and action can therefore develop through different learning histories.

Comparative performance combines a capacity with the conditions under which it is practiced and measured. Ronan’s mature behavior linked novel pulse rates to precise large movements after sustained experience, while the matched human task exposed substantial individual variation in that same form of sensorimotor coordination.
''','The simulated distribution is the original published model figure. It is not a new graph constructed for the lecture. Ronan’s crosses represent measured sea-lion behavior, whereas the surrounding distributions come from the model informed by human data. The direct behavioral comparison remains the empirical basis for describing her performance.')

add('Rats make spontaneous movements linked to musical beats','rat',['rat_motion'],'''
Ito and colleagues recorded rat head movement during playback of a Mozart piano sonata. A miniature wireless **accelerometer**, a sensor measuring acceleration, was attached to a head-mounted holder so that movement could be recorded without requiring trained tapping.

The investigators played sixty-second excerpts at 99, 132, 264 and 528 bpm. Some trials contained head movements aligned with putative beats, with the clearest group alignment near the original 132 bpm rate. The animals received neither a beat-following instruction nor rewards for synchronized movements.

The measured behavior was a small spontaneous movement response during listening. Tracking movement against the sound’s temporal structure identified beat-linked activity that ordinary observation might miss. The most favorable rate was within the range commonly associated with human musical pulse rather than at a uniquely rapid rate expected solely from small body size.
''','The four playback rates were 75%, 100%, 200% and 400% of the original recording’s tempo. Putative beats were identified from the music rather than supplied as isolated metronome clicks in the movement experiment. Individual trials differed in the strength of movement alignment.')
add('Movement derivatives identify rapid changes near a beat','rat',['rat_motion','rat_phase'],'''
The head-mounted sensor measured acceleration along three axes. **Jerk** is the rate of change of acceleration, so it emphasizes brief changes in movement rather than the sustained acceleration value. Ito and colleagues found beat-linked movement more consistently characterized by jerk than by acceleration alone.

They compared jerk near putative beat times with jerk between those times. Shifting the assumed beat window through the cycle produced a phase profile, identifying whether movement changes were concentrated around the actual musical beats or at other positions.

The resulting **beat contrast** measures the difference between on-beat and offbeat movement. A large overall movement is distinct from a large contrast, since vigorous motion can occur throughout a cycle. The timing relationship therefore depends on where movement changes occur, not simply on how much the animal moves during playback.
''','The study also compared sensor-based measures with video-derived movement in its validation analysis. Jerk has units of acceleration change per time, written m/s³ in the original plots. The source figure’s axes and calibration remain intact; the lecture does not reconstruct a derivative trace from reported summary data.')
add('Playback tempo alters rat movement alignment','rat',['rat_consensus','rat_phase'],'''
Increasing playback speed compressed the intervals between musical events. The same excerpt therefore tested whether rats would align more strongly with a faster pulse, as a body-size explanation might predict, or with a rate near the original music.

Beat contrast and agreement among movement profiles were strongest around 132 bpm rather than at 264 or 528 bpm. **Beat consensus** describes similarity of the phase profiles across animals, separating shared timing from an individual movement response that happens to favor another phase.

The result supports the hypothesis that preferred auditory timing depends partly on neural dynamics shared across species rather than being determined entirely by the body’s movement speed. Tempo changed the sound’s event spacing, and the animals’ most consistent beat-linked movement remained near the unmodified recording’s rate.
''','The body-based and brain-based accounts are hypotheses posed in the source. The movement measurements favor one range of acoustic timing but do not themselves identify a cellular mechanism. Neural recordings and the article’s adaptation analysis provide the separate evidence about auditory response dynamics.')
add('Rat and human movement varies across the same music','rat',['rat_human'],'''
Human participants heard the same tempo-modified excerpts while their head movements were measured. Both species showed reduced movement magnitude as playback tempo increased, with overlapping favored tempi despite different body sizes.

Across the original excerpt, the moments of stronger rat and human movement were related. At 132 bpm, corresponding putative beats elicited related rises and falls in movement magnitude, linking response strength to the excerpt’s changing acoustic context.

Rat movement was generally more delayed relative to the beat than human movement. Shared rate preferences and related moment-to-moment responses can coexist with different phase relationships. Spontaneous acoustic responses and predictive movement alignment are therefore distinguishable features of how the two species respond to the same musical sequence.
''','The source reports that some rat movement begins to rise before a beat, but the main phase peaks are more reactive than those of humans. It would be inaccurate to describe every rat head movement as anticipatory dancing. The comparison concerns spontaneous head movement during these excerpts, not trained metronome performance.')
add('Auditory population responses are tuned to musical timing','rat',['rat_neural','pitch_map'],'''
**Multi-unit activity** pools spikes, the brief electrical discharge events of nearby neurons, rather than isolating one neuron. Ito and colleagues recorded this activity from rat auditory cortex while presenting the same musical excerpt at several playback rates. Neural responses were measured separately from the freely moving behavioral recordings.

The strongest contrast between beat-note and nonbeat-note responses occurred near the original tempo. The activity evoked shortly after a note depended on its position within the musical sequence, linking population firing to the temporal organization of the sound rather than only to the existence of an onset.

The accompanying marmoset map identifies organized auditory cortical territories in another mammal. Its pitch-selective cells were tested with harmonic sounds; the rat population recordings were tested with music timing. Pitch-related cortical selectivity and timing-related population responses concern different acoustic dimensions within auditory processing.
''','The cortical anatomy image is Bendor and Wang’s marmoset map, not a rat map. Ito and colleagues recorded rat auditory multi-unit activity using a microelectrode array in a separate anesthetized preparation. Their onset measure compared activity 5–30 ms after note onset with the early baseline window, so it captures short-latency auditory responses.')
add('Identical clicks isolate the effect of preceding timing','rat',['rat_click','pitch_map'],'''
The rat investigators simplified the sound to repeated groups of three clicks followed by a rest. All clicks were acoustically identical, so different responses within a group could arise from preceding timing rather than from differences in pitch or intensity between the clicks.

Sequences were presented at 60, 120, 240 and 480 bpm. The first click followed a longer gap than the later clicks. Cortical population responses differed among positions, with the strongest beat-versus-nonbeat contrast near 120 bpm, paralleling the preferred range measured with music.

The history of recent sound exposure changes the response to a new onset. A gap allows more recovery before the next click, while closely spaced events maintain a different response state. The published marmoset cortical map supplies comparative anatomy; the click-response traces are the direct rat physiological evidence for timing-dependent auditory activity.
''','The first click is defined as the beat in this simplified stimulus because it follows the rest. This arrangement isolates a timing-history effect but is not equivalent to all forms of human metrical inference. The rat physiological preparation and the marmoset anatomy figure are identified separately in their captions and citations.')
add('Auditory adaptation predicts a favored rhythmic rate','rat',['rat_adaptation','pitch_map'],'''
**Short-term adaptation** is a response change produced by recent stimulation. Ito and colleagues hypothesized that the decay and recovery of auditory responses could produce rate-dependent beat contrast. They fitted the published model to cortical responses rather than assigning a preferred rate from body movement alone.

The fitted temporal influence included strong suppression for approximately 250 ms after sound stimulation. A following click therefore arrives in a different response state depending on the elapsed interval. Repeated sounds and inserted rests alter how much of this suppression remains at each event.

The model reproduced a peak in beat contrast around 120 bpm and several recorded responses to periodic and grouped clicks. This is a hypothesis about population response dynamics, with the model’s suppression term describing the effect of recent activity. The accompanying cortical map identifies the anatomical class of tissue studied across the mammalian comparisons.
''','The curves are the article’s original data and model panels. The fitted suppression kernel describes time-dependent effects at the population level; it is not a direct measurement of a named inhibitory receptor, transmitter or ion channel. No unmeasured molecular implementation is assigned to it in the slide.')

add('Cat-relevant compositions use different pitch and pulse','cat',['cat_response'],'''
Snowdon and colleagues composed music using acoustic features associated with domestic cat communication. **Tessitura** is the average pitch range of a musical passage. The cat compositions had an average pitch near 1.34 kHz, about two octaves above the human comparison music’s approximately 335 Hz.

Cozmo’s Air used a pulse based on purring, at 1,380 bpm; Rusty’s Ballad used a 250 bpm pulse based on suckling. Both contained frequent gliding frequencies, continuous changes in pitch. The human comparison pieces had slower pulses and substantially fewer frequency glides.

These compositions applied features of affiliative cat sounds rather than simply replaying recorded cat calls. The hypothesis was that species-relevant pitch, timing and frequency movement would increase cats’ orientation and approach. Acoustic relevance was tested through observable behavior toward playback, not through assuming that human musical genres carry the same meaning for cats.
''','The human pieces were Fauré’s Elegie and Bach’s Air on the G String. Their pulses were 66 and 56 bpm, respectively. The purring-based musical pulse is an acoustic modulation parameter and should not be equated with a cat moving its body 1,380 times per minute.')
add('Cats approach species-relevant playback more readily','cat',['cat_response'],'''
Cats heard species-relevant and human music at home. Excerpts lasted three minutes, with intervening silence. Counterbalanced order and speaker assignment prevented a consistently preferred speaker location from explaining the music comparison.

Interest behaviors included orienting the head, moving toward the speaker, sniffing it and rubbing against it. The median orient-and-approach score was 1.5 for cat music and 0.25 for human music. Median latency to the first response was 110 s for cat music and 171.75 s for the human comparison.

A shorter latency indicates earlier engagement during playback; the behavior score captures the frequency of scored interest responses. Both measures favored cat-relevant compositions. Response timing, orientation and approach connect acoustic properties to active interaction with the sound source.
''','The maximum observation interval was 180 s. A latency near that limit reflects a late or absent response during the brief excerpt and should not be generalized to a lifetime preference. Responses were aggregated at the household level when more than one cat participated in the same home.')
add('Age and measured behavior shape the cat music response','cat',['cat_age'],'''
The frequency of interest behaviors varied with cat age. Younger and older cats were more responsive to species-relevant music than middle-aged cats in the tested population, producing a curved rather than a simple steadily increasing age relationship.

The ethogram, a defined list of scored behaviors, also included possible negative responses such as leaving, piloerection and growling. **Piloerection** is erection of the hair. Such responses were uncommon and did not separate cat and human music clearly, whereas orientation and approach did.

The main effect was therefore increased engagement with selected acoustic features. A preference for approaching a sound source differs from a reduction in physiological stress. Age-related variation further means that one composition can recruit different amounts of visible interest among members of the same species.
''','The source curve relates interest behavior to age; it is not a direct measure of aging in the auditory pathway. The authors propose enrichment uses, but the measured endpoints here are orientation, approach, response latency and the defined negative behaviors. Those endpoints support engagement without requiring an unmeasured endocrine mechanism.')

add('A veterinary setting tests music under handling stress','dog',['dog_timeline','dog_behavior'],'''
King and colleagues tested bespoke music during a mock veterinary visit using repeated visits with and without music. Dogs entered a waiting area, spent fifteen minutes kenneled and then underwent a physical examination, allowing auditory treatment to be compared across different parts of the visit.

**Qualitative behavioral assessment** scores the animal’s expressed demeanor using descriptors such as anxious, relaxed or engaged. Dogs received higher afraid ratings during examination than during kenneling, and greater engagement when interacting with people. The physical and social setting changed the behavioral expression measured during the visit.

Music did not reduce the main behavioral stress components in this setting. Human contact and examination altered activity and demeanor even with playback present. The intervention’s effect therefore depends on its ability to change the measured response during the actual handling context, rather than on the music’s intended relaxing character.
''','The repeated-visit design compares the same dogs across control and treatment experiences. Waiting, kenneling and examination are distinct contexts with different human contact. The music was designed for the treatment, but an intended calming acoustic design is separate from a measured reduction in fear or anxious behavior.')
add('Behavior and endocrine activity can change differently','dog',['dog_cortisol','dog_temperature'],'''
**Cortisol** is an adrenal glucocorticoid measured in saliva as one component of the physiological response to a stressful event. **Immunoglobulin A** is an immune antibody also measured in saliva. Both concentrations rose after kenneling and remained elevated following examination compared with entry baseline.

The music treatment did not change either salivary measure clearly relative to control visits. Heart and respiration rates also lacked a clear treatment difference, while rectal temperature was lower during music visits. Different physiological endpoints therefore produced different treatment comparisons.

A reduced temperature value cannot replace the behavioral and endocrine measurements of the same intervention. Each endpoint samples a different process, and the combined results did not support a general calming effect during the mock visit. Physiological state is characterized by the relationships among these measures rather than by one selected favorable outcome.
''','The original plotted values and units remain intact. The source reports a rectal-temperature difference but no corresponding music effect on cortisol or the main behavioral dimensions. That disagreement changes the conclusion about a general stress-reducing treatment, making it a consequential result rather than a routine disclaimer.')
add('Thermal responses track the veterinary visit over time','dog',['dog_thermal','dog_behavior'],'''
**Infrared thermography** estimates surface temperature from emitted infrared radiation. The investigators sampled the dogs’ eye, nose and ear regions at entry, after kenneling and after examination, providing noncontact physiological measurements alongside saliva and behavioral ratings.

Surface temperatures increased after kenneling and remained higher following examination. These changes occurred during both control and music visits. In the behavioral scoring, dogs were more afraid during examination, whereas other ratings reflected the greater opportunity to interact with people during that stage.

The visit produced a time-dependent physiological response and a context-dependent behavioral response. Auditory enrichment operated within those ongoing demands rather than replacing them. Evaluating a music treatment consequently requires matching its proposed effect to the actual response measured, whether surface temperature, expressed fear, social engagement or endocrine activity.
''','The thermal panels are the source’s infrared measurements, not color added to an ordinary photograph. The instrument-generated colors and marked regions are preserved exactly as published. Surface temperature is distinct from rectal temperature, and the study measured those endpoints using different methods.')

add('Cockatiel music choices require location and shape controls','cockatiel',['cockatiel_schedule','cockatiel_device'],'''
Le Covec and colleagues offered cockatiels two shapes associated with fifteen-second piano excerpts: rock and roll or calm music. Birds could approach and peck voluntarily, and an experimenter triggered playback and delivered a food reward following the specified listening period.

The first experiment used a protected paper display because the intended touchscreen malfunctioned. The investigators exchanged the shapes’ locations and later exchanged their music associations. These reversals separated preference for a tune from preference for a side, a color or a geometric shape.

**Choice preference** is repeated selection of one available option under controlled alternatives. Changing the mapping requires a bird favoring a tune to select a different visual target when that tune moves. A bird continuing to peck the same shape despite a music reversal expresses a different preference from one following the sound.
''','The diagram is an original published figure of the experimental device. The study did not achieve autonomous touchscreen activation by cockatiels. Human-triggered playback followed their pecks, so the behavioral choice is voluntary but the playback mechanism remained assisted. Seeds rewarded participation rather than one particular musical option.')
add('Individual cockatiels follow different preferred tunes','cockatiel',['cockatiel_gaia','cockatiel_eole'],'''
Gaïa and Nephtys preferred the rock-and-roll excerpt, whereas Éole preferred calm music. Their selections followed the corresponding music across the location and music reversals, so the preferences differed among individuals rather than defining one favored style for all cockatiels.

Seth continued selecting the blue circle after its musical association changed. His behavior was therefore linked to the visual shape rather than to one tune. The same choice apparatus could produce either auditory preference or visual-target preference depending on the bird.

Holding the instrument constant reduced a possible piano-versus-other-instrument explanation, but the two excerpts still differed in several musical properties. The measured outcome was a preference between those specific excerpts. Individual variation and reversal behavior connect each bird’s choices to the available acoustic and visual contingencies.
''','The two excerpts were piano versions of Rock Around the Clock and Le roi et l’oiseau. Gaïa and Éole provide opposite musical choices in the original figures. Nephtys also preferred rock and roll; Seth’s blue-circle preference supplies the control case against treating every repeated shape choice as a musical preference.')
add('Consonance choices differ from preferences between tunes','cockatiel',['cockatiel_consonance','cockatiel_seth'],'''
**Consonance** and **dissonance** describe different harmonic relationships among simultaneously sounding pitches. A second cockatiel experiment compared an original Renaissance piece with a version combined with pitch-shifted copies, using a new pair of visual targets and the same fifteen-second playback duration.

Nephtys preferred one shape and Isis preferred one side across reversals, rather than consistently following consonant or dissonant music. The physical touchscreen also required the experimenter to touch after each bird’s peck, because the beak contact failed to activate playback reliably.

Preferences between two contrasting tunes therefore differed from preferences between harmonic versions of one tune. Voluntary approach can supply information about an animal’s choices, but the target mapping and response interface determine which preference is measured. Species-appropriate enrichment includes an operable choice mechanism as well as sound options relevant to the individual.
''','The source does not establish a consonance preference in these cockatiels. The decisive result is that choices followed a visual shape or spatial position. Assisted activation changes the practical interpretation of the device: it measured choices during supervised sessions but did not supply an autonomous enrichment system.')

assert len(S)==44,len(S)
refs=list(dict.fromkeys(ref(k) for k in R))
spec={'lecture':57,'content_slides':44,'title_height':2.8,'theme':'dusk-blue-paper','title_refs':[ref('patel')],'title_image':figure('snowball'),'slides':S,'takeaways':{'items':[
 {'lead':'Pitch integrates acoustic relationships.','text':'Marmoset pitch-selective cells respond to tones and missing-fundamental complexes with the same preferred fundamental frequency.'},
 {'lead':'Temporal regularity differs from inferred beat.','text':'Rhesus auditory mismatch responses track equal event spacing without the human pattern of metrical-position sensitivity.'},
 {'lead':'Synchronization requires rate and phase control.','text':'Parrots and a trained sea lion adjust repeated movements to external pulses; anticipation and perturbation recovery distinguish timing strategies.'},
 {'lead':'Experience and task demands affect performance.','text':'An experienced sea lion matches or exceeds many human performers when gross movement requirements are comparable.'},
 {'lead':'Auditory adaptation shapes rate-dependent responses.','text':'Rat cortical responses favor timing near 120–140 bpm; the published adaptation model links recent stimulation to response recovery.'},
 {'lead':'Musical engagement is species and individual dependent.','text':'Cat-relevant music increases approach, cockatiels have different tune preferences, and music fails to produce general calming during a mock dog veterinary visit.'}
 ],'cite':'Bendor and Wang (2005); Honing et al. (2018); Patel et al. (2009); Rouse et al. (2016); Cook et al. (2025); Ito et al. (2022); Snowdon et al. (2015); King et al. (2022); Le Covec et al. (2024)','refs':refs}}
(B/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
(B/'spine.md').write_text('# Lecture 57 teaching spine\n\n'+'\n'.join(f'{i}. {s["title"]}' for i,s in enumerate(S,1))+'\n')
for i,s in enumerate(S,2):
 w=len(re.sub(r'[*_]','', ' '.join(s['body'])).split())
 if not 90<=w<=170:print('WORDS',i,w)
 if len(s['title'])>62:print('TITLE',i,len(s['title']))
print('Wrote',len(S),'content slides')
