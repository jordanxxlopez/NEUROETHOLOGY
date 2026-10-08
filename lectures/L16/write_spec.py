#!/usr/bin/env python3
"""Build the source-grounded Lecture 16 spec; figures are untouched article crops."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
R = {
'L75': ('Long & Schnitzler (1975)', 'Long GR, Schnitzler H-U (1975). Behavioural audiograms from the bat, Rhinolophus ferrumequinum. Journal of Comparative Physiology 100:211–219. https://doi.org/10.1007/BF00614531', '10.1007/BF00614531'),
'S75': ('Suga et al. (1975)', 'Suga N, Simmons JA, Jen PH-S (1975). Peripheral specialization for fine analysis of Doppler-shifted echoes in the auditory system of the “CF-FM” bat Pteronotus parnellii. Journal of Experimental Biology 63(1):161–192. https://doi.org/10.1242/jeb.63.1.161', '10.1242/jeb.63.1.161'),
'S77': ('Suga (1977)', 'Suga N (1977). Amplitude Spectrum Representation in the Doppler-Shifted-CF Processing Area of the Auditory Cortex of the Mustache Bat. Science 196(4285):64–67. https://doi.org/10.1126/science.190681', '10.1126/science.190681'),
'C74': ('Schuller et al. (1974)', 'Schuller G, Beuter K, Schnitzler H-U (1974). Response to frequency shifted artificial echoes in the bat Rhinolophus ferrumequinum. Journal of Comparative Physiology 89(3):275–286. https://doi.org/10.1007/BF00696191', '10.1007/BF00696191'),
'M02': ('Metzner et al. (2002)', 'Metzner W, Zhang S, Smotherman M (2002). Doppler-shift compensation behavior in horseshoe bats revisited: auditory feedback controls both a decrease and an increase in call frequency. Journal of Experimental Biology 205(11):1607–1616. https://doi.org/10.1242/jeb.205.11.1607', '10.1242/jeb.205.11.1607'),
'H18': ('Schoeppler et al. (2018)', 'Schoeppler D, Schnitzler H-U, Denzinger A (2018). Precise Doppler shift compensation in the hipposiderid bat, Hipposideros armiger. Scientific Reports 8:4598. https://doi.org/10.1038/s41598-018-22880-y', '10.1038/s41598-018-22880-y'),
'H22': ('Schoeppler et al. (2022)', 'Schoeppler D, Denzinger A, Schnitzler H-U (2022). The resting frequency of echolocation signals changes with body temperature in the hipposiderid bat Hipposideros armiger. Journal of Experimental Biology 225(3):jeb243569. https://doi.org/10.1242/jeb.243569', '10.1242/jeb.243569'),
}
slides=[]
def add(title, refs, body, transcript, figure=None):
    keys=refs.split(); s={'title':title,'layout':'text','body':body,'transcript':transcript,'cite':'; '.join(R[k][0] for k in keys),'refs':[R[k][1] for k in keys]}
    if figure:
        name,key,num,description=figure
        s.update(layout='figure-right',figure_width=5.2,figure={'kind':'article','path':f'figures/{name}.png','caption':f'{R[key][0]}, Fig. {num}. {description}','source_url':'https://doi.org/'+R[key][2]})
    slides.append(s)

add('CF-FM calls combine a sustained tone and a short sweep','H18 S75',[
'**Echolocation** is active sensing with emitted sounds and returning echoes. A **constant-frequency component**, or CF, maintains nearly one frequency; a **frequency-modulated component**, or FM, changes frequency during the signal. CF-FM bats combine a prolonged tone with a brief downward sweep.',
'In _Hipposideros armiger_, recordings during flight contain several **harmonics**, frequency components at integer multiples of the lowest component. The second harmonic carries the greatest amplitude. Its CF frequency is around 65–66 kHz in the animals studied by Schoeppler and colleagues.',
'The CF component persists during approach to a landing target, even as call duration and harmonic prominence change. A narrowband carrier and a changing terminal sweep therefore coexist within individual calls; the signal is not simply a pure tone.'
],[
'An echolocating bat supplies its own acoustic input by producing a call and receiving reflections. Constant frequency describes the sustained part of that call, whereas frequency modulation describes the brief change in frequency at its end.',
'A harmonic belongs to a series of frequencies related by whole-number multiples. The second harmonic was the strongest component in these Hipposideros armiger recordings. Its frequency was near 65 to 66 kilohertz, which is above the human audible range.',
'The recordings include stationary calling and flight toward a landing grid. The sustained component remained present during the final approach, although the calls became shorter and the higher harmonics weakened. The CF and FM labels describe acoustic components, not two separate calls.'
],('schoeppler18_fig1','H18','1(a–d)','Flight call sequence and CF-FM structure, in kHz and ms.'))

add('Flutter changes the echoes carried by the CF component','H18 S75',[
'**Flutter** is the periodic motion of an insect’s wings. Flutter-detecting bats receive echoes whose amplitude and frequency vary as the reflecting wings move. The long CF component supplies a sustained carrier on which those changes can occur.',
'The **auditory fovea** is an expanded, sharply tuned representation of a narrow frequency range in the hearing system. In CF-FM bats, that range corresponds closely to the returning CF component rather than to all ultrasonic frequencies equally.',
'Flight-induced shifts can move the echo carrier away from this specialized range. Doppler-shift compensation keeps echoes from stationary targets ahead near the preferred frequency, supporting analysis of smaller variations associated with flutter. The behavioral adjustment and peripheral specialization are complementary adaptations.'
],[
'An insect wing changes position and orientation repeatedly during a wingbeat. The resulting echo can change in both amplitude and frequency. A long constant-frequency call provides a carrier whose fluctuations can be resolved by a hearing system specialized for that band.',
'The term auditory fovea refers to unequal representation: a narrow range of frequencies receives unusually fine tuning and extensive representation. It does not mean that the ear is equally sensitive to every part of an ultrasonic call.',
'Self-motion also changes echo frequency, even when the reflecting object is stationary. Compensation reduces that large shift of the carrier. It does not require the bat to remove every smaller fluctuation produced by a moving wing. Suga’s peripheral recordings and the flight observations address different parts of this combined sensory strategy.'
])

add('Approaching a reflector raises returning echo frequency','C74 H18',[
'A **Doppler shift** is a frequency change caused by relative motion between a sound source, a reflector, and a receiver. When a bat approaches a stationary object, the returning echo has a higher frequency than the emitted sound.',
'**Doppler-shift compensation** lowers the frequency of subsequent calls as approaching motion raises echo frequency. The regulated quantity is the returning CF frequency. The emitted CF frequency must therefore change rather than remain fixed throughout flight.',
'Schoeppler and colleagues recorded calls and reconstructed flight toward a grid. Call frequency fell during acceleration and recovered during deceleration. Schuller and colleagues independently manipulated echo frequency in stationary bats, separating an auditory-feedback effect from the mechanical effects of flight.'
],[
'A stationary reflector can return a frequency-shifted echo when the bat itself is moving. Motion toward the reflector raises the returning frequency. The bat counters this by lowering the frequency it emits on later calls.',
'Compensation is an adjustment of the outgoing signal based on the returning signal. The bat can maintain a relatively stable echo frequency while producing a sequence of calls whose frequencies differ substantially.',
'Free-flight recordings connect the adjustment to natural movement, but movement also changes distance, echo intensity, and other conditions. Artificial-echo playback provides a separate causal test. A stationary animal changes its call frequency when only the frequency of its acoustic feedback is altered, establishing that physical acceleration is not required to evoke the response.'
])

add('Resting frequency is an individual calling baseline','C74',[
'The **resting frequency** is the mean CF frequency of consecutive calls emitted by a stationary bat. In Schuller and colleagues’ greater horseshoe bats, _Rhinolophus ferrumequinum_, individual resting frequencies ranged from about 81 to 84.2 kHz.',
'The investigators measured the central CF portion, excluding the first and last 5 ms to avoid the adjoining FM sweeps. Repeated calls clustered closely around an individual’s baseline. Playing back unshifted calls did not systematically change that baseline.',
'Resting frequency is therefore a reference for describing changes in emitted frequency, not the frequency at which all compensated echoes must return. Individual and temporal differences require a baseline measured in the same animal and experimental period.'
],[
'The resting frequency is calculated from a series of calls made while the bat is stationary. It is an individual baseline, rather than a single frequency assigned to an entire species.',
'These horseshoe bats called near 81 to 84.2 kilohertz. The measurements excluded the beginning and end of each call because those portions include frequency sweeps. The central sustained portion supplied the estimate of constant frequency.',
'Unshifted playback controlled for the presence of an additional acoustic signal. It did not cause a systematic change in resting frequency. Frequency-shifted playback could therefore be compared against a baseline that was not simply altered by any echo presentation. The eventual frequency of a compensated echo must still be distinguished from this emission baseline.'
],('schuller74_fig1','C74','1','Distribution of CF frequencies in a stationary horseshoe bat.'))

add('Shifted playback causes subsequent calls to fall in pitch','C74',[
'Schuller and colleagues returned each horseshoe bat’s own call through an electronic frequency shifter. The stationary animal could move its head, but it did not fly. The microphone and loudspeaker were positioned 34 cm in front of it.',
'When the artificial echo was shifted upward, later emitted calls decreased in CF frequency. After several calls, the animal reached a new emission level. Increasing the imposed positive shift required progressively greater lowering of the outgoing frequency.',
'This **closed-loop playback** preserves the link between the animal’s current call and its feedback. The compensation response depends on an experimentally imposed frequency discrepancy, rather than requiring actual motion toward a reflector.'
],[
'The returning sound was made from the bat’s own vocalization. Its frequency was changed electronically and it was played back to the animal. As the animal changed its next call, the playback changed with that call while retaining the imposed shift.',
'The horseshoe bat remained stationary. An upward change in playback frequency nevertheless caused it to lower subsequent emissions. The response settled after a short sequence of calls, rather than being a fixed change caused by a single prerecorded tone.',
'The intervention establishes an auditory contribution to frequency control. It does not identify the neurons that compare feedback with a preferred frequency, and it does not recreate every property of a naturally moving target. Natural Doppler shifts and an electronic shift can differ in how they affect the frequency-modulated parts of a call.'
],('schuller74_fig2','C74','2','Emission-frequency compensation under increasing positive echo shifts, in Hz.'))

add('Compensated echoes sit slightly above resting frequency','C74',[
'The **reference frequency** is the returning CF frequency maintained during compensation. In Schuller and colleagues’ experiments, the downward change in emission was slightly smaller than the upward shift imposed on the artificial echo.',
'The resulting echo therefore remained above resting frequency. This **compensation offset**, the difference between reference and resting frequencies, was approximately 50–300 Hz across the bats studied and stayed relatively constant across an individual’s compensation range.',
'Compensation does not mean returning every echo to the stationary emission baseline. It means controlling feedback near an individual reference frequency. A small persistent offset and a large adjustable change in emitted frequency can occur together.'
],[
'An artificial echo combines the bat’s current emitted frequency with the shift added by the playback apparatus. Lowering emission by slightly less than that added shift leaves the returning echo slightly above the resting baseline.',
'The authors called the stabilized returning frequency the reference frequency. The offset between this reference and resting frequency was about 50 to 300 hertz, depending on the animal. Within an animal, that offset remained similar as the imposed shift increased.',
'An emission change and an echo-frequency error are different measurements. A bat can make a large downward change in emitted frequency and still retain a small positive offset in feedback. The regulated echo band is therefore not identical to the average call frequency measured at rest.'
],('schuller74_fig3','C74','3','Echo-frequency offset and emission compensation across imposed shifts, in kHz.'))

add('Frequency compensation has a finite operating range','C74',[
'Positive artificial shifts up to about 4.4 kHz were compensated across the horseshoe bats tested by Schuller and colleagues. Some animals responded over a range extending to about 6 kHz. The operating range was not unlimited.',
'Above an individual’s compensation limit, responses differed. Some bats lowered emission by an insufficient amount, some changed frequency irregularly, and some continued near resting frequency. A large imposed shift did not always produce a proportionately larger correction.',
'These results distinguish the **operating range**, where feedback correction remains effective, from a fixed hearing threshold. Failure at a large shift could reflect sensory, control, or vocal limitations; the behavioral measurements alone do not isolate the limiting mechanism.'
],[
'The electronic shift was increased while the bat’s emission was monitored. Compensation was reliable over a substantial positive range, but the same relation did not extend indefinitely.',
'About 4.4 kilohertz could be compensated across the animals, and some animals compensated shifts approaching 6 kilohertz. At larger shifts, the behavioral response could saturate, become irregular, or disappear.',
'A compensation limit does not by itself establish that the bat cannot hear the shifted sound. The response also depends on the comparison process and the vocal apparatus. These recordings establish the range of the whole auditory-vocal behavior under the playback conditions, rather than a separate limit for each component of the system.'
],('schuller74_fig4','C74','4','An individual compensation function and its reference-frequency offset.'))

add('Early playback tests found little response to lower echoes','C74 M02',[
'In the 1974 experiments, downward shifts of artificial echoes did not evoke a systematic increase in emitted frequency. The bats continued calling near resting frequency, although their calls became somewhat less regular in frequency.',
'This finding supported an initially asymmetric account: echoes above the reference band lowered emission, whereas echoes below it appeared ineffective. However, the intensity dependence of the response was not systematically measured in that study.',
'Metzner and colleagues later tested feedback above and below resting frequency at comparable levels above hearing threshold. Their results changed the interpretation of the earlier asymmetry: a weak response to lower-frequency feedback does not establish that this feedback is absent from vocal control.'
],[
'The original playback experiments produced a clear decrease in emission for positive shifts, but did not produce a comparable increase for negative shifts. That result described behavior under the tested conditions.',
'Frequency and audibility are coupled in a sharply tuned hearing system. A sound below the most sensitive band may have to be much louder to be equally audible. Comparing feedback at the same physical sound level is therefore not necessarily comparing equal auditory stimulation.',
'The later study controlled playback level relative to hearing threshold. Under those conditions, lower-frequency echoes did raise emitted frequency. The historical difference is a change in experimental conditions and interpretation, rather than evidence that the bat’s nervous system acquired a new ability between studies.'
])

add('Equal sound levels need not produce equal audibility','M02 L75',[
'An **audiogram** relates sound frequency to the minimum level required for detection. The horseshoe bat’s auditory fovea has a low threshold near its preferred echo band, with substantially poorer sensitivity at some lower frequencies.',
'**Sound pressure level**, or dB SPL, describes physical sound amplitude. **Sensation level** describes how far a sound lies above the hearing threshold at its frequency. Equal dB SPL values can correspond to different sensation levels.',
'Metzner and colleagues delivered positive and negative frequency shifts at approximately comparable suprathreshold levels. Lower-frequency feedback required louder playback. This control separated the sign of a frequency shift from the reduction in audibility that otherwise accompanies a shift away from the fovea.'
],[
'An audiogram is a frequency-by-frequency measure of detection threshold. A low threshold means that a relatively weak sound can be detected. The narrow sensitive band in a horseshoe bat makes the relation between physical intensity and audibility strongly dependent on frequency.',
'Sound pressure level measures the sound itself. Sensation level expresses that sound relative to the threshold at the tested frequency. A playback below the sensitive band can require a higher sound pressure level to achieve comparable auditory stimulation.',
'The experiment therefore adjusted intensity as well as frequency. Comparing sufficiently audible feedback on both sides of resting frequency tested whether lower-frequency information could participate in call control. The audiogram reproduced in the article supplies the threshold context; the compensation measurements are the study’s behavioral intervention.'
],('metzner02_fig1','M02','1','Auditory thresholds and playback ranges; audiogram credited in the paper to Long and Schnitzler (1975).'))

add('Audible lower-frequency echoes raise emitted frequency','M02',[
'Metzner and colleagues sinusoidally varied the frequency of feedback made from each bat’s own call. A **sinusoidal modulation** is a repeated smooth rise and fall. Feedback shifts extended above or below the animal’s resting frequency.',
'Positive shifts caused emitted frequency to decrease. At sufficient playback levels, negative shifts caused emitted frequency to increase above resting frequency. The opposite changes followed the changing frequency of the artificial echo.',
'The vocal system therefore receives useful feedback from both sides of the resting band. This two-direction response contradicts an explanation in which lower-frequency echoes have no influence on call frequency. It does not imply equally complete correction in the two directions.'
],[
'The playback shift changed gradually and repeatedly rather than remaining at a single value. The animal heard an echo mimic whose frequency depended on its current call and the experimentally imposed modulation.',
'When the echo mimic was shifted upward, the bat lowered emission. When it was shifted downward and presented loudly enough, the bat raised emission above its resting frequency. The change occurred systematically over repeated cycles of the imposed modulation.',
'The presence of an upward vocal correction establishes that feedback below resting frequency can influence the control system. The amount of correction remained smaller in that direction. Sensory participation and compensation completeness are separate claims, and only the former is required to reject a strictly one-sided auditory-feedback account.'
],('metzner02_fig2','M02','2(A–D)','Call and playback changes for positive and negative frequency shifts.'))

add('Upward vocal corrections are smaller than downward ones','M02',[
'In Metzner and colleagues’ playback experiments, bats compensated for roughly 95% of positive shifts but only up to about 22% of the range of negative shifts. Increasing emission above resting frequency was possible but comparatively limited.',
'A negative shift as large as 4.5 kHz produced a maximum observed emission increase of 1.51 kHz. Detecting feedback and generating a full motor correction therefore cannot be treated as the same capacity.',
'The authors related the asymmetry to restrictions on vocal production and discussed constraints involving the larynx. Their behavioral data establish unequal correction in the two directions. They do not independently isolate a particular muscle or biomechanical limit as its sole cause.'
],[
'Compensation performance describes how much of the imposed frequency shift is countered by the bat’s emission change. The correction for positive shifts was much more complete than the correction for negative shifts.',
'The reported comparison was approximately 95 percent versus up to 22 percent. In one negative-shift condition, a shift of 4.5 kilohertz produced a maximum emission increase of 1.51 kilohertz. The animal responded to the feedback without fully cancelling it.',
'The vocal apparatus must convert an auditory correction into a change in the call. The authors proposed that laryngeal constraints contribute to the smaller upward range. The experiment itself measured vocal output during playback; it did not directly measure the mechanical limit of an isolated laryngeal muscle.'
])

add('Removing an imposed shift reverses the vocal correction','M02',[
'A **step perturbation** changes the imposed feedback shift abruptly. Metzner and colleagues first added a positive shift, which lowered call frequency. They then returned the apparatus to zero shift while the animal was still emitting below its resting frequency.',
'At that instant, the playback also fell below resting frequency. The animal increased emission toward its previous baseline. Its correction depended on the current frequency of feedback, not simply on whether the apparatus had previously imposed a positive shift.',
'This sequence tests both directions of control within one closed loop. The returning trajectory reflects the existing state of the animal’s emission as well as the external shift. Zero imposed shift is not immediately equivalent to feedback at resting frequency.'
],[
'The first positive step makes feedback too high. The animal lowers its emitted frequency until the returning signal is closer to its preferred band.',
'When the electronic shift is removed, emission is still low for the first calls. Because the playback is made from those calls, the returning signal is now below resting frequency. The bat consequently raises its emission again.',
'The same physical setting of the playback apparatus can therefore produce different feedback frequencies at different times. The current vocal output is part of the loop. The recovery phase establishes an active upward adjustment, rather than requiring that the bat passively return to its baseline after an upward shift ends.'
],('metzner02_fig3a','M02','3(A)','A positive playback step lowers calls; removal of the step evokes recovery.'))

add('Louder feedback accelerates correction in both directions','M02',[
'Metzner and colleagues varied echo-mimic attenuation while maintaining stepwise frequency perturbations. **Attenuation** is a reduction in signal level. Stronger feedback produced faster vocal adjustment for both upward and downward corrections.',
'For recovery after a negative step, reported response time constants shortened from about 2.28 s at 30 dB attenuation to 0.89 s at zero attenuation. For positive steps, corresponding values shortened from about 1.64 s to 0.75 s.',
'The **time constant** describes the measured progress toward the adjusted call frequency. These differences require the control response to depend on feedback strength as well as frequency. A sign-only rule, insensitive to audibility, cannot account for the observed response speeds.'
],[
'Attenuating an echo mimic by 30 decibels makes it weaker than the unattenuated playback. The study compared correction trajectories across different playback levels while controlling the imposed frequency change.',
'Stronger feedback accelerated call-frequency recovery and accelerated the lowering response to a positive shift. The reported time constants were on the order of a second for the stronger conditions and longer for weaker feedback.',
'The time constant was measured from the vocal trajectory, using the progress toward the final correction. It is not a directly measured conduction delay in a single neuron. The experiment constrains the behavior of the entire feedback loop and requires an account that includes the strength of the returning acoustic signal.'
],('metzner02_fig3b','M02','3(B)','Call-frequency recovery under strong and attenuated feedback, in seconds.'))

add('The larynx converts auditory correction into call frequency','M02',[
'The **larynx** is the vocal sound-producing organ. Metzner and colleagues described call-frequency control through motor activity reaching the laryngeal apparatus, including the superior laryngeal nerve and the cricothyroid muscle.',
'The **cricothyroid muscle** changes the mechanical state of the vocal apparatus. Its activity must be coordinated with opening and closure of the **glottis**, the airway opening at the vocal folds. The authors proposed that this coordination limits large increases in call frequency.',
'Auditory feedback above and below resting frequency must ultimately produce opposite changes in vocal output. The playback data establish the required output relation, while the proposed biomechanical restriction remains an interpretation informed by earlier motor studies rather than a direct measurement in these experiments.'
],[
'The bat changes its sound by changing motor commands to its vocal apparatus. The superior laryngeal nerve supplies a route through which neural activity can influence the structures controlling call frequency.',
'The cricothyroid muscle participates in changing the mechanical conditions of sound production. Its action is coordinated with activity at the glottis. That coordination can make raising a call above its normal resting frequency different from lowering it below the baseline.',
'Metzner and colleagues used previous stimulation and vocal-production studies to discuss this asymmetry. Their own experiments measured calls during auditory feedback perturbations. Those measurements specify what a successful sensory-to-motor mechanism must accomplish, but they do not provide a muscle recording or a direct biomechanical test of the proposed restriction.'
])

add('Opposed feedback actions can stabilize a vocal set point','M02',[
'A **set point** is the preferred state maintained by a feedback system. Positive and negative echo-frequency deviations evoke opposing vocal changes around the resting band. Louder feedback accelerates both directions of adjustment.',
'Metzner and colleagues argued that an **antagonistic feedback mechanism**, combining opposing effects on vocal motor activity, is consistent with these results. They reported preliminary pharmacological evidence implicating the inhibitory transmitter GABA acting through GABA_A receptors and the excitatory transmitter glutamate acting through AMPA receptors.',
'These receptor names identify proposed synaptic routes for decreasing or increasing activity; they do not identify an anatomically complete circuit. The behavioral study tests frequency correction, whereas its discussion of receptor mechanisms refers to earlier preliminary work. Exact cellular connectivity was not established by the playback data.'
],[
'A feedback loop must change output in opposite directions when its returning signal lies above or below the desired band. The dependence on echo strength also constrains how sensory activity is converted into a correction.',
'The authors proposed opposed inhibitory and excitatory actions. GABA is a neurotransmitter associated here with an inhibitory pathway through GABA_A receptors. Glutamate is the neurotransmitter associated with an excitatory pathway through AMPA receptors. A neurotransmitter is a chemical signal acting at a synapse, and a receptor is the molecular target through which it affects the receiving cell.',
'The receptor account in this paper was linked to preliminary pharmacological work, not demonstrated by the call recordings themselves. It supports a mechanistic hypothesis without supplying a complete map of cell types, receptor distributions, or the connections that implement the comparison.'
])

add('Cochlear recordings separate receptor and neural signals','S75',[
'The **cochlea** is the inner-ear structure that converts sound into receptor activity. Suga and colleagues recorded **cochlear microphonics**, or CM, electrical responses related to acoustic stimulation of the cochlea, using an electrode at the round window.',
'They also recorded the **N1 response**, summed activity of primary auditory neurons. CM and N1 therefore sampled different stages of peripheral processing: receptor-related activity and neural discharge. Tone bursts allowed the researchers to compare responses during sound and at its onset and cessation.',
'The paper’s short CM stimuli lasted 4 ms, with rapid rise and decay. Stimulus frequency and sound pressure were controlled at the ear. These recordings test whether narrow frequency selectivity and offset responses already arise peripherally, before a cortical interpretation of echo information.'
],[
'The round window provides a recording site near the cochlea. The cochlear microphonic follows acoustic stimulation and is a receptor-related electrical signal; it is not a count of action potentials from one neuron.',
'The N1 signal represents the summed activity of primary auditory neurons. Recording both signals allows a receptor-related transient to be compared with a transient in neural discharge. Their similarity can support a peripheral origin for a neural response, although the two measurements are not interchangeable.',
'Suga and colleagues presented controlled tone bursts and calibrated their amplitude at the ear. Short bursts exposed onset and offset effects while reducing interference from the middle-ear muscle reflex. The frequency dependence of these effects supplied evidence about the sharply tuned mechanical properties of the inner ear.'
],('suga75_fig1','S75','1(A–B)','Round-window cochlear and neural responses to calibrated tone bursts.'))

add('The cochlear response is sharply tuned near CF2','S75',[
'**CF2** is the constant-frequency component of the second harmonic. In Suga and colleagues’ mustached bats, _Pteronotus parnellii_, CF2 lay near 61–62 kHz. The CM threshold curve contained a pronounced sensitivity notch in approximately this band.',
'The best frequencies depended on the recorded response: CM onset was most sensitive near 61–62 kHz, summed neural onset near 63–64 kHz, and summed neural offset near 60–61 kHz. **Onset** and **offset** refer to the beginning and cessation of the stimulus.',
'A sharply tuned receptor-related response indicates specialization before cortical processing. The difference between neural onset and other thresholds requires attention to the response envelope and synchrony; it does not mean the hearing system’s preferred echo band is simply 63–64 kHz.'
],[
'The second harmonic of the constant-frequency call is abbreviated CF2. Its frequency was about 61 to 62 kilohertz in the mustached bats studied. The receptor-related threshold curve had a narrow notch near that range.',
'The minimum threshold of a response identifies the sound level required to evoke it. The recorded CM onset, neural onset, and neural offset signals did not have identical best frequencies. An onset response measures a different event from discharge at the cessation of the same sound.',
'The narrow CM sensitivity supports a peripheral specialization. Suga and colleagues related the displaced neural onset minimum to the time course of cochlear excitation. A population onset measure is therefore not a complete substitute for sustained hearing sensitivity or for the tuning of individual neurons.'
],('suga75_fig2','S75','2(A–C)','Threshold notches of CM onset, neural onset, and neural offset, in kHz.'))

add('A cochlear resonator prolongs excitation after sound ends','S75',[
'A **resonator** responds especially strongly near a particular frequency and can continue oscillating after stimulation stops. Near the CF2 band, Suga and colleagues found that CM activity built up and decayed slowly compared with responses farther from the tuned range.',
'The residual CM activity after stimulus cessation was called **CM-after**. Its transient behavior was consistent with mechanical ringing in the inner ear. A neural offset response accompanied these peripheral events rather than requiring a new acoustic pulse.',
'Resonance links high frequency selectivity to a distinctive time course. The ear does not reproduce the imposed tone-burst envelope identically at every frequency. A sound with a sharp external ending can therefore produce continuing or changing receptor excitation inside the cochlea.'
],[
'Mechanical resonance combines frequency preference with persistence in time. A system that is strongly energized near its resonant frequency can continue moving after the external driving sound stops.',
'The recorded cochlear microphonic had a slow build-up and residual activity near the tuned CF band. Suga and colleagues called the residual activity CM-after. The measurements connected the neural activity at stimulus offset to events already present in the cochlear signal.',
'The external acoustic envelope specifies when sound is delivered, whereas the cochlear envelope specifies how the peripheral response develops. Those envelopes differed near resonance. A neural response after the stimulus cannot consequently be assumed to originate from a central rebound mechanism solely because the loudspeaker has become silent.'
],('suga75_fig3','S75','3(A–B)','Different best frequencies of cochlear and neural onset and offset responses.'))

add('Onset synchrony depends on the sound envelope','S75',[
'The **envelope** is the changing amplitude of a sound or response over time. Slow cochlear build-up near resonance can spread the onset times of individual neural impulses. A summed neural onset response becomes smaller when those impulses are less synchronized.',
'Suga and colleagues varied the rise time of tones away from the resonant band. Lengthening rise time raised the threshold of the summed onset response. A 1 ms rise produced an approximately 8 dB threshold increase relative to an abrupt rise; a 3 ms rise produced a much larger increase.',
'This control supports an envelope-based explanation of the apparent onset-threshold shift. A weak summed response can result from dispersed spike timing even when individual neurons remain sensitive. Population synchrony and acoustic sensitivity must be distinguished.'
],[
'The amplitude envelope determines how quickly a sound reaches its sustained level. Individual neurons need not fire their first impulses at precisely the same time when excitation rises slowly.',
'A summed onset potential depends on those impulses overlapping in time. If they are spread out, the recorded population peak can be smaller without requiring every neuron to become less responsive. The experiment lengthened the stimulus rise time at frequencies away from resonance to test this timing effect independently.',
'The onset threshold rose when the sound rose more slowly. That result supports the interpretation that resonance can alter the apparent neural onset sensitivity by changing synchronization. It does not require the entire auditory system to prefer the frequency at which the largest summed onset response happens to be measured.'
],('suga75_fig4','S75','4(A–B)','Cochlear transients and the dependence of neural onset threshold on rise time.'))

add('Cochlear responses are nonlinear near resonance','S75',[
'A **response-amplitude function** relates stimulus level to the size of the recorded response. Suga and colleagues compared CM during sound and at offset across frequencies and sound pressure levels.',
'Near 60 kHz, sustained CM amplitude reached a plateau around 70–80 dB SPL before increasing again at higher levels. CM offset had a different growth pattern and could exceed the sustained response over part of the tested intensity range.',
'This **nonlinearity** means that doubling an acoustic input does not imply a proportionate response at every level. Frequency and intensity jointly determine the cochlear response. The offset signal cannot be explained as a fixed, scaled copy of the sustained CM activity.'
],[
'The stimulus amplitude was varied while the investigators measured the cochlear microphonic. A response-amplitude function specifies how the peripheral electrical response changes with the level of sound delivered at the ear.',
'Near the offset-sensitive band, the sustained response grew, reached a plateau, and then increased again at higher levels. The offset response followed a different relation. At some stimulus levels it was larger than the sustained response, despite occurring after the external tone had ended.',
'The difference establishes that the cochlea’s temporal response is not simply proportional to stimulus strength. It also explains why onset, sustained, and offset activity need separate measurements. The plotted microvolts describe recorded electrical amplitude, while the horizontal sound-pressure axis describes the acoustic stimulus.'
],('suga75_fig5','S75','5','Sustained and offset CM amplitude as a function of sound pressure level.'))

add('Middle-ear contraction preserves the tuning notch','S75',[
'The **ossicular chain** is the set of middle-ear bones transmitting sound toward the cochlea. The **stapedius muscle** can alter this transmission by changing the mechanical conditions of the chain.',
'Suga and colleagues electrically stimulated the stapedius and measured cochlear thresholds. Contraction reduced sensitivity over the tested range, but its effect was comparatively small near the sharply tuned CM band. The narrow cochlear specialization remained identifiable.',
'The control tested whether middle-ear mechanics could account for the resonance-like tuning. Changing sound transmission affected response level without eliminating the distinctive cochlear notch. The results argue against treating the ossicular chain as the sole source of the narrow frequency specialization.'
],[
'Sound reaches the inner ear through mechanical transmission involving the middle-ear bones. Contraction of a middle-ear muscle can change that transmission, so the researchers tested its effect instead of assuming that all sharp tuning arose inside the cochlea.',
'They stimulated the stapedius muscle electrically and compared threshold curves before and during contraction. Sensitivity changed across frequencies, but the sharp feature near the tuned CF band was not removed.',
'This intervention distinguishes an effect on transmission from an explanation of the frequency notch itself. The middle ear can influence how much sound reaches the cochlea, while the narrow tuning remains associated with the inner-ear system. The result does not make middle-ear control irrelevant to hearing; it limits its explanatory role for this particular specialization.'
],('suga75_fig6','S75','6(A–B)','Threshold changes during stapedius contraction and their frequency dependence.'))

add('Sharp tuning survives loss of the ossicular chain','S75',[
'Suga and colleagues also disrupted middle-ear transmission more directly by eliminating the ossicular chain in a preparation. Overall hearing sensitivity was greatly reduced, as expected when the usual mechanical route to the cochlea was interrupted.',
'The sharp tuning associated with the offset CM response nevertheless remained near its original frequency. A receptor-related frequency specialization survived despite the large change in how sound was delivered to the inner ear.',
'The persistence of this notch supports an **inner-ear origin** for the resonance. Reduced sensitivity and loss of selectivity are different outcomes. The preparation was an invasive control of peripheral mechanics, not a demonstration of normal echo detection after middle-ear removal.'
],[
'Eliminating the ossicular chain removes the normal chain of middle-ear bones that transmits sound toward the cochlea. The investigators expected a substantial decrease in sensitivity, and that decrease occurred.',
'The critical comparison was whether the narrow tuned feature disappeared along with sensitivity. It did not. The offset-related cochlear microphonic retained a sharp frequency preference near the original band.',
'The experiment therefore supports a mechanical specialization within the inner ear rather than one generated exclusively by the middle-ear bones. It cannot establish that the manipulated animal would perform normal echolocation. The invasive preparation was used to locate the source of tuning, and its poor overall sensitivity must be kept separate from the persistence of the frequency notch.'
],('suga75_fig7','S75','7(A–B)','Cochlear offset tuning before and after disruption of ossicular transmission.'))

add('Terminal FM suppresses cochlear offset transients','S75',[
'Suga and colleagues compared a CF tone ending abruptly with the same tone followed by a downward FM component. The added sweep changed the cochlear response after the sustained tone rather than merely adding a second independent response.',
'A terminal FM sweep reduced residual CM activity and the summed neural offset response under the tested conditions. The effect depended on the sweep’s extent and duration. CF and FM therefore interact in the peripheral time course of excitation.',
'The finding connects the acoustic structure of a natural CF-FM signal to cochlear mechanics. It does not establish that every terminal sweep eliminates all residual excitation during free flight. The stimulus comparisons isolate how a controlled FM ending modifies a tuned CF response.'
],[
'A pure CF tone with an abrupt ending can leave a resonating cochlear response. The experiment added a downward frequency sweep to the end of that tone, creating a CF-FM stimulus more similar to a bat’s call.',
'The cochlear residual response and the summed neural offset response were reduced. Changing the duration and extent of the terminal sweep changed the outcome, so the components cannot be treated as independent sounds whose responses simply add together.',
'This interaction was measured in controlled peripheral recordings. It establishes that a brief FM ending can alter how the resonant system stops responding to CF stimulation. It does not directly measure prey capture or prove that the same degree of suppression occurs for every natural call and echo.'
],('suga75_fig8','S75','8(A–D)','Terminal FM changes cochlear ringing and the summed neural offset response.'))

add('Peripheral neurons can discharge when a tone ends','S75',[
'Suga and colleagues recorded individual peripheral auditory neurons, sampling the auditory nerve and nearby cochlear nucleus. A **post-stimulus-time histogram** aligns impulses from repeated trials to the onset of the same stimulus.',
'Individual neurons could produce sustained activity during a tone and concentrated discharges after its cessation. For some tested frequencies and levels, the offset discharge remained prominent even when sustained activity was weak.',
'These offset responses linked the summed N1-offset signal to individual neural activity. They occurred in neurons with excitatory tone responses, rather than requiring a separate population responding only at offset. Peripheral sampling and recording location limit claims about an exclusively cortical mechanism.'
],[
'An individual neuron’s impulse times can be compared across repeated presentations of a tone. Aligning those times to stimulus onset produces a post-stimulus-time histogram, which distinguishes onset, sustained, and later activity.',
'The sampled neurons included auditory-nerve and nearby cochlear-nucleus recordings. Some neurons produced a distinct cluster of impulses after the tone ended. At lower levels or particular frequencies, this offset cluster could remain conspicuous while the sustained response was much weaker.',
'The observation supplies a cellular counterpart to the summed neural offset potential. These were not necessarily neurons with an exclusive offset-only function. The data relate individual activity to peripheral transients and cannot be used to assign the same response to a specific cortical cell type.'
],('suga75_fig9','S75','9(A–D)','Single-neuron responses across tone frequency and level, with offset discharges.'))

add('Neural tuning narrows near the preferred echo band','S75',[
'A **tuning curve** gives the sound levels and frequencies that excite a neuron. Its **best frequency** is the frequency of greatest sensitivity. Suga and colleagues measured tuning curves from individual peripheral auditory neurons using calibrated tone bursts.',
'Neurons near the mustached bat’s CF2 band had much narrower excitatory areas than many neurons at other frequencies. Their narrow tips allowed small changes near 61 kHz to activate different subsets of neurons.',
'The frequency code is therefore supported by selective peripheral inputs. A narrow tip does not imply absolute selectivity at every level: as stimulus intensity rises, the excitatory region of an auditory-nerve tuning curve can widen. Frequency preference must be evaluated together with stimulus level.'
],[
'A tuning curve is obtained by varying frequency and finding the level needed to evoke a response. Its lowest threshold identifies the neuron’s best frequency. The full curve also specifies the range of frequencies that can excite the neuron at higher levels.',
'The peripheral neurons near the CF2 band had particularly narrow tuning tips. Such tuning makes a small change in echo frequency alter which neurons are strongly driven. That is a population code supported by frequency-selective inputs.',
'The same neuron may respond to a wider frequency range when a sound is louder. A sharp threshold tip must therefore not be interpreted as an unchanging narrow band for all intensities. Suga and colleagues compared both frequency and level rather than assigning selectivity from the best frequency alone.'
],('suga75_fig11','S75','11','Individual peripheral tuning curves across the hearing range.'))

add('Q values quantify the narrowness of a tuning curve','S75',[
'**Bandwidth** is the range of frequencies encompassed by a tuning criterion. Suga and colleagues used **Q at 10 dB above threshold**, a measure that compares a neuron’s best frequency with the width of its excitatory band at that level.',
'A larger Q indicates a narrower relative band. Mustached-bat neurons near the CF2 region reached much higher Q values than most neurons elsewhere in their hearing range. The paper also compared this pattern with previously recorded neurons from an FM-using bat.',
'The comparison describes different distributions of peripheral selectivity. It does not imply that every mustached-bat neuron is sharper than every neuron in the other species. The strongest specialization is concentrated within a particular, behaviorally relevant frequency region.'
],[
'Bandwidth describes how much frequency space lies within a specified response criterion. Q expresses narrowness relative to best frequency, so a larger Q corresponds to a relatively narrower tuned band.',
'The criterion here was 10 decibels above the neuron’s minimum threshold. That fixed level makes the tuning widths comparable without assuming that curves have the same width at every intensity. The mustached-bat distribution contained especially high values near the CF region.',
'The comparison with Myotis lucifugus used earlier neuronal data included in Suga’s article. It supports a specialization concentrated near the mustached bat’s preferred echo band. The overlap and spread of the measurements remain part of the result; species labels do not substitute for the tuning of a particular neuron.'
],('suga75_fig12','S75','12(A–B)','Q values versus best frequency in mustached and little brown bats.'))

add('The highest peripheral selectivity clusters near 61 kHz','S75',[
'Within the 50–70 kHz range studied closely by Suga and colleagues, the largest Q values were concentrated near 61 kHz. Values were generally lower for best frequencies below or above that narrow region.',
'This local peak corresponds to the range of CF2 signals and compensated echoes in the studied mustached bats. Peripheral frequency selectivity is organized around a particular acoustic operating band rather than distributed uniformly across ultrasound.',
'The relation is an alignment between vocal behavior and sensory tuning. It supports fine analysis near the carrier used for echolocation. The recordings do not show that the peripheral neurons themselves perform the motor correction that maintains echo frequency in this band.'
],[
'The researchers examined tuning especially closely around the constant-frequency second harmonic. The distribution of Q values had its largest values near 61 kilohertz, rather than showing the same selectivity throughout the measured region.',
'This frequency range overlaps the CF2 band used by the mustached bats and the preferred returning band during compensation. That alignment supports a sensory role for the peripheral specialization.',
'A neuron’s sharp tuning and a bat’s ability to change its call are connected but distinct observations. The recordings establish selective input capable of distinguishing small frequency differences. They do not demonstrate that an auditory-nerve neuron directly issues a laryngeal motor command. Frequency correction requires a sensory-to-motor pathway beyond these peripheral measurements.'
],('suga75_fig13','S75','13','A local peak of peripheral Q values near the CF2 band.'))

add('Low threshold and narrow tuning are different properties','S75',[
'**Minimum threshold** is the weakest sound level that evokes an excitatory response. **Selectivity** describes how restricted that response is across frequencies. A neuron can be sensitive without having an exceptionally narrow tuning curve.',
'Suga and colleagues plotted minimum thresholds against best frequency and separately measured Q values. The lowest peripheral thresholds clustered near the CF2 band, but the threshold distribution and the sharpness distribution measured different aspects of hearing.',
'The **auditory fovea** combines strong sensitivity with detailed frequency representation. Neither a low threshold alone nor a narrow curve alone specifies the full specialization. Comparing both measurements prevents a population onset potential from being mistaken for a complete description of the tuned hearing system.'
],[
'Threshold asks how weak a sound can be and still excite the neuron. Frequency selectivity asks which neighboring frequencies also excite it. Those questions require different measurements.',
'The threshold plot places each neuron according to its best frequency and its minimum effective sound level. The Q plots instead describe the relative width of its tuned band. Suga and colleagues found an important concentration of sensitivity and selectivity near the CF region, but did not equate these quantities.',
'The distinction also matters when considering the summed neural onset signal. A population peak can depend on synchronized impulse timing, whereas a single-neuron threshold depends on whether that neuron responds. The foveal specialization has to be described using these measurements together rather than inferred from one peak or one minimum.'
],('suga75_fig14','S75','14','Minimum excitatory thresholds versus neuronal best frequency.'))

add('Offset tuning can differ from the same neuron’s onset tuning','S75',[
'Suga and colleagues mapped the frequencies and levels evoking excitation during sound and discharge after sound cessation in the same peripheral neurons. These two response regions were not always centered at the same frequency.',
'Offset best frequencies clustered around 59.5–61.5 kHz, even when the neuron’s onset or sustained best frequency differed. The offset band corresponded closely to the cochlear offset-sensitive region.',
'The response of one neuron can therefore reflect more than one temporal feature of cochlear excitation. An onset best frequency does not fully predict its offset behavior. The relation supports the contribution of a common mechanical transient to offset firing across neurons with different excitatory best frequencies.'
],[
'The investigators compared two response regions for the same neuron: excitation associated with the tone and discharge occurring after it ended. The frequencies giving the greatest response need not be identical for those events.',
'The offset-sensitive frequencies clustered near 59.5 to 61.5 kilohertz. That clustering persisted across neurons whose ordinary excitatory best frequencies varied more widely. The mechanical offset response of the cochlea had a corresponding frequency preference.',
'This relation makes a common peripheral transient a plausible source of the offset discharge. Assigning a neuron one best frequency is useful but incomplete when its activity depends on when the measurement is made. Onset, sustained activity, and offset each carry information about how the cochlea and peripheral neurons respond to the same stimulus.'
],('suga75_fig15','S75','15(A–H)','Excitatory and offset-sensitive areas recorded from the same neurons.'))

add('An offset discharge need not be rebound from inhibition','S75',[
'**Inhibition** reduces neural activity. A **rebound response** would occur after inhibitory activity ends. Suga and colleagues tested whether peripheral offset firing required suppression of a neuron’s spontaneous discharge during the preceding tone.',
'Offset responses occurred without the necessary preceding inhibition. The researchers also identified separate inhibitory response regions and tested interactions between two tones. Inhibition was measurable in some neurons, but it did not explain all offset firing.',
'**Two-tone suppression** is reduced excitation during simultaneous presentation of another sound. Its presence is distinct from proving an inhibitory rebound mechanism. The paired-tone and offset measurements require mechanical transients and neural suppression to be evaluated separately.'
],[
'A rebound account predicts an association between preceding inhibition and discharge after that inhibition ends. The peripheral recordings did not meet that requirement for all offset responses: some appeared without suppression of spontaneous activity during the tone.',
'Suga and colleagues also obtained evidence of inhibition in other stimulus regions and measured suppression when two sounds were delivered together. Those effects demonstrate interactions in the peripheral response without turning every later discharge into an inhibitory rebound.',
'Two-tone suppression describes the response to simultaneous acoustic inputs, whereas an offset discharge describes activity after a stimulus ends. The two observations need different causal tests. The authors linked the offset response to cochlear transients and distinguished it from the inhibitory effects that were also present in the sampled auditory neurons.'
],('suga75_fig16','S75','16(A–B)','Inhibitory response regions and two-tone suppression measured separately.'))

add('Terminal FM also reduces single-neuron offset discharge','S75',[
'Suga and colleagues compared a CF tone with a CF tone followed by a brief downward FM sweep while recording single peripheral neurons. The added FM component reduced the discharge concentrated after the CF component ended.',
'The test used the same neuron and varied sound level, allowing CF-only and CF-FM responses to be compared directly. The decrease in offset discharge paralleled the reduction of cochlear after-activity and the summed neural offset response.',
'The result connects peripheral mechanics to the firing pattern of individual neurons. It does not establish that terminal FM universally inhibits every auditory neuron. The observed interaction concerns a particular transient response evoked by a tuned CF stimulus.'
],[
'The comparison preserved the constant-frequency portion and changed how it ended. A terminal downward sweep reduced the later discharge in the recorded neuron, rather than producing the same response as the CF tone alone.',
'Testing the same neuron under CF-only and CF-FM conditions controls for differences between neurons. Repeating the comparison at different sound levels also separates a stimulus-structure effect from a result observed at just one intensity.',
'The reduction corresponds to the earlier cochlear and summed-neural findings. It links the terminal acoustic sweep to a change in peripheral impulse timing. The experiment does not imply that all FM stimulation is inhibitory or that all neurons respond in this way; it concerns the offset transient accompanying the particular CF response.'
],('suga75_fig17','S75','17(A1–A3, B1–B3)','CF-only and CF-FM stimuli produce different offset spike patterns.'))

add('Peripheral impulses can track beats between nearby tones','S75',[
'**Beats** are periodic amplitude fluctuations produced when tones of slightly different frequency overlap. Suga and colleagues presented paired tones and recorded whether peripheral impulses followed the resulting fluctuations.',
'**Phase locking** means that discharge occurs at a consistent phase of a repeating stimulus feature. Peripheral neurons could phase-lock to beats up to about 3 kHz. Changing the separation between tones changed the rate of the amplitude fluctuations.',
'This timing code complements the code supplied by sharply tuned best frequencies. Overlapping emitted CF signals and returning echoes can provide beat information, but the paired-tone recordings do not establish which cue a freely flying bat relies on in every compensation decision.'
],[
'Two nearby tone frequencies produce a repeating change in their combined amplitude. Those fluctuations are beats. The experiment changed the difference between the tones and measured the times at which peripheral neurons discharged.',
'Phase locking refers to a consistent relation between impulse timing and a phase of the repeating amplitude pattern. The neurons could follow beat rates up to approximately 3 kilohertz. Their impulse timing therefore supplied information beyond the average number of impulses produced by a tone.',
'Suga and colleagues related this property to overlap between outgoing signals and echoes. That is a potential temporal representation of frequency difference, alongside the representation supplied by sharply tuned neurons. The laboratory recordings demonstrate the available peripheral signal; they do not select one exclusive behavioral cue for natural flight.'
],('suga75_fig18','S75','18(A–B)','Peripheral impulse timing follows beat envelopes at different frequency separations.'))

add('The cortex devotes extensive space to the CF echo band','S77',[
'The **primary auditory cortex** is a cortical region receiving organized auditory input. In Suga’s mustached-bat study, the Doppler-shifted-CF processing area occupied about 2.3 mm², approximately 30% of primary auditory cortex.',
'Its neurons were concentrated near the 61–63 kHz band associated with CF components of emitted signals and echoes. This large representation mirrors the peripheral specialization but adds cortical response properties beyond a neuron’s best frequency.',
'**Tonotopy** is an orderly representation of frequency across neural tissue. Suga examined how neurons sharing a best frequency differed in preferred sound amplitude. The enlarged CF region was not simply a collection of interchangeable neurons carrying identical information.'
],[
'The primary auditory cortex contains an organized representation of sound. Suga described an unusually large region concerned with the constant-frequency echo band of the mustached bat, occupying roughly 30 percent of that cortical area.',
'Tonotopy means that frequency preference changes systematically with location. Within the enlarged CF region, many neurons could share similar best frequencies. The experiment therefore measured their response to sound amplitude as well as frequency.',
'The cortical representation adds another dimension to the peripheral frequency code. The measured area and tuning describe auditory representation, not proof that this entire cortical region is necessary for every compensation response. Suga also cautioned that the region’s specialization does not exclude responses to signals other than orientation calls and their echoes.'
])

add('Some cortical neurons prefer an intermediate sound level','S77',[
'A neuron’s **best amplitude** is the sound pressure level producing its largest response. Suga measured impulse counts during 50 ms tones at each cortical neuron’s best frequency and compared response growth across sound levels.',
'Many CF-region neurons had **nonmonotonic** responses: impulse counts rose with amplitude, reached a maximum, then fell at stronger levels. Other neurons showed more nearly monotonic growth. Preferred amplitude therefore differed from minimum threshold.',
'An **upper threshold** marks a level above which excitation becomes weak or absent. These cortical response limits create amplitude selectivity that cannot be described solely as increasing discharge to louder sounds. Frequency and sound level jointly determine which cortical populations are most active.'
],[
'The investigators held tone frequency at a neuron’s best frequency and increased sound level. Some neurons produced more impulses up to an intermediate amplitude, then produced fewer impulses as the sound became stronger.',
'That rise followed by a fall is a nonmonotonic response. The amplitude giving the peak is the best amplitude. Minimum threshold is different: it identifies the weakest effective sound, not the level producing the maximum response.',
'The loss of excitation at higher levels can create an upper threshold. Suga related this property to inhibitory interactions elsewhere in the auditory pathway. The cortical recordings establish level-selective response functions, while the origin of every neuron’s inhibitory input was not directly reconstructed in this mapping experiment.'
],('suga77_fig1a','S77','1(A)','Cortical impulse-count functions have different preferred sound levels.'))

add('Columns share frequency and amplitude preferences','S77',[
'Suga inserted electrodes approximately perpendicular to the cortical surface. Neurons encountered along an individual penetration had similar best frequencies, response thresholds, and preferred amplitudes, supporting a **columnar organization** of those properties.',
'A **cortical column** here means a depth-oriented grouping with related response preferences. Across the cortical surface, best frequency and best amplitude changed systematically. Suga mapped these two properties using single-neuron and multi-unit responses.',
'**Multi-unit activity** combines responses from several nearby neurons. The similarity of neurons within a penetration made it useful for mapping local preferences. It does not resolve the synaptic connections among those neurons or prove that every cell in a column has identical selectivity.'
],[
'An electrode penetration samples neurons at different depths beneath a surface location. Suga found that neurons along a penetration tended to share their best frequency and best amplitude, along with related response characteristics.',
'This relation supports a columnar organization: nearby neurons aligned through cortical depth have related preferences. The preference changes when the surface location of the electrode changes, so the cortex contains an ordered map rather than the same response everywhere.',
'Multi-unit recording pools the activity of neighboring cells. Because their preferences were similar at a location, the pooled response could supply an estimate of its best frequency and amplitude. That estimate is useful for mapping but does not identify every cell’s connectivity or replace all single-neuron measurements.'
],('suga77_fig2bc','S77','2(B–C)','Frequency and best-amplitude contours in the mapped CF processing region.'))

add('Amplitude and frequency occupy cortical coordinates','S77',[
'**Amplitopic representation** is an orderly spatial organization of preferred sound amplitude. In Suga’s mapped CF processing area, best-frequency contours and best-amplitude contours followed different directions across the cortical surface.',
'The best-amplitude organization varied among animals. The posterior region consistently placed larger preferred amplitudes dorsally, whereas the anterior region could follow either of two arrangements. The data support structured amplitude representation without a single identical map in every bat.',
'Preferred amplitudes of about 30–50 dB SPL occupied more cortical area than preferred amplitudes of about 80–100 dB SPL. This unequal allocation describes the measured map. Its relation to commonly encountered echo levels was an interpretation rather than a direct measurement of natural echo statistics.'
],[
'Amplitopy refers to a spatial ordering of preferred sound level, just as tonotopy refers to a spatial ordering of preferred frequency. The two properties do not have to change along the same direction across the cortical surface.',
'Suga found a systematic relation between location and best amplitude, but the arrangement was not identical across all animals. Two patterns were described in the anterior part of the CF processing area, while the posterior pattern was more consistent.',
'The maps gave more space to intermediate preferred sound levels than to very high preferred levels. The author proposed a relation to the amplitudes of echoes commonly used in echolocation. The mapping experiment measured neural preference and location; it did not independently sample the complete distribution of echoes encountered by a bat in nature.'
],('suga77_fig2de','S77','2(D–E)','Measured best amplitude varies with cortical position, in dB SPL and degrees.'))

add('Cortical activity represents a spectrum across populations','S77',[
'An **amplitude spectrum** specifies signal amplitude across frequencies. Suga’s cortical data supported a representation in which both frequency preference and preferred amplitude vary with the location of responding neurons.',
'This organization differs from describing amplitude only through the discharge rate of an individual peripheral neuron. Cortical population activity can change spatially when either frequency or amplitude changes, and upper-threshold responses can sharpen that organization.',
'One cortical column does not uniquely identify target velocity or target size. Tuning curves and amplitude-response functions have finite widths, so multiple locations can respond to a signal. The representation concerns a pattern of population activity rather than a single neuron that unambiguously labels an object.'
],[
'A signal’s amplitude spectrum describes how amplitude is distributed across its frequency components. Suga proposed that the CF-region population represents that distribution through the locations of neurons with appropriate frequency and level preferences.',
'At the periphery, increasing amplitude often changes discharge rate within a frequency-selective population. In the cortex, a stronger signal can also change which populations are most strongly activated because different locations prefer different amplitudes.',
'The preferences are not infinitely sharp. A particular acoustic signal can activate several columns, and a column can respond to a range of signals. Consequently, the activity at one cortical site cannot uniquely specify a target’s velocity or size. The interpretation depends on the distributed response and the acoustic conditions producing the echo.'
])

add('Free flight lowers emission while preserving echo frequency','H18',[
'Schoeppler and colleagues studied _Hipposideros armiger_ flying toward a landing grid. They recorded echolocation signals, reconstructed the flight trajectory, and calculated the frequency of echoes from targets ahead using the measured flight speed.',
'During acceleration, emitted CF2 frequency decreased. In a representative flight, the minimum emission frequency coincided with a maximum speed of 4.7 m/s. The calculated returning frequency remained close to the animal’s reference band.',
'This separates the changing outgoing signal from the controlled echo estimate. The study used natural flight, but the displayed echo frequency was calculated from call frequency and kinematics; it was not a direct recording from the bat’s cochlea or a microphone at its ear.'
],[
'The bats flew toward a grid while calls and flight trajectories were recorded. The reconstruction supplied speed, and the investigators used that speed together with the emitted frequency to calculate the expected Doppler-shifted echo frequency.',
'The emitted second-harmonic CF frequency fell as the bat accelerated. In the example flight, the lowest emission coincided with a speed of 4.7 metres per second. The calculated echo frequency changed far less than the emitted frequency.',
'The result supplies a natural-flight counterpart to playback experiments. Its echo measure remains an estimate based on recorded calls and reconstructed movement. The method does not directly measure cochlear stimulation, and the distinction between recorded emission and calculated echo frequency is necessary when assessing the evidence for compensation precision.'
],('schoeppler18_fig2ef','H18','2(e–f)','Measured emission and flight speed, with calculated echo frequency.'))

add('Approach changes call timing while CF is retained','H18',[
'**Pulse interval** is the time between consecutive calls; **duty cycle** is the proportion of time occupied by sound emission. Both describe how frequently a bat samples its surroundings, independently of CF frequency.',
'In _H. armiger_, pulse intervals and call durations decreased toward landing. During the final approach, mean call duration reached about 3–4 ms and pulse interval about 11–12 ms. Duty cycle increased, while the CF component remained present.',
'Frequency compensation therefore operates within an acoustic sequence whose temporal structure is also changing. The terminal approach is not a sequence of otherwise identical calls. Timing, harmonic prominence, and the FM component can change while the returning CF band remains regulated.'
],[
'Pulse interval measures the time from one call to the next. Duty cycle measures how much of the sequence is occupied by emitted sound. Shortening intervals and shortening calls can change duty cycle in different ways, so all three quantities must be measured.',
'The Hipposideros armiger calls became shorter and more closely spaced near the landing grid. The final approach included calls of roughly 3 to 4 milliseconds and intervals of roughly 11 to 12 milliseconds. The sustained CF component was retained.',
'The bat was therefore changing the timing of sampling at the same time that it controlled frequency. These measurements describe flight toward a landing target, not prey capture. The frequency, duration, interval, and harmonic changes belong to the observed approach behavior and should not be treated as identical results for every hunting situation.'
],('schoeppler18_fig2','H18','2(a–f)','Call timing, FM properties, duty cycle, and compensation during approach.'))

add('Resting and reference frequencies shift together','H18',[
'Schoeppler and colleagues measured resting frequency immediately before each flight and reference frequency from the corresponding calculated echoes. The absolute values changed between flights and across recording days, rather than remaining permanently fixed.',
'The two frequencies remained closely coupled. Their mean offset was about 80 Hz, with the reference usually above the resting frequency. In one bat, reference frequency declined by about 1 kHz over nine days.',
'A drifting absolute frequency does not by itself imply poor compensation. Comparing an echo estimate from one time with a resting measurement from another can exaggerate the offset. A contemporaneous baseline is required to distinguish movement of the preferred band from error around that band.'
],[
'The investigators measured the resting call series just before take-off and paired it with the echo estimate from that particular flight. This pairing matters because both frequencies can change across time.',
'The resting and reference values usually moved in the same direction. Their mean separation remained approximately 80 hertz even though one animal’s reference frequency declined by about a kilohertz over nine days.',
'A precise control system can track a preferred state that itself changes. Using a resting value from an earlier session would mix that shift with the actual compensation offset. The observed coupling is therefore more informative than asking whether every call remains at one absolute frequency for the lifetime of an individual bat.'
],('schoeppler18_fig3','H18','3(a–b)','Paired resting and reference frequencies and their offsets across flights.'))

add('Precision within a flight differs from stability across days','H18',[
'**Control precision** describes how closely echo frequency remains near the reference within a flight. **Longer-term stability** describes how little that reference changes across flights or days. These are different properties of the feedback system.',
'In Schoeppler and colleagues’ recordings, emission changed with speed while calculated echoes stayed near the reference. Deviations from the reference were only weakly related to speed across the tested trajectories, with greater variation at low speeds.',
'The natural-flight results challenged the assumption that hipposiderid compensation is inherently imprecise. A varying baseline can coexist with tight regulation around that baseline. The evidence concerns the studied animals and flight conditions, rather than proving identical performance in every hipposiderid species.'
],[
'Within-flight precision is measured relative to the reference appropriate for that flight. Longer-term stability concerns whether that reference stays at the same absolute frequency across sessions.',
'The calculated echo frequency remained near the reference over a range of flight speeds. The deviations were only weakly predicted by speed, although they were more variable near low speeds. The outgoing calls changed much more substantially with movement.',
'These data separate a shifting preferred frequency from inaccurate regulation. They support precise compensation in the studied Hipposideros armiger preparation and revise an interpretation based on measurements taken at different times. The result is not a measurement of every hipposiderid, and the echo estimates depend on the reconstructed flight and the target geometry used in the study.'
],('schoeppler18_fig4','H18','4(a–b)','Calculated echo frequency and deviation from the flight-specific reference versus speed.'))

add('Resting call frequency rises as torpid bats warm','H22',[
'**Torpor** is a state of reduced physiological activity associated here with lower temperature. Schoeppler and colleagues attached a miniature logger between the shoulder blades of _H. armiger_ and recorded skin temperature together with echolocation calls.',
'After the experimenter entered the room, resting bats became more active, warmed, and increased their CF2 resting frequency. The largest frequency rise during activation reached about 1.44 kHz. The change occurred without a flight-induced Doppler shift.',
'The experiment links physiological state to the frequency emitted at rest. It does not isolate temperature from every accompanying change in activity, and the logger measured skin rather than cochlear temperature. The result requires a baseline that can vary even when the animal is stationary.'
],[
'Torpor involves reduced physiological activity and, in these recordings, a lower temperature before activation. The investigators measured skin temperature with a small logger on the back and recorded ultrasonic calls at the same time.',
'Entering the room elicited increased calling and warming. As the bats activated, the frequency of their resting second-harmonic CF component rose, in some cases by as much as 1.44 kilohertz. Because these were resting calls, the change could not be assigned to compensation for flight speed.',
'The paired recordings connect call frequency with physiological state. Skin temperature is an indirect indicator of internal temperature, and activation changes more than temperature alone. The measurements support a state-dependent shift of the resting band without directly proving how the temperature of the cochlear resonator changed.'
],('schoeppler22_fig2cde','H22','2(C–E)','Skin temperature, calling activity, and resting CF2 frequency during activation.'))

add('Frequency can peak before measured skin temperature','H22',[
'Schoeppler and colleagues compared the time of maximum resting frequency with the time of maximum skin temperature during activation. The frequency maximum generally occurred earlier, while skin temperature continued increasing.',
'After the skin-temperature maximum, both temperature and resting frequency tended to decline. The timing difference prevents a simple conversion of every skin-temperature change into a fixed frequency change throughout warming and cooling.',
'The authors discussed delayed warming of skin relative to internal tissues as one explanation. Cochlear temperature was not recorded, so that explanation remains indirect. A correlation between two time series does not establish that their maxima must coincide or identify the precise thermal mechanism controlling vocal frequency.'
],[
'The two signals were recorded together, but their peaks were not simultaneous. The bat’s resting frequency usually reached a maximum before the temperature measured at the skin reached its maximum.',
'A sensor on the back does not necessarily follow the temperature inside the cochlea with the same timing. Internal tissues could warm earlier than the skin, but that possibility was not directly tested with a cochlear temperature probe.',
'The later decline in both quantities supports their association while preserving the temporal difference. It would be incorrect to assign a universal kilohertz-per-degree conversion from these skin recordings. The source explicitly distinguishes its measured skin temperature from the unmeasured temperature at the inner-ear resonator.'
],('schoeppler22_fig3a','H22','3(A)','Resting-frequency and skin-temperature peaks differ in time during activation.'))

add('A changing sensory band can coexist with precise feedback','H22 H18 M02',[
'State-dependent resting-frequency changes and the coupling of resting and reference frequencies support an **adaptive operating band**: the feedback system can regulate around a preferred frequency that changes with the animal’s physiological state.',
'Schoeppler and colleagues proposed that the controlled variable is activation of the cochlear foveal resonance system. **Afferent pathways** carry sensory activity toward control centers; **efferent pathways** carry motor commands toward the vocal apparatus, changing the next emitted call.',
'The warming experiment measured skin temperature and emitted frequency, not cochlear activation or a complete neural circuit. Its proposed control account must therefore be distinguished from the directly observed frequency shifts. The behavioral and peripheral studies together constrain how a moving sensory target can remain compatible with precise echo regulation.'
],[
'The preferred acoustic band is not necessarily fixed permanently. The temperature study found state-linked changes in resting calls, and the flight study found that resting and reference frequencies remain coupled when their absolute values shift.',
'The authors proposed regulation of activity in the cochlear resonance system. Afferent input carries sensory information into the nervous system. Efferent output changes the vocal apparatus, and the new call changes the acoustic feedback returning to the ear.',
'That account connects the measured observations, but the warming experiment did not directly record the cochlear activity being proposed as the controlled variable. The strongest established claims remain the change in resting frequency, the relation to skin temperature, and the coupling of resting and reference frequencies measured in the separate flight study. Precise regulation and a changing preferred band are compatible.'
],('schoeppler22_fig5','H22','5','Resting frequency covaries with skin temperature across activation and recovery.'))

spec={'lecture':16,'theme':'espresso-stone','content_slides':44,'slides':slides,'takeaways':{
'cite':'Suga et al. (1975); Suga (1977); Schuller et al. (1974); Metzner et al. (2002); Schoeppler et al. (2018, 2022)',
'refs':[R[k][1] for k in R],
'items':[
{'lead':'Echo frequency is the controlled signal.','text':'CF-FM bats lower emitted CF frequency as approach raises echo frequency, maintaining echoes near an individual reference band.'},
{'lead':'Resting and reference frequencies differ.','text':'The resting emission baseline usually lies slightly below the compensated echo reference; their offset must be measured at the same time.'},
{'lead':'Audible feedback acts in both directions.','text':'Horseshoe bats lower calls for higher echoes and can raise calls for sufficiently audible lower echoes, with unequal correction ranges.'},
{'lead':'The auditory fovea begins peripherally.','text':'Cochlear resonance and sharply tuned peripheral neurons concentrate sensitivity and selectivity near the CF2 echo band.'},
{'lead':'Neural codes include timing and population location.','text':'Peripheral impulses can follow beats; cortical populations organize both frequency and preferred amplitude.'},
{'lead':'Precision can track a changing operating band.','text':'Resting and reference frequencies can shift together, and resting calls change during warming without a flight-induced Doppler shift.'},
]}}
assert len(slides)==44, len(slides)
(ROOT/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
print(f'Wrote {len(slides)} content slides; {sum("figure" in s for s in slides)} article-figure slides')
