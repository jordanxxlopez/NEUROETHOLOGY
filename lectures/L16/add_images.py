#!/usr/bin/env python3
"""Add article figures to the Lecture 16 spec without changing any slide text.

Crops panels from open-access article figures (papers/<Paper>/, gitignored) into figures/,
then edits lecture.json: text-only slides gain a figure, many single-figure slides gain a
second one (figures-right), and the title slide gets the study animal. Titles, body text
and transcripts are untouched; the new paper is added to the slide's refs and footer cite.
Idempotent: re-running rebuilds the same spec from the slide titles.
"""
import json
from pathlib import Path
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent
P = ROOT / 'papers'

REFS = {
    'B25': ('Babl et al. (2025)', 'Babl SS, Kiai A, García-Rosales F, Hechavarría JC (2025). Neuronal activity underlying vocal production in bats. Annals of the New York Academy of Sciences 1550(1):37–54. https://doi.org/10.1111/nyas.15410', '10.1111/nyas.15410'),
    'H22b': ('Hase et al. (2022)', 'Hase K, Kadoya Y, Takeuchi Y, Kobayasi KI, Hiryu S (2022). Echo reception in group flight by Japanese horseshoe bats, Rhinolophus ferrumequinum nippon. Royal Society Open Science 9(2):211597. https://doi.org/10.1098/rsos.211597', '10.1098/rsos.211597'),
    'L22': ('Luo et al. (2022)', 'Luo J, Lu M, Wang X, Wang H, Moss CF (2022). Doppler shift compensation performance in Hipposideros pratti across experimental paradigms. Frontiers in Systems Neuroscience 16:920703. https://doi.org/10.3389/fnsys.2022.920703', '10.3389/fnsys.2022.920703'),
    'M26': ('Matsumoto et al. (2026)', 'Matsumoto H, Yoshida S, Hiryu S (2026). Greater Japanese horseshoe bats (Rhinolophus nippon) gradually converge their echolocation call frequency to colony members. Journal of Comparative Physiology A 212(5):835–844. https://doi.org/10.1007/s00359-026-01821-5', '10.1007/s00359-026-01821-5'),
    'H18': ('Schoeppler et al. (2018)', 'Schoeppler D, Schnitzler H-U, Denzinger A (2018). Precise Doppler shift compensation in the hipposiderid bat, Hipposideros armiger. Scientific Reports 8:4598. https://doi.org/10.1038/s41598-018-22880-y', '10.1038/s41598-018-22880-y'),
    'H22': ('Schoeppler et al. (2022)', 'Schoeppler D, Denzinger A, Schnitzler H-U (2022). The resting frequency of echolocation signals changes with body temperature in the hipposiderid bat Hipposideros armiger. Journal of Experimental Biology 225(3):jeb243569. https://doi.org/10.1242/jeb.243569', '10.1242/jeb.243569'),
    'S23': ('Schoeppler et al. (2023)', 'Schoeppler D, Kost K, Schnitzler H-U, Denzinger A (2023). Transmitter and receiver of the low frequency horseshoe bat Rhinolophus paradoxolophus are functionally matched for fluttering target detection. Journal of Comparative Physiology A 209(1):191–202. https://doi.org/10.1007/s00359-022-01571-0', '10.1007/s00359-022-01571-0'),
    'W22': ('Wang et al. (2022)', 'Wang H, Zhou Y, Li H, Moss CF, Li X, Luo J (2022). Sensory error drives fine motor adjustment. Proceedings of the National Academy of Sciences USA 119(27):e2201275119. https://doi.org/10.1073/pnas.2201275119', '10.1073/pnas.2201275119'),
    'WX25': ('Wang et al. (2025)', 'Wang X, Bao M, Wang H, Sun R, Dai W, Sun K, Zhu Y, Pu Y, Chu Y, Li X, Wang T, Zhang M, Lin A, Li J, Feng J (2025). Cochlear cell atlas of two laryngeal echolocating bats—new evidence for the adaptive nervous physiology in constant frequency bat. Molecular Ecology Resources 25(6):e14101. https://doi.org/10.1111/1755-0998.14101', '10.1111/1755-0998.14101'),
    'WA18': ('Washington et al. (2018)', 'Washington SD, Hamaide J, Jeurissen B, van Steenkiste G, Huysmans T, Sijbers J, Deleye S, Kanwal JS, De Groof G, Liang S, Van Audekerke J, Wenstrup JJ, Van der Linden A, Radtke-Schuller S, Verhoye M (2018). A three-dimensional digital neurological atlas of the mustached bat (Pteronotus parnellii). NeuroImage 183:300–313. https://doi.org/10.1016/j.neuroimage.2018.08.013', '10.1016/j.neuroimage.2018.08.013'),
    'Y26': ('Yoshida et al. (2026)', 'Yoshida S, Matsumoto H, Kobayasi KI, Hiryu S (2026). Horseshoe bats (Rhinolophus nippon) suppress clutter noise through echolocation frequency control to detect prey. Communications Biology 9:663. https://doi.org/10.1038/s42003-026-10217-9', '10.1038/s42003-026-10217-9'),
}

# name: (source image, (left, top, right, bottom) as fractions of the source)
CROPS = {
    'title_rhinolophus': ('web/rhinolophus_ferrumequinum_maiorano.jpeg', (0.0, 0.0, 1.0, 0.85)),
    'y26_fig3b': ('Yoshida2026/42003_2026_10217_Fig3_full.png', (0.0, 0.43, 1.0, 1.0)),
    'y26_fig2b': ('Yoshida2026/42003_2026_10217_Fig2_full.png', (0.0, 0.58, 1.0, 1.0)),
    'y26_fig1b': ('Yoshida2026/42003_2026_10217_Fig1_full.png', (0.49, 0.0, 1.0, 1.0)),
    'babl25_fig1a': ('Babl2025/NYAS-1550-37-g001.jpg', (0.0, 0.0, 0.25, 0.36)),
    'babl25_fig4ad': ('Babl2025/NYAS-1550-37-g005.jpg', (0.0, 0.0, 1.0, 0.51)),
    'wangx25_fig1e': ('WangX2025/MEN-25-e14101-g005.jpg', (0.49, 0.785, 1.0, 1.0)),
    'wangx25_fig1b': ('WangX2025/MEN-25-e14101-g005.jpg', (0.0, 0.145, 0.5, 0.415)),
    'wash18_fig9b': ('Washington2018/nihms-1528373-f0010.jpg', (0.365, 0.245, 0.585, 0.64)),
    'wash18_fig9c': ('Washington2018/nihms-1528373-f0010.jpg', (0.60, 0.0, 1.0, 0.57)),
    'wash18_fig9de': ('Washington2018/nihms-1528373-f0010.jpg', (0.0, 0.62, 1.0, 1.0)),
    'wash18_fig8a': ('Washington2018/nihms-1528373-f0009.jpg', (0.0, 0.0, 0.52, 0.505)),
    'luo22_fig5a': ('Luo2022/g005_large.jpg', (0.0, 0.0, 0.48, 0.29)),
    'luo22_fig2': ('Luo2022/g002_large.jpg', (0.0, 0.0, 1.0, 1.0)),
    'luo22_fig4': ('Luo2022/g004_large.jpg', (0.0, 0.0, 1.0, 1.0)),
    'wang22_fig2ac': ('Wang2022/pnas.2201275119fig02.jpg', (0.0, 0.0, 0.708, 0.715)),
    'wang22_fig2df': ('Wang2022/pnas.2201275119fig02.jpg', (0.712, 0.0, 1.0, 0.705)),
    'wang22_fig2gi': ('Wang2022/pnas.2201275119fig02.jpg', (0.0, 0.718, 1.0, 1.0)),
    'wang22_fig3ae': ('Wang2022/pnas.2201275119fig03.jpg', (0.0, 0.0, 1.0, 0.49)),
    'wang22_fig3fl': ('Wang2022/pnas.2201275119fig03.jpg', (0.0, 0.49, 1.0, 1.0)),
    's23_fig2a': ('Schoeppler2023/359_2022_1571_Fig2_full.png', (0.0, 0.0, 1.0, 0.385)),
    's23_fig2bc': ('Schoeppler2023/359_2022_1571_Fig2_full.png', (0.0, 0.40, 1.0, 1.0)),
    's23_fig3': ('Schoeppler2023/359_2022_1571_Fig3_full.png', (0.0, 0.0, 1.0, 1.0)),
    's23_fig5': ('Schoeppler2023/359_2022_1571_Fig5_full.png', (0.0, 0.0, 1.0, 1.0)),
    'matsu26_fig1a': ('Matsumoto2026/359_2026_1821_Fig1_HTML.png', (0.0, 0.0, 0.88, 0.43)),
    'matsu26_fig2ab': ('Matsumoto2026/359_2026_1821_Fig2_HTML.png', (0.0, 0.0, 0.80, 0.345)),
    's23_fig1a': ('Schoeppler2023/359_2022_1571_Fig1_full.png', (0.0, 0.0, 1.0, 0.51)),
    's23_fig1b': ('Schoeppler2023/359_2022_1571_Fig1_full.png', (0.0, 0.515, 0.335, 1.0)),
    'luo22_fig6a': ('Luo2022/fnsys-16-920703-g006.jpg', (0.0, 0.0, 0.82, 0.245)),
    'hase22_fig4': ('Hase2022/rsos211597f04.jpg', (0.0, 0.0, 1.0, 1.0)),
    'h18_fig5': ('Schoeppler2018/41598_2018_22880_Fig5_HTML.jpg', (0.0, 0.0, 1.0, 1.0)),
    'h22_fig1': ('Schoeppler2022/jexbio-225-243569-g1.jpg', (0.0, 0.0, 1.0, 1.0)),
    'h22_fig4': ('Schoeppler2022/jexbio-225-243569-g4.jpg', (0.0, 0.0, 1.0, 1.0)),
}


def trim(im, pad=6):
    bg = Image.new('RGB', im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg).convert('L').point(lambda v: 255 if v > 18 else 0)
    box = diff.getbbox()
    if not box:
        return im
    l, t, r, b = box
    return im.crop((max(0, l - pad), max(0, t - pad), min(im.width, r + pad), min(im.height, b + pad)))


def crop_all():
    out = ROOT / 'figures'
    for name, (src, (l, t, r, b)) in CROPS.items():
        im = Image.open(P / src).convert('RGB')
        w, h = im.size
        im = trim(im.crop((round(l * w), round(t * h), round(r * w), round(b * h))))
        im.thumbnail((1800, 1800))  # proportional downscale only; pixels otherwise unchanged
        im.save(out / f'{name}.png')


def fig(name, key, num, text):
    return {'kind': 'article', 'path': f'figures/{name}.png',
            'caption': f'{REFS[key][0]}, Fig. {num}. {text}', 'source_url': 'https://doi.org/' + REFS[key][2]}


TITLE_IMAGE = {'kind': 'web', 'path': 'figures/title_rhinolophus.png',
               'caption': 'Photo: greater horseshoe bats (Rhinolophus ferrumequinum) roosting in a cave in winter; Raffaele Maiorano, CC0 1.0 (Wikimedia Commons).',
               'credit': 'Raffaele Maiorano (iNaturalist)', 'license': 'CC0 1.0',
               'source_url': 'https://commons.wikimedia.org/wiki/File:Rhinolophus_ferrumequinum_110412929.jpg'}

# slide title -> list of (key, figure) added to that slide
ADD = {
    'CF-FM calls combine a sustained tone and a short sweep': [
        ('B25', fig('babl25_fig1a', 'B25', '1A', 'Pteronotus parnellii echolocation call: oscillogram and spectrogram with CF and FM parts.'))],
    'Flutter changes the echoes carried by the CF component': [
        ('Y26', fig('y26_fig3b', 'Y26', '3B', 'On-board recording near a tethered moth; wingbeat glints appear above the call band.')),
        ('S23', fig('s23_fig1a', 'S23', '1a', 'Rhinolophus paradoxolophus call sequence from take-off to landing.'))],
    'Frequency compensation has a finite operating range': [
        ('L22', fig('luo22_fig6a', 'L22', '6A', 'Maximum Doppler compensation per bat in free flight and on a pendulum; 100% is full.'))],
    'Terminal FM suppresses cochlear offset transients': [
        ('S23', fig('s23_fig1b', 'S23', '1b', 'R. paradoxolophus call with initial FM, CF and terminal FM, with power spectrum.'))],
    'Approaching a reflector raises returning echo frequency': [
        ('S23', fig('s23_fig2a', 'S23', '2a', 'Rhinolophus paradoxolophus: CF2 falls after take-off and recovers at landing.')),
        ('L22', fig('luo22_fig5a', 'L22', '5A', 'Hipposideros pratti in flight: emitted (blue) and echo (green) frequency.'))],
    'Resting frequency is an individual calling baseline': [
        ('M26', fig('matsu26_fig1a', 'M26', '1a', 'CF2 calls of a stationary greater Japanese horseshoe bat.'))],
    'Shifted playback causes subsequent calls to fall in pitch': [
        ('W22', fig('wang22_fig2ac', 'W22', '2A–C', 'Hipposideros armiger calls under 0, −50 and +50 cent feedback shifts.'))],
    'Compensated echoes sit slightly above resting frequency': [
        ('S23', fig('s23_fig2bc', 'S23', '2b–d', 'Resting CF2 before take-off; emitted and echo frequency and flight speed in flight.'))],
    'Early playback tests found little response to lower echoes': [
        ('W22', fig('wang22_fig3fl', 'W22', '3F–L', 'Call-frequency change across shift sizes from −150 to +150 cents.'))],
    'Equal sound levels need not produce equal audibility': [
        ('S23', fig('s23_fig5', 'S23', '5', 'Behavioural audiogram of R. paradoxolophus; the arrow marks the threshold minimum.'))],
    'Audible lower-frequency echoes raise emitted frequency': [
        ('L22', fig('luo22_fig4', 'L22', '4', 'Hanging H. pratti under 0, +700 and −700 Hz feedback: rate, level, duration, frequency.'))],
    'Upward vocal corrections are smaller than downward ones': [
        ('W22', fig('wang22_fig2gi', 'W22', '2G–I', 'Relative call-frequency change for 0, −50 and +50 cent shifts.')),
        ('W22', fig('wang22_fig3ae', 'W22', '3A–E', 'Frequency adjustment of two bats across small upward and downward shifts.'))],
    'Removing an imposed shift reverses the vocal correction': [
        ('W22', fig('wang22_fig2df', 'W22', '2D–F', 'CF of 10 calls before, 20 during and 10 after perturbation; feedback in blue.'))],
    'Louder feedback accelerates correction in both directions': [
        ('Y26', fig('y26_fig1b', 'Y26', '1B', 'Phantom echoes (red) and calls (blue) under constant, periodic and multiple shifts.'))],
    'The larynx converts auditory correction into call frequency': [
        ('B25', fig('babl25_fig4ad', 'B25', '4A–D', 'Rousettus frontal cortex: recording site, Nissl section and vocalization-locked firing.'))],
    'Opposed feedback actions can stabilize a vocal set point': [
        ('H22b', fig('hase22_fig4', 'H22b', '4', 'Group flight: a bat’s own echo CF2 stays near its reference while others’ calls vary.'))],
    'Cochlear recordings separate receptor and neural signals': [
        ('WX25', fig('wangx25_fig1e', 'WX25', '1E', 'H&E sections of the cochlea of R. ferrumequinum (top) and Myotis pilosus.'))],
    'Peripheral neurons can discharge when a tone ends': [
        ('WX25', fig('wangx25_fig1b', 'WX25', '1B', 'Cochlear cell types of R. ferrumequinum from single-nucleus RNA-seq, incl. SGN1 and SGN2.'))],
    'The cortex devotes extensive space to the CF echo band': [
        ('WA18', fig('wash18_fig9b', 'WA18', '9B', 'Mustached-bat auditory cortex map; DSCF area (black) with iso-frequency contours in kHz.'))],
    'Columns share frequency and amplitude preferences': [
        ('WA18', fig('wash18_fig8a', 'WA18', '8A', 'Nissl and myelin-stained coronal sections of the mustached-bat brain.'))],
    'Amplitude and frequency occupy cortical coordinates': [
        ('WA18', fig('wash18_fig9c', 'WA18', '9C', 'Auditory cortical fields of Pteronotus on the 3D MRI brain, dorsal view.'))],
    'Cortical activity represents a spectrum across populations': [
        ('WA18', fig('wash18_fig9de', 'WA18', '9D–E', 'DSCF, FM-FM and CF/CF fields on the 3D brain, left and right lateral views.'))],
    'Free flight lowers emission while preserving echo frequency': [
        ('Y26', fig('y26_fig2b', 'Y26', '2B', 'On-board microphone: calls lowered in frequency, echoes held near a fixed band.'))],
    'Approach changes call timing while CF is retained': [
        ('L22', fig('luo22_fig2', 'L22', '2', 'H. pratti flight to a platform: position, speed, call rate, level, duration, frequency.'))],
    'Resting and reference frequencies shift together': [
        ('H18', fig('h18_fig5', 'H18', '5', 'Resting versus reference frequency for 20 flights per bat.'))],
    'Precision within a flight differs from stability across days': [
        ('S23', fig('s23_fig3', 'S23', '3', 'R. paradoxolophus: resting and reference frequencies over 3 weeks.'))],
    'Resting call frequency rises as torpid bats warm': [
        ('H22', fig('h22_fig1', 'H22', '1', 'Relative skin temperature of two bats over 34 h; lines mark experimenter entry.'))],
    'Frequency can peak before measured skin temperature': [
        ('H22', fig('h22_fig4', 'H22', '4', 'Skin-temperature rise against prior calling activity and resting-frequency rise.'))],
    'A changing sensory band can coexist with precise feedback': [
        ('M26', fig('matsu26_fig2ab', 'M26', '2a–b', 'CF2 of captured (red) and resident (black) bats over 30 days.'))],
}


def split_height(figs, width, total=4.3):
    """Share the column's image height between two figures in proportion to their shapes."""
    nat = []
    for f in figs:
        w, h = Image.open(ROOT / f['path']).size
        nat.append(width * h / w)
    first = nat[0] + max(0.0, total - sum(nat)) / 2 if sum(nat) <= total else total * nat[0] / sum(nat)
    return round(min(max(first, 1.3), total - 1.3), 2)


def apply():
    spec_path = ROOT / 'lecture.json'
    spec = json.loads(spec_path.read_text())
    spec['title_image'] = TITLE_IMAGE
    seen = set()
    for s in spec['slides']:
        extra = ADD.get(s['title'])
        if not extra:
            continue
        seen.add(s['title'])
        figs = [s['figure']] if s.get('figure') else []
        figs = [f for f in figs if f['path'] not in {e[1]['path'] for e in extra}]
        figs += [e[1] for e in extra]
        for key, _ in extra:
            if REFS[key][1] not in s['refs']:
                s['refs'].append(REFS[key][1])
            if REFS[key][0] not in s['cite']:
                s['cite'] += '; ' + REFS[key][0]
        s.pop('figure', None)
        s.pop('figures', None)
        if len(figs) == 1:
            s.update(layout='figure-right', figure_width=5.2, figure=figs[0])
        else:
            assert len(figs) == 2, s['title']
            s.update(layout='figures-right', figure_width=5.2, figures=figs,
                     primary_figure_height=split_height(figs, 5.2))
    missing = set(ADD) - seen
    if missing:
        raise SystemExit(f'slide titles not found: {sorted(missing)}')
    spec_path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    crop_all()
    apply()
