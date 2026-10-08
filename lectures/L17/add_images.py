#!/usr/bin/env python3
"""Add article figures to the Lecture 17 spec without changing any slide text.

Crops panels from open-access article figures (papers/<Paper>/, gitignored) into figures/,
then edits lecture.json: text-only slides gain a figure and many single-figure slides gain a
second one (figures-right). Titles, body text and transcripts are untouched; the new paper is
added to the slide's refs and footer cite. Idempotent.
"""
import json
from pathlib import Path
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent
P = ROOT / 'papers'

REFS = {
    'BZ22': ('Beetz & Hechavarría (2022)', 'Beetz MJ, Hechavarría JC (2022). Neural processing of naturalistic echolocation signals in bats. Frontiers in Neural Circuits 16:899370. https://doi.org/10.3389/fncir.2022.899370', '10.3389/fncir.2022.899370'),
    'BZ26': ('Beetz et al. (2026)', 'Beetz MJ, Kössl M, Hechavarría JC (2026). First come, first served: neuronal processing of multi-echo streams in the auditory cortex of echolocating bats. Journal of Experimental Biology 229(10):jeb252069. https://doi.org/10.1242/jeb.252069', '10.1242/jeb.252069'),
    'C26': ('Cadigan et al. (2026)', 'Cadigan SC, Smith NA, Jones TK, Wohlgemuth MJ (2026). Unpredictable prey motion shapes behavior across time scales. Journal of Experimental Biology 229(15):jeb250896. https://doi.org/10.1242/jeb.250896', '10.1242/jeb.250896'),
    'GF17': ('Greiter & Firzlaff (2017)', 'Greiter W, Firzlaff U (2017). Representation of three-dimensional space in the auditory cortex of the echolocating bat P. discolor. PLoS ONE 12(8):e0182461. https://doi.org/10.1371/journal.pone.0182461', '10.1371/journal.pone.0182461'),
    'G26': ('Grinnell (2026)', 'Grinnell AD (2026). Reflections on the neural processing of echoes for distance information in echolocating bats. Journal of Comparative Physiology A 212(5):913–926. https://doi.org/10.1007/s00359-026-01804-6', '10.1007/s00359-026-01804-6'),
    'MA25': ('Ma et al. (2025)', 'Ma N, Xia H, Zheng H, Luo J (2025). Prey evasiveness and masking noise jointly promote the ultrahigh call rate in echolocating bats. BMC Biology 23:323. https://doi.org/10.1186/s12915-025-02435-0', '10.1186/s12915-025-02435-0'),
    'MC22': ('Macías et al. (2022)', 'Macías S, Bakshi K, Smotherman M (2022). Faster repetition rate sharpens the cortical representation of echo streams in echolocating bats. eNeuro 9(1):ENEURO.0410-21.2021. https://doi.org/10.1523/ENEURO.0410-21.2021', '10.1523/ENEURO.0410-21.2021'),
    'M20': ('Ming et al. (2020)', 'Ming C, Bates ME, Simmons JA (2020). How frequency hopping suppresses pulse-echo ambiguity in bat biosonar. Proceedings of the National Academy of Sciences 117(29):17288–17295. https://doi.org/10.1073/pnas.2001105117', '10.1073/pnas.2001105117'),
    'SS26': ('Simmons & Simmons (2026)', 'Simmons JA, Simmons AM (2026). Beamforming as a mechanism for azimuthal localization of targets by FM-echolocating big brown bats. Journal of Comparative Physiology A 212(5):901–911. https://doi.org/10.1007/s00359-026-01834-0', '10.1007/s00359-026-01834-0'),
    'T24': ('Teshima et al. (2024)', 'Teshima Y, Mogi M, Nishida H, Tsuchiya T, Kobayasi KI, Hiryu S (2024). Discrimination of object information by bat echolocation deciphered from acoustic simulations. Royal Society Open Science 11(1):231415. https://doi.org/10.1098/rsos.231415', '10.1098/rsos.231415'),
}

CROPS = {
    'bz22_fig1': ('Beetz2022/g001_large.jpg', (0.0, 0.0, 1.0, 1.0)),
    'bz22_fig3': ('Beetz2022/fncir-16-899370-g003.jpg', (0.0, 0.265, 0.97, 0.97)),
    'bz22_fig5a': ('Beetz2022/fncir-16-899370-g005.jpg', (0.0, 0.0, 0.62, 0.75)),
    'bz26_fig1b': ('Beetz2026/jexbio-229-252069-g1.jpg', (0.44, 0.0, 1.0, 0.23)),
    'bz26_fig2ab': ('Beetz2026/jexbio-229-252069-g2.jpg', (0.0, 0.0, 1.0, 0.635)),
    'bz26_fig3': ('Beetz2026/jexbio-229-252069-g3.jpg', (0.0, 0.0, 1.0, 1.0)),
    'bz26_fig5': ('Beetz2026/jexbio-229-252069-g5.jpg', (0.0, 0.0, 1.0, 1.0)),
    'bz26_fig6ag': ('Beetz2026/jexbio-229-252069-g6.jpg', (0.0, 0.0, 1.0, 0.51)),
    'c26_fig3': ('Cadigan2026/jexbio-229-250896-g3.jpg', (0.0, 0.0, 1.0, 1.0)),
    'gf17_fig2ab': ('Greiter2017/pone.0182461.g002.jpg', (0.0, 0.0, 0.6, 1.0)),
    'g26_fig5': ('Grinnell2026/359_2026_1804_Fig5_HTML.png', (0.0, 0.0, 1.0, 1.0)),
    'g26_fig9': ('Grinnell2026/359_2026_1804_Fig9_HTML.png', (0.0, 0.0, 1.0, 1.0)),
    'ma25_fig1af': ('Ma2025/12915_2025_2435_Fig1_HTML.jpg', (0.0, 0.0, 1.0, 0.565)),
    'ma25_fig2bc': ('Ma2025/12915_2025_2435_Fig2_HTML.jpg', (0.0, 0.218, 1.0, 0.532)),
    'mc22_fig3ab': ('Macias2022/ENEURO.0410-21.2021_f003.jpg', (0.0, 0.0, 1.0, 0.51)),
    'm20_fig1c': ('Ming2020/pnas.2001105117fig01.jpg', (0.645, 0.0, 0.99, 1.0)),
    'm20_fig4': ('Ming2020/pnas.2001105117fig04.jpg', (0.0, 0.0, 1.0, 1.0)),
    'ss26_fig1': ('SimmonsBeam2026/359_2026_1834_Fig1_full.png', (0.0, 0.0, 1.0, 1.0)),
    'ss26_fig2a': ('SimmonsBeam2026/359_2026_1834_Fig2_full.png', (0.0, 0.0, 0.49, 1.0)),
    'ss26_fig4': ('SimmonsBeam2026/359_2026_1834_Fig4_full.png', (0.0, 0.0, 1.0, 1.0)),
    't24_fig2b': ('Teshima2024/rsos231415f02.jpg', (0.0, 0.535, 1.0, 1.0)),
    't24_fig3ab': ('Teshima2024/rsos231415f03.jpg', (0.0, 0.0, 0.59, 1.0)),
}

def fig(name, key, num, text):
    return {'kind': 'article', 'path': f'figures/{name}.png',
            'caption': f'{REFS[key][0]}, Fig. {num}. {text}', 'source_url': 'https://doi.org/' + REFS[key][2]}


TITLE_IMAGE = None  # the existing title image (Moss et al. 2006, Fig. 1) is kept

ADD = {
    'FM calls distribute acoustic energy across frequencies': [
        ('BZ22', fig('bz22_fig1', 'BZ22', '1', 'Spectrograms of an FM call (Carollia perspicillata) and a CF-FM call (Pteronotus parnellii).'))],
    'Echo delay specifies the round trip to a target': [
        ('BZ26', fig('bz26_fig1b', 'BZ26', '1B', 'Pulse followed by echoes from objects at different distances; oscillograms and spectrograms.'))],
    'Bats can choose the nearer of two reflecting targets': [
        ('T24', fig('t24_fig3ab', 'T24', '3a–b', 'Flight trajectories of bats approaching two targets in a two-choice test.'))],
    'Range discrimination occurs across sonar signal types': [
        ('G26', fig('g26_fig9', 'G26', '9', 'Approach responses of big brown bats to artificial echoes built from pure-tone steps.'))],
    'Electronic echoes isolate arrival time from other cues': [
        ('GF17', fig('gf17_fig2ab', 'GF17', '2A–B', 'Delay-response fields of two cortical units in Phyllostomus discolor; spike count in color.'))],
    'Echo arrival time can support the range judgment': [
        ('BZ26', fig('bz26_fig2ab', 'BZ26', '2A–B', 'Echo delay over an approach sequence and color-coded cortical multi-unit rasters.'))],
    'A matched receiver is a functional hypothesis': [
        ('M20', fig('m20_fig4', 'M20', '4', 'Spectrograms, cross-correlations and SCAT neural spectrograms for successive echoes.'))],
    'Timing is registered early in the auditory pathway': [
        ('BZ22', fig('bz22_fig5a', 'BZ22', '5A', 'Inferior colliculus and cortex responses to call–echo pairs, color-coded by echo delay.'))],
    'Echo cascades approximate a scene with several objects': [
        ('BZ26', fig('bz26_fig3', 'BZ26', '3', 'Cortical responses to echo cascades from three objects and object preference indices.'))],
    'Population potentials register calls and echoes': [
        ('BZ22', fig('bz22_fig3', 'BZ22', '3', 'Carollia auditory cortex activity across an approach sequence, caudal to rostral.'))],
    'First-echo responses follow the changing delay': [
        ('BZ26', fig('bz26_fig6ag', 'BZ26', '6A–G', 'Cortical units respond mainly to the first echo of a cascade at differing echo levels.'))],
    'Later echoes have more variable population responses': [
        ('BZ26', fig('bz26_fig5', 'BZ26', '5', 'Response to the leading echo against suppression of the lagging echo.'))],
    'Measured brainstem precision leaves a perceptual gap': [
        ('MC22', fig('mc22_fig3ab', 'MC22', '3A–B', 'Tadarida cortical neuron: tuning and spike rasters to pulse–echo trains at 10–15 Hz.'))],
    'Local and inherited selectivity can coexist': [
        ('SS26', fig('ss26_fig4', 'SS26', '4', 'Interaural-level inflection points of 56 big brown bat IC neurons by best frequency.'))],
    'The two harmonics have different beam widths': [
        ('SS26', fig('ss26_fig1', 'SS26', '1', 'Big brown bat head, FM1/FM2 call, flight corridor, and transmit and receive beams.'))],
    'A two-glint echo provides a structured target': [
        ('T24', fig('t24_fig2b', 'T24', '2b', 'Echo impulse responses and FM echoes from five targets; surface (S) and occlusion (O) parts.'))],
    'Similar echo delays can create masking blind spots': [
        ('G26', fig('g26_fig5', 'G26', '5', 'Interference by artificial CF-FM echoes as a function of CF–FM onset interval.'))],
    'Harmonic timing links acuity and clutter rejection': [
        ('M20', fig('m20_fig1c', 'M20', '1C', 'Delay jitter acuity after high-pass or low-pass removal of FM1 or FM2 frequencies.'))],
    'Nearby vegetation reduces prey-capture success': [
        ('MA25', fig('ma25_fig1af', 'MA25', '1A–F', 'Hipposideros pratti foraging: call rate and terminal buzz for different prey states.'))],
    'Flight paths change target–clutter separation': [
        ('SS26', fig('ss26_fig2a', 'SS26', '2a', 'Acoustic-camera view of echoes from a corridor of hanging chains.'))],
    'Sonar strobe groups control repeated scene sampling': [
        ('C26', fig('c26_fig3', 'C26', '3', 'Call intervals and sonar sound groups for predictable and unpredictable target motion.'))],
    'The terminal buzz shortens near vegetation': [
        ('MA25', fig('ma25_fig2bc', 'MA25', '2B–C', 'Pulse intervals and spectrograms in silence and noise; buzz percentage by noise level.'))],
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
    if TITLE_IMAGE:
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
