"""Lecture 81: teaching prose tied to verified primary studies."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parent
R=json.loads((B/'research.json').read_text());F=json.loads((B/'figure_sources.json').read_text());S=[]
def short(k):return R[k]['author']+' ('+str(R[k]['year'])+')'
def fig(n):
 x=F[n];return {'path':'figures/'+n+'.png','kind':'article','caption':short(x['paper'])+', Fig. '+x['figure']+'. '+x['description']+'.','source_url':'https://doi.org/'+R[x['paper']]['doi']}
def add(title,keys,imgs,text,note):
 body=text.strip().split('\n\n');assert len(body)==3;assert len(title)<=62,title
 keys=list(dict.fromkeys(keys+[F[n]['paper'] for n in imgs]))
 z={'title':title,'body':body,'transcript':[[re.sub(r'\*\*','',p),[]] for p in body]+[note],'cite':'; '.join(short(k) for k in keys),'refs':[R[k]['reference'] for k in keys],'figure_width':5.8}
 if len(imgs)==1:z.update(layout='figure-right',figure=fig(imgs[0]))
 else:z.update(layout='figures-right',figures=[fig(n) for n in imgs],primary_figure_height=2.5)
 
 if imgs in (['g_error','g_histology'],['g_prob','g_histology'],['g_passive','g_histology'],['b_identity','b_anatomy'],['b_onset','b_anatomy']):z.update(figure_arrangement='side-by-side',primary_figure_width=3.8)
 if imgs==['b_branch','b_anatomy']:z.update(primary_figure_height=3.0)
 S.append(z)
add('Feedback changes the song that produced it',['tumer'],['t_song'],'''
A **closed-loop interface** measures an animal’s ongoing behavior and delivers feedback determined by that measurement. Tumer and Brainard recorded adult Bengalese finches while a computer detected particular song elements and selectively overlaid brief bursts of white noise.

The computer measured **pitch**, the perceptual correlate of fundamental frequency, and delivered noise to either higher or lower variants of a target syllable. A **syllable** is a discrete acoustic element within the song sequence. Renditions that escaped noise retained normal auditory feedback.

**Reinforcement** changes the frequency of future actions according to their consequences. Birds shifted the target syllable’s pitch toward variants that escaped disruption. The feedback therefore altered subsequent performances of the same behavior, even though adult song was already stable. Residual variation supplied the alternatives on which reinforcement could act.
''','A closed loop links measurement to intervention on the same ongoing behavior. The experimental feedback was binary: the target rendition either triggered noise or escaped it. The animal was never explicitly told which acoustic feature determined that outcome.')
add('Harmonic syllables provide a measurable vocal target',['tumer'],['t_pitch'],'''
**Fundamental frequency** is the repetition rate of a periodic sound, measured in hertz, or cycles per second. Harmonic syllables contain energy at this frequency and at higher multiples, allowing a computer to estimate their pitch from brief portions of the vocalization.

In one Bengalese finch, the baseline target syllable was centered near **2,281 Hz**. Small differences among repeated renditions provided higher and lower variants without requiring the bird to invent a new song element.

Noise delivered to higher variants shifted the distribution toward lower frequencies over three days. The animal changed how frequently it produced existing variants and moved the overall pitch distribution. A previously stereotyped vocal action therefore remained available for fine adjustment through feedback.
''','A distribution of syllable pitches describes repeated renditions, rather than the frequency spectrum within one syllable. The computer measured the same short acoustic segment on every rendition so the feedback contingency referred to a consistent vocal feature.')
add('Small performance variation supports motor exploration',['tumer'],['t_updown'],'''
**Motor exploration** is variation among actions that allows different outcomes to be sampled. Adult Bengalese finches produced subtle pitch differences despite highly practiced songs. Tumer and Brainard tested whether those differences could become the basis of adaptive learning.

Noise contingent on high-pitch variants favored lower pitches; noise contingent on low-pitch variants favored higher pitches. Opposite contingencies produced opposite changes even though the type of disruptive sound remained the same.

The direction of learning depended on the relationship between the vocal variant and its outcome. Variability supplied selectable alternatives, while feedback favored the alternatives associated with undistorted sound. The behavioral result supports exploration as a functional component of stable adult song rather than treating every fluctuation as irrelevant noise.
''','The two contingencies differ in which renditions receive disruption. An identical feedback sound can therefore drive learning in either direction. The experiment tests the use of natural variability, not the production of arbitrary novel vocal actions.')
add('Adaptive pitch changes accumulate within hours',['tumer'],['t_rapid'],'''
Pitch-contingent reinforcement changed adult Bengalese finch song within the first day of training. Most birds had already shifted toward the escape region within **7 hours**, while the pitch distribution approached a stable trained range over the following days.

In the representative downward-learning experiment, the fraction of renditions triggering noise fell from **91% to 17%** by the third day. The reduction followed a shift in the measured vocal feature, rather than avoidance of the entire singing behavior.

When contingent noise ended, pitch returned toward the original range. The normal song remained a behavioral reference despite the temporary reinforced change. Adaptive control therefore combines ongoing flexibility with a tendency to restore the previously learned vocal pattern when the external contingency disappears.
''','Learning involved many repeated renditions spread through a day. The rapid trajectory distinguishes fine adjustment of an established syllable from the slower acquisition of an entire juvenile song. Recovery followed termination of the feedback manipulation.')
add('Learning selects one feature within a rapid sequence',['tumer'],['t_specific'],'''
A bird could escape disruptive feedback by changing an entire song, but Bengalese finches instead modified the pitch of the targeted syllable. Neighboring syllables retained their usual fundamental frequencies even when they occurred only tens of milliseconds away.

The trained syllable also retained its duration, volume, and **spectral entropy**, a measure of how broadly acoustic energy is distributed across frequencies. Feedback selected the specific dimension used by the computer to decide whether noise would occur.

This precision allows a learned sequence change locally without destabilizing every component. Distinct song features can remain under separate adaptive control, so correction of one vocal gesture preserves the surrounding gestures. The behavioral specificity places a temporal and acoustic constraint on the neural teaching signals that support learning.
''','The same target syllable was assessed for several acoustic properties. A shift in fundamental frequency was accompanied by stable measures of the other properties. The control syllables were part of the same song, providing a within-sequence comparison.')
add('A short feedback delay determines successful learning',['tumer'],['t_delay'],'''
**Latency** is the interval between a measured event and the response it triggers. In the Bengalese finch experiments, noise normally began **16–30 ms** after pitch measurement and overlapped the targeted syllable.

Adding **100 ms** moved the noise beyond the target syllable and prevented the adaptive pitch shift. The same animals could learn under the shorter delay, so the difference depended on when the consequence followed the vocal action.

**Temporal credit assignment** links an outcome to the action responsible for it. Rapid songs contain several nearby events that could receive credit. Immediate feedback preserved the relationship between the target’s acoustic variant and disruption; delayed feedback failed to select that variant effectively under this experimental arrangement.
''','The extra delay was applied after measuring the same pitch feature. The result concerns this targeted feedback task; it is not a universal upper bound on learning delays in all behaviors. Short delays allowed the noise to overlap the action being reinforced.')
add('Moving the threshold extends the learned pitch range',['tumer'],['t_large'],'''
A fixed feedback threshold eventually leaves most renditions in the escape region. **Incremental reinforcement** changes the criterion as behavior adapts, maintaining a difference in outcomes among the variants that the animal currently produces.

Tumer and Brainard progressively adjusted the pitch threshold across training days. The bird continued moving its target syllable beyond the range reached under the initial criterion, while the neighboring song structure remained recognizable.

Their original supplementary recording combines the reported pitch trajectory with sampled syllable sounds. The audible change accompanies the shift in measured fundamental frequency. Adaptive song control can therefore move an established vocal feature repeatedly when the feedback criterion tracks the learner’s changing performance.
''','The original Supplementary Video 1 contains syllables sampled from two baseline days and thirteen reinforcement days. The source’s blue line represents the experimental threshold. These are the authors’ recorded sounds and presentation, preserved without new plots or reconstructed audio.')
add('Song production and adaptation use linked pathways',['brown'],['b_anatomy'],'''
**HVC**, used as a proper name, is a song premotor nucleus whose activity precedes vocal production. It projects directly to the **robust nucleus of the arcopallium**, or **RA**, in the descending song motor pathway.

HVC also projects into the **anterior forebrain pathway**, a circuit running through the basal-ganglia nucleus **Area X**, the thalamic nucleus **DLM**, and the **lateral magnocellular nucleus of the anterior nidopallium**, or **LMAN**. LMAN returns output to RA.

The descending pathway supports production of learned vocal movements, while the anterior pathway contributes to song acquisition and adjustment. These routes converge on motor output while providing different contributions to performance. Learning can therefore alter a practiced song through a circuit linked to, but distinguishable from, its descending production pathway.
''','DLM is the dorsolateral nucleus of the medial thalamus. RA ultimately influences brainstem pathways controlling vocal behavior. HVC participates in both routes, whereas Area X, DLM, and LMAN form the indirect route through basal ganglia and thalamus.')
add('Dopamine reaches the vocal basal ganglia from VTA',['gadagkar'],['g_histology','g_anatomy'],'''
The **ventral tegmental area**, or **VTA**, is a midbrain region containing neurons that release **dopamine**, a transmitter involved in reinforcement-related signaling. A population of VTA neurons sends **axons**, signal-carrying neuronal processes, to Area X, placing a potential teaching signal within the vocal learning circuit.

Gadagkar and colleagues injected a **retrograde tracer** into Area X. This label travels back to the cell bodies of neurons projecting there. VTA cells carrying the tracer also expressed **tyrosine hydroxylase**, an enzyme used in dopamine synthesis.

The combined projection label and dopamine-related marker identified the anatomical route studied during singing. Recording along this route connected momentary vocal outcomes to the activity of neurons positioned to influence basal-ganglia learning, rather than assuming every neuron in the VTA served the same function.
''','More than 95% of Area X-projecting VTA cells were identified as dopaminergic in the anatomical literature cited by the study. The histology also preserves the electrode trajectory, connecting the recorded cells with the relevant anatomical population.')
add('Spike collision identifies a neuron’s projection',['gadagkar'],['g_anatomy','g_histology'],'''
**Antidromic stimulation** evokes an action potential that travels backward along an axon toward its cell body. Gadagkar and colleagues stimulated Area X while recording individual neurons in VTA to identify cells whose axons reached the vocal basal ganglia.

An evoked spike arrived with a consistent timing. When a spontaneous spike had just traveled outward along the same axon, the evoked spike disappeared in a **collision test**. Oppositely traveling spikes cannot pass through the recently activated axonal segment.

Projection identification made the physiological comparison specific. The Area X-projecting population strongly overlapped with cells carrying song-performance error responses, while most other recorded VTA neurons lacked those responses. Circuit membership therefore predicted the relevance of a neuron’s activity to vocal evaluation.
''','The collision test distinguishes stimulation of the recorded neuron’s own axon from an indirect synaptic response. The anatomical and physiological identification methods support complementary claims: where the neuron projects and what its activity encodes during singing.')
add('Distorted feedback briefly suppresses dopamine cells',['gadagkar'],['g_error','g_histology'],'''
**Distorted auditory feedback** alters the sound a bird hears while it sings. Gadagkar and colleagues randomly distorted a target syllable with a **50-ms** sound segment, while other renditions of that same syllable remained undistorted.

Area X-projecting VTA neurons reduced their firing after distortion. The response began about **58 ms** after distortion onset, lasted about **86 ms**, and reduced firing by roughly **75%** on average in the error-responsive population.

The response occurred after the altered auditory consequence rather than simply accompanying the motor act. A transient decrease in activity therefore carried information about a worse vocal outcome at a particular point in the sequence. Repeated comparisons between distorted and undistorted renditions isolated this outcome-related component of activity.
''','The neurons were recorded while the bird produced its own song. The distortion probability was arranged in advance, and distorted and undistorted renditions were interleaved. Response timing was aligned to the target feedback event, not to an arbitrary recording interval.')
add('An omitted distortion produces a positive error signal',['gadagkar'],['g_error','g_histology'],'''
An undistorted syllable can be better than expected when distortion has occurred on previous renditions. Gadagkar and colleagues found brief VTA firing increases at the precise song time when an anticipated distortion failed to occur.

These activations began about **51 ms** after the target time and lasted about **62 ms**. The error-responsive population increased firing by roughly **77%** relative to its pretarget activity, complementing the decreases following distorted feedback.

A **prediction error** is a difference between an outcome and an expectation. The same target syllable could yield a negative signal when distorted and a positive signal when it unexpectedly escaped distortion. Dopamine activity therefore represented vocal outcome relative to a learned benchmark, rather than merely registering the presence of sound.
''','The positive response was aligned to the time when distortion could have occurred, even though no new external stimulus arrived on that rendition. A temporally organized expectation is therefore needed to account for the omission response.')
add('Distortion history changes the value of an escape',['gadagkar'],['g_prob','g_histology'],'''
Gadagkar and colleagues targeted two syllables in the same song with different distortion probabilities, approximately **49%** for one and **20%** for the other. This created different expectations for the two moments within a single vocal sequence.

An undistorted rendition of the frequently distorted syllable produced a larger VTA activation than an undistorted rendition of the rarely distorted syllable. Average firing increases were about **67%** and **22%**, respectively, in the studied population.

The response to one target did not depend on whether the other target had just been distorted. Each syllable was evaluated against its own temporally aligned benchmark. Performance evaluation therefore used local experience within the sequence, allowing the same normal feedback to receive different values at different song times.
''','The distortion sound was not intrinsically a reward. The positive signal followed a normal outcome whose value depended on the probability of a worse outcome at that specific target time. The two-target comparison separates song-time expectation from a global good or bad song state.')
add('Performance evaluation depends on active singing',['gadagkar'],['g_passive','g_histology'],'''
The distorted and undistorted songs could also be played to a bird while it was silent. Under passive playback, the VTA cells that encoded performance errors during singing did not produce the same differential responses to those recordings.

This comparison separates an evaluation of the bird’s ongoing action from an ordinary response to hearing the disruptive sound. The auditory stimulus alone was insufficient to reproduce the singing-related firing pause or the positive omission response.

Active performance supplied the context in which the sound was evaluated. The bird’s own vocal sequence and its expected consequences jointly determined the dopamine response. Song reinforcement thus draws on information about an action being produced, rather than treating every external presentation of its acoustic consequence as equivalent.
''','Movement was also measured in the recording experiments, and the feedback manipulation did not account for the error response through an accompanying change in movement. The passive listening comparison changes the interpretation of the signal, so it belongs in the teaching content rather than as a routine disclaimer.')
add('Optical tools target VTA axons inside Area X',['xiao'],['x_anatomy'],'''
**Optogenetics** uses genetically expressed light-sensitive proteins to control selected neural elements. Xiao and colleagues expressed **channelrhodopsin**, or **ChR2**, for optical excitation and **archaerhodopsin**, or **ArchT**, for optical inhibition in VTA neurons.

**Axon terminals** are the projection’s release sites at its target. An axon-targeting sequence improved delivery of these proteins to terminals within Area X. Optical fibers positioned over Area X then illuminated the terminals, concentrating the intervention at the projection’s basal-ganglia endpoint rather than illuminating VTA cell bodies directly.

Fluorescent labeling verified expression in VTA neurons and their terminals. This anatomical targeting allowed the investigators to connect detected song variants to brief increases or decreases in projection activity. The intervention converted a naturally evaluative pathway into a controllable input for closed-loop vocal learning.
''','The axon-targeted constructs are named axChR2 and axArchT in the paper. ChR2 permits light-driven excitation, whereas ArchT permits light-driven inhibition. Their functional effects on dopamine release were measured independently before interpreting the behavioral reinforcement experiments.')
add('Optical excitation evokes measurable dopamine release',['xiao'],['x_release'],'''
**Fast-scan cyclic voltammetry** measures transmitter-related electrical currents while an electrode rapidly sweeps its voltage. Xiao and colleagues used this method in brain slices containing VTA connections to Area X to test the chemical effect of terminal illumination.

A **100-ms** pulse of **470-nm** blue light activated ChR2-expressing terminals and evoked a dopamine-related signal in Area X. Electrical stimulation provided a comparison with the characteristic electrochemical response of the same projection.

The optical intervention therefore changed transmitter release at the intended learning-circuit endpoint. This measurement connects the anatomical projection, its light-sensitive protein, and a chemical consequence. Subsequent behavioral experiments could then ask whether a transient release signal linked to a particular vocal variant altered future song production.
''','Voltammetry is a chemical readout rather than a count of action potentials. The source panel preserves the voltage sweep, current scale, and time axis. Optical excitation and electrical stimulation produced comparable dopamine signatures under the slice preparation.')
add('Optical inhibition reduces evoked dopamine release',['xiao'],['x_inhibit_release'],'''
To test terminal inhibition, Xiao and colleagues electrically stimulated VTA neurons while illuminating their ArchT-expressing axons in Area X. The preparation linked a known release-evoking input to an independently controlled inhibitory intervention at its terminals.

A **100-ms** pulse of **540-nm** light reduced the electrically evoked dopamine signal. The release response was smaller when illumination accompanied electrical stimulation than when the same stimulation occurred without optical inhibition.

This comparison establishes opposite chemical effects for the two optical tools: ChR2 excitation increased dopamine release, whereas ArchT inhibition reduced evoked release. The paired manipulations enabled causal tests of both signs of reinforcement, connecting transient changes at a neural projection with the direction of later behavioral adaptation.
''','The wavelength here is the 540-nm slice inhibition condition described in the study, rather than a universal ArchT wavelength. Behavioral optical inhibition used a related green-light condition. The release measurement verifies suppression under a controlled preparation.')
add('A neural interface couples pitch to terminal stimulation',['xiao'],['x_loop'],'''
Xiao and colleagues implanted optical fibers over Area X in adult male zebra finches expressing light-sensitive proteins in VTA terminals. The birds recovered their normal daily singing and produced repeated song motifs while a computer monitored a target syllable.

For excitation experiments, the computer selected naturally occurring variants in the lower or upper portion of the pitch distribution. Light began approximately **24 ms** after pitch measurement and continued for **100 ms**, overlapping the targeted syllable.

The interface linked acoustic measurement to a neural intervention with a defined projection, sign, and timing. Birds continued singing through the pulses. The resulting feedback could select future vocal variants without requiring a disruptive sound, providing a causal test of the teaching pathway itself.
''','This is a closed-loop neural stimulation experiment: acoustic sensing controls a neural input. It differs from a neural decoder, in which a recorded brain signal is used to infer behavior. The study combines freely produced behavior with projection-targeted stimulation.')
add('Positive reinforcement favors the stimulated variant',['xiao'],['x_positive','x_anatomy'],'''
**Positive reinforcement** increases actions associated with a favorable consequence. When VTA terminal excitation was delivered to syllable variants below **875 Hz**, the zebra finch’s target pitch decreased by **17.1 Hz** during the first stimulation day. Lower variants became more frequent as training proceeded.

The fraction of renditions receiving stimulation increased from **46% to 79%** in that representative experiment. Excitation therefore favored the vocal performances associated with the intervention, in contrast to disruptive noise, which drove avoidance of targeted performances.

Stimulating high-pitch variants instead shifted pitch upward. The same anatomical projection could reinforce either direction because the computer determined which variants received excitation. The learned change followed the contingency between the action and terminal activation, rather than a fixed motor command to raise or lower pitch.
''','The experiment measured pitch throughout the training day, not just during illuminated renditions. Animals receiving illumination without the excitatory protein did not acquire the same pitch shift. The optical effect therefore depended on functional expression and behavioral contingency.')
add('Negative reinforcement favors escape from inhibition',['xiao'],['x_negative','x_anatomy'],'''
**Negative reinforcement** favors actions that escape an unfavorable consequence. Optical inhibition of VTA terminals in Area X drove pitch away from the variants paired with reduced dopamine release. In a representative experiment, inhibition targeted syllable renditions below **595 Hz**, and pitch increased by **7.5 Hz** during the training day.

As the bird shifted upward, fewer renditions reached the inhibition threshold. Applying inhibition to high-pitch variants instead favored downward shifts. The behavioral direction was opposite to the effect of terminal excitation under the corresponding contingency.

Transient decreases and increases in the same projection could therefore provide complementary teaching signals. Excitation selected the associated variant; inhibition selected alternatives that escaped the intervention. Both manipulations adjusted an established vocal feature through repeated performances rather than requiring acquisition of an entirely new song.
''','The optical inhibition experiment provides a causal counterpart to the firing suppression observed after distorted feedback. The source’s individual pitch measurements and running averages preserve the trajectory of learning rather than only an endpoint comparison.')
add('The teaching signal changes later performances',['xiao'],['x_motor','x_anatomy'],'''
A direct motor command should alter the current syllable whenever stimulation occurs. Xiao and colleagues instead found that pitch changes accumulated over repeated performances and were not explained by an immediate systematic change on illuminated trials.

The target’s pitch, duration, and other measured acoustic properties remained comparable on stimulated and nearby unstimulated renditions during the acute comparisons. **Catch trials**, performances on which the usual intervention is withheld, allowed learned changes to be measured without concurrent illumination.

The pathway therefore biased future output through learning rather than simply forcing a pitch on each stimulated rendition. This distinction separates an evaluative input from a descending motor instruction. A brief neural consequence can reshape the distribution of later actions while leaving the immediately ongoing vocal gesture largely intact.
''','Catch trials are critical because they reveal what the bird produces without the intervention currently acting on it. The accumulated pitch shift is a behavioral memory of previous contingent feedback. The study also tested measures of motivation and movement to assess alternative explanations.')
add('Credit remains local unless vocal features covary',['xiao'],['x_precision','x_anatomy'],'''
Optical reinforcement largely changed the pitch of the target syllable while preserving other acoustic properties and neighboring syllables. The targeted elements were approximately **100 ms** long, and many nearby elements remained unchanged even when separated by only a short interval.

**Covariation** means that two measurements tend to change together across natural performances. Some neighboring syllables shifted when their baseline pitches covaried with the target’s pitch, even though the computer measured only the designated target.

Reinforcement can therefore select associated performance features as well as the explicitly measured feature. Temporal proximity alone did not determine spread; the relationship among vocal variants also mattered. Adaptive control retains local precision while remaining sensitive to coordinated variation already present in the bird’s song.
''','The paper compares target and control syllables and measures baseline correlations before interpreting the spread of learning. Covariation is a specific mechanistic reason to qualify strict syllable independence, rather than an automatic uncertainty statement attached to every experiment.')
add('Projection-targeted ablation reduces adaptive learning',['hisey'],['h_lesion'],'''
**Intersectional targeting** selects neurons by combining two biological criteria. Hisey and colleagues used viral expression in VTA together with a retrogradely delivered signal from Area X to activate a cell-ablation mechanism in the projecting population.

Before the ablation developed, birds learned to raise a target syllable’s pitch under contingent noise. Approximately a month later, after loss of VTA-to-Area X cells, the same animals exhibited reduced learning under the corresponding feedback task.

The manipulation preserved trial-to-trial pitch variation and recovery toward baseline after noise ended. These behaviors therefore have distinguishable dependencies: the projecting cells support normal reinforcement-driven adjustment, while production of residual variation and restoration of the baseline song can persist after partial loss of the teaching projection.
''','Ablation is irreversible loss of the targeted cells, unlike transient optical inhibition. Comparing early and later tests in the same bird ties the impairment to development of the manipulation. Histology connects the behavioral change to survival of the projecting population.')
add('D1 receptor signaling enables reinforcement-driven change',['hisey'],['h_d1'],'''
An **antagonist** blocks a receptor’s activation by its normal transmitter. Hisey and colleagues delivered the **D1-type dopamine receptor** antagonist **SCH23390** into Area X through microdialysis, a local drug-delivery method using a semipermeable probe.

With saline delivery, pitch-contingent noise drove adaptive pitch learning. During D1 blockade, the target syllable failed to acquire the usual shift despite continuing to exhibit trial-to-trial pitch variation. Learning returned when saline replaced the antagonist.

D1 blockade also reduced learning driven by optical activation of VTA terminals. The behavioral effect of this projection therefore depended on dopamine-sensitive receptors at its basal-ganglia endpoint. Receptor signaling links the transient teaching input to subsequent vocal adjustment, rather than treating projection activity alone as a sufficient account of the plasticity.
''','The reversible pharmacological manipulation separates learning from the ability to produce variable song. Microdialysis supplied the antagonist locally in Area X. The optical-plus-antagonist experiment also addresses the possibility that other transmitters released by VTA terminals explain the learning effect.')
add('D2 blockade changes practice more than learning per song',['hisey'],['h_d1'],'''
**D2-type dopamine receptors** provide another route for dopamine to influence Area X. Hisey and colleagues blocked these receptors with **sulpiride** and compared the resulting behavior with D1 blockade and saline conditions.

D2 blockade strongly reduced how much the birds sang, with an average reduction of about **66%** in the reported comparison. Its effects on total daily pitch learning were variable, while trial-to-trial pitch variability remained present.

When learning was considered relative to the number of target renditions, it was often preserved or enhanced. Daily change depends on both the learning supported by each performance and the amount of practice. D1 and D2 manipulations therefore separated receptor-dependent adaptation from dopamine-related regulation of how often the vocal behavior occurred.
''','A reduced daily learning total can follow fewer opportunities to practice even when learning per rendition remains intact. The source explicitly makes this behavioral distinction. D1 and D2 receptors can coexist in Area X neurons, so the results do not require assuming two completely separate receptor-exclusive cell populations.')
add('Juvenile copying uses the same dopamine pathway',['hisey'],['h_juvenile'],'''
Juvenile zebra finches learn a tutor’s song without the experimentally imposed noise used in adult pitch training. Hisey and colleagues tested whether this internally guided learning shared the VTA-to-Area X pathway required by the adult reinforcement task.

Projection-targeted ablation impaired tutor-song copying. Reversible D1 blockade in Area X during a **10-day** juvenile learning period also prevented the normal increase in similarity to the tutor while the antagonist was present.

After drug treatment ended, juveniles improved and ultimately approached the copying achieved by controls. The circuit is therefore required during ongoing acquisition rather than merely reflecting adult responses to external feedback. Internally guided imitation and externally reinforced adjustment recruit a common dopamine-sensitive learning pathway despite different sources of the desired outcome.
''','The D1 manipulation targeted the period around 50–60 days after hatching. The later improvement after washout distinguishes a temporary interruption of learning from permanent destruction of the memorized tutor model. Ablation and receptor blockade provide complementary cellular and pharmacological evidence.')
add('Two afferent pathways supply evaluative information',['kearney'],['k_map','k_transmitters'],'''
An **afferent** is an input projection arriving at a neural region. Kearney and colleagues examined two major inputs to VTA: the **ventral intermediate arcopallium**, or **Aiv**, and the **ventral pallidum**, or **VP**.

Aiv receives auditory-related information, while VP receives inputs that include the vocal basal ganglia. These connections place both regions upstream of the dopamine teaching signal, where information about performed song can influence evaluation.

The projections differed in transmitter-related molecular markers and in the direction of learning produced by contingent stimulation. Aiv input favored avoidance of associated variants; VP input favored their repetition. The VTA therefore integrates multiple evaluative routes rather than deriving both signs of reinforcement from an undifferentiated input.
''','Aiv and VP are anatomically distinct from the descending song motor pathway. The source’s original molecular panels locate the projecting cell populations. Their roles were tested through temporally specific interference and through contingent stimulation in the absence of auditory punishment.')
add('Aiv activity matters during the feedback window',['kearney'],['k_aiv_jam'],'''
Kearney and colleagues optically activated Aiv terminals in VTA on every rendition of a target syllable while noise remained contingent on pitch. This imposed similar terminal activity across performances that normally received different auditory outcomes.

Stimulation during the **50-ms auditory feedback window** strongly reduced the pitch learning driven by noise. Moving the intervention into the **50-ms premotor window** just before syllable onset preserved the learning response.

**Premotor** activity precedes and contributes to movement; evaluative activity processes its outcome. The timing comparison assigned Aiv input a feedback-related role. Variation in this projection during the auditory consequence was necessary for normal learning, whereas imposing comparable activation before the vocal action did not have the same effect.
''','The feedback-window intervention began approximately 10 ms after the expected noise onset. It was delivered on all target renditions, so it interfered with outcome-dependent variation rather than positively reinforcing only one pitch range. The same manipulation also had no acute systematic effect on syllable acoustics.')
add('VP interference also disrupts feedback evaluation',['kearney'],['k_vp_jam'],'''
The same timing strategy was applied to VP terminals in VTA. Noise still punished selected pitch variants, while optical stimulation imposed a common input on every detected rendition of the target syllable.

VP stimulation during the auditory feedback window reduced noise-driven learning. Stimulation during the earlier premotor window preserved the usual pitch adjustment. The intervention’s timing therefore mattered even though its anatomical target remained unchanged.

Both Aiv and VP inputs contributed to evaluation at the time of the vocal consequence. Their normal variation across renditions was needed for adaptive learning. These matched timing experiments separate the pathways’ evaluative function from an immediate command that simply changes how the current syllable is produced.
''','The VP experiment parallels the Aiv experiment but tests a separate afferent population. Neither manipulation should be interpreted as a lesion of the entire evaluator. Imposing a stereotyped input during feedback interferes with the information normally carried by that pathway.')
add('LMAN contributes before the vocal action',['kearney'],['k_lman'],'''
LMAN provides the cortical output of the anterior forebrain learning pathway and projects to RA and back into Area X. Kearney and colleagues used channelrhodopsin expression and optical fibers to interfere with its activity during defined song windows.

Optical activation evoked reliable high-frequency bursts, exceeding **400 spikes per second** in the validation recordings. During singing, stimulation in the premotor window prevented the usual pitch learning driven by contingent noise.

The same intervention in the auditory feedback window allowed normal learning. LMAN therefore contributed at a different time from Aiv and VP: before production rather than during evaluation. This temporal separation supports a circuit in which premotor variation and bias influence the action, while distinct afferents evaluate its acoustic consequence.
''','The physiological validation was performed in anesthetized birds, whereas the behavioral timing comparison was performed during singing. The LMAN histology and firing traces connect the optical intervention with the targeted nucleus. The pathway’s premotor role does not mean that it is the sole source of all song variability.')
add('Aiv stimulation makes associated variants less frequent',['kearney'],['k_aiv_learn','k_aiv_anatomy'],'''
Pitch-contingent stimulation can test whether an evaluative input supplies a teaching signal without disruptive sound. Kearney and colleagues delivered **50-ms**, **473-nm** light pulses to Aiv terminals in VTA when a target syllable crossed the chosen pitch threshold.

Over repeated training days, pitch shifted away from the stimulated range. Stimulating low variants favored higher pitches, whereas stimulating high variants favored lower pitches. Learned changes were measured on unstimulated catch renditions.

The effect resembled negative reinforcement by noise and remained largely restricted to the targeted syllable. Aiv terminal activity therefore supplied a consequence that selected avoidance of the associated performance. The result links a defined evaluative afferent to the sign of later behavioral change rather than only correlating its activity with an auditory error.
''','Illumination without functional channelrhodopsin did not drive the corresponding change. Catch renditions separate accumulated learning from acute optical effects. The histology verifies the projection from Aiv cells to VTA terminals in the same published study.')
add('VP stimulation makes associated variants more frequent',['kearney'],['k_vp_learn','k_vp_anatomy'],'''
When comparable optical pulses targeted VP terminals in VTA, learning proceeded in the opposite direction from Aiv stimulation. The zebra finches shifted target pitch toward the region associated with terminal activation.

Stimulation paired with low-pitch variants favored lower future pitches; stimulation paired with high-pitch variants favored higher pitches. The effect developed across training days and was assessed on catch renditions without concurrent light.

VP input therefore provided a positively reinforcing consequence under the tested conditions. The contrast with Aiv arose from stimulating different projections into the same midbrain region, not from changing the acoustic detector’s basic operation. Complementary evaluative pathways can assign opposite values to similar vocal variants and thereby guide adaptive control in either direction.
''','The investigators used histology to verify VP cells and their terminals in VTA. Acute stimulation did not account for the accumulated pitch shift through an immediate change in the vocal feature. The sign of reinforcement was established from the direction of learning toward or away from the selected variants.')
add('Aiv and VP have opposing effects on VTA neuron classes',['kearney'],['k_units'],'''
Kearney and colleagues recorded VTA neurons while stimulating Aiv or VP terminals. **Putative dopamine neurons** were identified physiologically by relatively broad action potentials and low spontaneous firing, commonly below **15 spikes per second**.

Aiv stimulation increased firing in many thin-spiking neurons while suppressing many broad-spiking cells. VP stimulation produced the reverse pattern, suppressing thin-spiking neurons while exciting the putative dopamine population.

An **interneuron** is a locally acting neuron that modifies activity within a circuit. These opposite responses connect the behavioral signs of reinforcement with distinct effects inside VTA. The physiological classification remains putative, but the combination of firing responses and molecular anatomy supports local inhibitory control as a route for converting afferent activity into bidirectional dopamine signaling.
''','The recording preparation was anesthetized, and cell identities were assigned from physiological properties rather than genetically tagging every recorded unit. The experiments establish opposing population tendencies. Anatomical transmitter markers provide independent support for the local circuit interpretation.')
add('Inhibition can invert the sign of an evaluative input',['kearney'],['k_transmitters','k_synapses'],'''
**Glutamatergic** neurons release glutamate, while **GABAergic** neurons release the inhibitory transmitter gamma-aminobutyric acid. Molecular labeling identified most VTA-projecting Aiv cells with a vesicular glutamate transporter and most VP cells with a vesicular GABA transporter.

Both afferents preferentially apposed VTA neurons expressing **parvalbumin**, a marker used here for inhibitory interneurons. Aiv’s excitatory input can recruit inhibition of dopamine cells; VP’s inhibitory input can suppress that local inhibition.

**Disinhibition** increases a neuron’s activity by reducing inhibition acting on it. The circuit hypothesis is that Aiv excites local inhibitory cells to reduce dopamine firing, whereas VP inhibits those cells to increase dopamine firing. This sign inversion accounts for the opposite physiological and behavioral effects of the two evaluative pathways.
''','VGLUT2 marks vesicular glutamate transport and VGAT marks vesicular GABA transport. Close apposition is an anatomical relationship, not a direct measurement of each synapse’s strength. The local sign-inverting circuit is explicitly a hypothesis supported by converging molecular, anatomical, and physiological findings.')
add('Population electrical signals carry song information',['brown'],['b_record'],'''
A **local field potential**, or **LFP**, is an extracellular voltage signal reflecting aggregate neural currents near a recording site. Brown and colleagues chronically implanted multisite probes targeting HVC and recorded the electrical signal together with the bird’s song.

The preparation measured freely produced vocal behavior and multiple neural channels at the same time. Song consisted of repeated motifs containing distinct syllables, allowing electrical activity to be aligned with both the larger sequence and individual acoustic events.

LFP features provide a population-level readout that differs from isolating a single neuron’s spikes. Their relationship to vocal timing can support neural decoding when individual units are difficult to maintain. The study tested what these signals predict about natural song, rather than assuming that any detectable rhythm is sufficient for an operating neural interface.
''','The recording location is described as presumptively HVC in the source because chronic localization has practical uncertainty. LFP is not equivalent to dopamine concentration or to the firing of one identified projection neuron. It summarizes electrical activity accessible to the implanted probe.')
add('Song changes the power of multiple frequency bands',['brown'],['b_power','b_anatomy'],'''
**Power** describes the strength of a signal’s frequency components. Brown and colleagues analyzed HVC-targeted LFP activity during vocalization and nearby silent periods to identify changes associated with production of song.

Power increased in frequencies above roughly **50 Hz** before and during singing. Lower-frequency components also exhibited structured rhythmic changes, including a prominent **25–35 Hz** pattern and additional organization in **4–8 Hz** and **8–12 Hz** bands.

High-frequency power declined shortly after the bout ended, linking it to the period of vocal activity. Several frequency ranges therefore carried behavior-related information on different time scales. Neural decoding can use these distinct features, rather than treating the entire population signal as a single undifferentiated measure of activation.
''','A song bout can contain several repeated motifs. Electrical frequency is distinct from the much higher acoustic frequencies of the syllables. The source uses electrical spectrograms to characterize neural rhythms and acoustic spectrograms to characterize the emitted song.')
add('Oscillation phase aligns to individual syllable timing',['brown'],['b_phase','b_anatomy'],'''
**Phase** specifies the position within an oscillatory cycle, while power specifies its strength. Brown and colleagues compared LFP phase at the onset of repeated syllables to determine whether population rhythms carried precise timing information.

Individual syllables had characteristic phase preferences in several frequency bands. Aligning the signal to actual syllable onsets produced stronger consistency than aligning it only to the average expected time within the motif.

The neural rhythm therefore tracked local vocal events rather than merely running as a fixed clock from the beginning of the song. This event-related alignment can help a decoder distinguish when a particular syllable is about to occur, even when the timing of the larger sequence varies across performances.
''','The same song can vary in tempo or in the timing of particular syllables. Comparing actual and average syllable onset times tests whether phase organization follows the local action. The published polar distributions and time-frequency panels retain the source’s frequency and timing scales.')
add('Phase and power provide complementary identity signals',['brown'],['b_identity','b_anatomy'],'''
**Neural decoding** estimates a behavioral variable from recorded brain activity. Brown and colleagues trained classifiers using LFP segments that ended before syllable onset, testing whether neural features predicted the identity of the upcoming vocal element.

They separated phase-related and power-related information to assess their contributions. Each feature type supported classification above the behavioral chance benchmark, and combining them generally improved performance as information from additional channels was included.

Different signal properties therefore supplied complementary information about intended vocal output. The classifier learned a relationship between measured neural patterns and labeled actions rather than generating song by itself. The analysis established an information source for interfaces, while its training and testing remained an offline decoding experiment.
''','The analysis used a linear discriminant classifier, an algorithm that assigns observations to categories from weighted features. Causal filtering and pre-onset feature windows reduce the possibility of classifying a syllable merely by incorporating signals recorded after it has already begun.')
add('Premotor features predict the onset of a syllable',['brown'],['b_onset','b_anatomy'],'''
Predicting which syllable will occur differs from predicting when it begins. Brown and colleagues used neural feature templates to estimate the onset of each syllable within the naturally performed song sequence.

The features came from causally filtered signals recorded before the acoustic onset. Prediction was compared with a behavioral timing benchmark based on the average onset of that syllable relative to the first syllable of the motif.

Neural predictions followed rendition-specific timing rather than relying entirely on the stereotyped sequence. This distinction matters for an adaptive interface because a fixed song clock can miss natural timing changes. A measured premotor signal can supply event-specific timing information even when the order of most syllables is predictable.
''','A causal filter uses present and earlier signal samples rather than future samples. The study’s neural prediction analysis remained offline; it did not itself demonstrate a deployed feedback controller. The comparison with a behavioral timing model tests the added information in the neural recordings.')
add('Branch-point decoding distinguishes singing from stopping',['brown'],['b_branch','b_anatomy'],'''
Some zebra finch performances omitted a syllable or ended a bout before the usual sequence finished. These natural branch points tested whether neural decoding merely reproduced an average song order or reflected the action actually selected.

Brown and colleagues compared neural prediction confidence when a syllable was produced, skipped, or replaced by termination of the bout. The neural features distinguished these alternatives, including situations where a timing-only model expected a syllable that never occurred.

An interface based solely on stereotyped sequence timing would confuse an omitted action with a delayed one. Population activity instead carried information about the selected continuation. Adaptive control can therefore benefit from signals related to both action identity and action timing when behavior departs from its most common sequence.
''','The published examples preserve the recorded waveform, spectrogram, and neural prediction traces for performed, skipped, and terminated sequences. These branch-point comparisons are stronger evidence of behavioral information than predicting a perfectly fixed series of events.')
add('Acoustic decoding enables sequence-contingent feedback',['kawaji'],['q_decoder'],'''
Kawaji and colleagues developed **SAIBS**, a simultaneous automatic interpreter for birdsongs, to identify syllable sequences from ongoing audio. The system learned categories from each bird’s recorded song and used a **convolutional neural network**, a classifier that extracts local patterns from input data.

Annotation computation took about **6 ms** after syllable detection. The measured interval from song completion to feedback presentation was about **109 ms**, allowing consequences to depend on the contents of a completed song.

SAIBS is an acoustic decoder, not a neural recording device. It complements projection-targeted stimulation by providing a richer behavioral measurement for closed-loop experiments. The system could count repeated syllables and recognize sequences, extending adaptive feedback beyond a single pitch threshold within one vocal element.
''','The authors clustered syllable spectra before training the classifier, reducing the need for manual annotation. The software’s processing time and the complete feedback latency are different quantities. Total system latency includes detection and presentation beyond the classifier’s computation.')
add('Social video reinforcement increases syllable repetition',['kawaji'],['q_social'],'''
**Operant conditioning** changes behavior through consequences contingent on an action. Kawaji and colleagues counted repetitions of a target syllable in Bengalese finch song and presented an original conspecific video when the count crossed a selected threshold.

**Conspecific** means an individual of the same species. The social stimulus elicited approaches, singing, and feather erection in preliminary observations. Under repetition-contingent presentation, birds increased the occurrence of songs containing enough repetitions to meet the criterion.

Comparable nonsocial visual feedback failed to produce the same increase. The reinforcing effect therefore depended on the social content rather than merely the arrival of a visual event. Closed-loop feedback can select a sequence property through a behaviorally meaningful consequence, broadening adaptive song control beyond punishment by noise.
''','The embedded Supplementary Movie 1 is the original conspecific stimulus, not a recording of the subject’s behavioral response. The source distinguishes this social video from the nonsocial control in Supplementary Movie 2. The published figure retains the repetition criterion and measured change as a static fallback.')
add('A learned visual context changes song without new reward',['kawaji'],['q_context'],'''
Bengalese finches alternated between days when sufficient target repetition produced a social video and days when it produced no reward. Repetition increased under the reward condition and declined under the no-reward condition.

Kawaji and colleagues associated those rules with different frame colors on the monitor. In subsequent tests, the birds altered repetition according to the trained color even when the video reward was withheld in both conditions.

The change emerged within **10 minutes** after the visual context switched. A **context cue** identifies which learned rule currently applies. The birds therefore used a learned external cue to adjust song structure, rather than requiring a fresh reward after every performance to maintain the condition-dependent difference.
''','Green and yellow were the colors of the source’s experimental monitor frames, not deck design colors. The unrewarded test probes the learned association between context and rule. Faster and slower alternation schedules in the source test how quickly the bird can change repetition after a context switch.')
add('Area X supports flexible use of the learned sequence',['kawaji'],['q_area_x'],'''
Kawaji and colleagues tested the contribution of Area X after Bengalese finches had learned repetition-contingent reward rules. **Ablation** removed the targeted nucleus using an excitotoxic intervention, and histology verified the affected region.

After Area X ablation, target repetition decreased toward the preconditioning level. Further reward and no-reward training failed to restore the normal condition-dependent difference, while much of the existing syllable transition structure remained recognizable.

The basal-ganglia contribution therefore extended from adjustment of syllable pitch to flexible use of song sequences. Established vocal structure and context-sensitive adaptation had different dependencies. Together with the dopamine experiments, the result places reinforcement-sensitive song control within circuits that link evaluation to the selection of future vocal actions.
''','The lesion effect concerns flexibility in the tested repetition task rather than elimination of all song production. The source’s anatomical panel includes Area X within the anterior forebrain pathway. Preserved transition structure makes the loss of context-dependent modulation a specific behavioral result.')
assert len(S)==44,len(S)
for i,s in enumerate(S,2):
 n=len(re.findall(r'\b\S+\b',' '.join(s['body'])));assert 90<=n<=170,(i,n,s['title'])
tk={'cite':'Tumer & Brainard (2007); Gadagkar et al. (2016); Hisey et al. (2018); Kearney et al. (2019); Brown et al. (2021); Kawaji et al. (2024)','items':[
 {'lead':'Closed-loop contingencies','text':'Select particular vocal variants by linking measured performance to an immediate consequence.'},
 {'lead':'Performance prediction errors','text':'VTA-to-Area X neurons decrease firing after distortion and increase it after an unexpectedly undistorted syllable.'},
 {'lead':'Dopamine-dependent learning','text':'Contingent excitation and inhibition drive opposite pitch changes; D1 signaling in Area X supports adult adjustment and juvenile copying.'},
 {'lead':'Distinct circuit timing','text':'Aiv and VP contribute during feedback evaluation, whereas LMAN contributes during the premotor window.'},
 {'lead':'Neural decoding','text':'LFP phase and power predict syllable identity and timing; offline prediction must be distinguished from a tested real-time controller.'},
 {'lead':'Flexible sequence control','text':'Social reinforcement and learned context cues alter repetition, while Area X supports the adaptation of song to those conditions.'}
 ],'transcript':['Closed-loop feedback operates on natural performance variation. The meaning and timing of the intervention determine which variants become more frequent.','Dopamine cells carry both positive and negative performance-related responses. Projection stimulation and receptor blockade connect these signals causally with learning.','The evaluator and premotor components act in distinct song windows. Neural decoding supplies information about upcoming behavior, while sequence-contingent reinforcement can change flexible vocal organization.'],'refs':[v['reference'] for v in R.values()]}
spec={'lecture':81,'content_slides':44,'theme':'muted-carmine-paper','title_height':2.6,'title_min_pt':25,'title_image':fig('x_photo'),'title_refs':[R['xiao']['reference']],'slides':S,'takeaways':tk}
(B/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
(B/'PLAN.md').write_text('# Lecture 81: final content plan\n\n'+ '\n'.join(f'{i}. {s["title"]} ({s["cite"]})' for i,s in enumerate(S,1))+'\n')
print('Wrote 44 content slides with source figures and teaching transcripts')
