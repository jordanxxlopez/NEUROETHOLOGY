from pathlib import Path
import json,subprocess
B=Path('lectures/L100');p=B/'lecture.json';s=json.loads(p.read_text());a=json.loads((B/'assets.json').read_text())
# Keep the separate histology figures intact and identify them individually.
subprocess.run(['python','tools/crop_figure.py',str(B/'papers'/'rspb20121357.pdf'),'4','--box','0.100','0.067','0.442','0.680','-o',str(B/'figures'/'vampire_2.png')],check=True,stdout=subprocess.DEVNULL)
a['vampire'][1]['caption']='Hoving & Robison (2012), Fig. 2. Arm structures, cirri and mucus-producing cells.'
(B/'assets.json').write_text(json.dumps(a,indent=2)+'\n')
s['slides'][23]['figure']=a['vampire'][1];s['slides'][22]['figure']=a['vampire'][2]
s['slides'][32]['figure']=a['worm'][3]
s['slides'][25]['body'][0]='The hydrothermal vent shrimp _Rimicaris hybisae_ has an enlarged dorsal eye beneath its carapace rather than ordinary image-forming eyestalk optics. Nagata and colleagues examined this sensory anatomy and identified six opsins, connecting photoreceptor organization to a molecular repertoire operating without sunlight.'
s['slides'][25]['body'][2]='Microvilli are small membrane projections that provide space for photopigments. Microscopy revealed organized microvillar arrays in the dorsal photoreceptors. The receptor repertoire includes visual opsins and Opn5, while experiments with expressed proteins distinguish light reception, cellular signaling, and chromophore regeneration among the six molecules.'
s['slides'][26]['figure']=a['vent'][3]
s['slides'][26]['body'][1]='The measured pigments respond in the visible range near 457–517 nm. Their different spectral sensitivities connect individual receptor identities to the wavelengths capable of initiating a response, matching molecular light detection to the blue-green signals present around hydrothermal vents.'
s['slides'][27]['body'][1]='RhPeropsin absorbed most strongly near 495 nm and bound all-trans-retinal. Illumination above 500 nm increased production of 11-cis-retinal. These are different molecular configurations of retinal, and conversion between them supplies a route for producing the chromophore used by other photopigments.'
s['slides'][27]['body'][2]='A **photoisomerase** uses light to convert a molecule between configurations. RhPeropsin performed this chromophore-converting function, whereas the other five identified opsins showed light-dependent G-protein activity. The repertoire therefore includes molecular support for pigment regeneration as well as receptors that initiate cellular signaling.'
s['slides'][28]['figure']=a['vent'][1]
s['slides'][28]['body'][1]='The Opn5 receptor formed a blue-light-sensitive pigment and engaged inhibitory G-protein signaling. A **G protein** couples an activated receptor to intracellular effectors. Cells expressing this receptor showed a light-dependent decrease in cyclic AMP, a molecule that carries intracellular signals.'
s['slides'][28]['body'][2]='Cells without an introduced opsin provided a comparison for the light-dependent measurements. The researchers also measured intracellular calcium responses to examine another signaling route. These preparations connect pigment activation to biochemical changes within cells, rather than treating photon absorption as the endpoint of sensory reception.'
full='Musilova Z, Cortesi F, Matschiner M, Davies WIL, Patel JS, Stieb SM, de Busserolles F, Malmstrøm M, Tørresen OK, Brown CJ, Mountford JK, Hanel R, Stenkamp DL, Jakobsen KS, Carleton KL, Jentoft S, Marshall J, Salzburger W (2019). Vision using multiple distinct rod opsins in deep-sea fishes. Science 364:588–592. https://doi.org/10.1126/science.aav4632'
for slide in s['slides']:
 slide['refs']=[full if '10.1126/science.aav4632'in r else r for r in slide['refs']];slide['transcript']=[x.replace('**','').replace('_','')for x in slide['body']]
s['takeaways']['refs']=[full if '10.1126/science.aav4632'in r else r for r in s['takeaways']['refs']]
p.write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n')
# Store corrections separately, so the original authoring and source changes are reviewable.
(B/'refine_spec.py').write_text(Path(__file__).read_text())
