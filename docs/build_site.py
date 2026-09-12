#!/usr/bin/env python3
"""Build the He Lab static pages. Uses only Python's standard library.
Edit the page content here and publications in site-data.json, then run this file.
"""
from pathlib import Path
import json
from hashlib import sha256
from html import escape as esc

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'site-data.json').read_text())
EMAIL = 'yichunhe@illinois.edu'
NAV = [('about.html', 'Research'), ('publications.html', 'Publications'), ('resources.html', 'Resources'), ('team.html', 'Team'), ('join.html', 'Join us')]

def asset_url(path):
    return f'{path}?v={sha256((ROOT / path).read_bytes()).hexdigest()[:10]}'

def page(file, title, description, body, home=False):
    links = ''.join(f'<a href="{u}"'+(' aria-current="page"' if file==u else '')+f'>{n}</a>' for u,n in NAV)
    out = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | He Lab</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#ffffff">
<meta property="og:title" content="{esc(title)} | He Lab"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website">
<link rel="icon" href="{asset_url('images/he-lab-brain-favicon.png')}" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{asset_url('lab.css')}"><script src="{asset_url('lab.js')}" defer></script></head>
<body class="{'home' if home else 'inner-page'}"><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><nav class="nav-inner wrap" aria-label="Main navigation">
<a class="brand" href="index.html" aria-label="He Lab home"><img src="{asset_url('images/he-lab-brain-compact.png')}" alt="" width="44" height="44"><span>He Lab</span></a>
<div class="desktop-nav">{links}</div><button id="hamburger" aria-controls="mobile-nav" aria-expanded="false" aria-label="Open menu"><span></span><span></span></button>
</nav><nav id="mobile-nav" class="mobile-nav" aria-label="Mobile navigation" hidden>{links}</nav></header>
<main id="main">{body}</main>
<footer class="site-footer wrap"><div class="footer-title">He Lab · AI for Biology and Human Intelligence</div>
<p>Siebel School of Computing and Data Science <br>University of Illinois Urbana-Champaign · Planned launch in 2027</p>
<div class="footer-links"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="https://scholar.google.com/citations?user=LMnJmvIAAAAJ&amp;hl=en">Google Scholar</a><a href="https://github.com/yichunher">GitHub</a><a href="news.html">News</a></div></footer></body></html>'''
    (ROOT / file).write_text(out)

ARROW='<span aria-hidden="true">↗</span>'
def link(url,text,cl='text-link'): return f'<a class="{cl}" href="{url}">{text} {ARROW}</a>'
def intro(kicker,title,desc):
    title={'OUR RESEARCH':'Research','PEOPLE':'Team','JOIN HE LAB':'Join us','PUBLICATIONS':'Publications','TOOLS & DATA':'Resources','NEWS & UPDATES':'News'}[kicker]
    return f'<section class="page-intro wrap"><h1>{title}</h1><p class="page-deck">{desc}</p></section>'

DIRECTIONS=[
 ('01','cross-organ','Biological function and disease','How do genes and cells shape biological function in health and disease?', 'We connect genes, cells, and tissues to understand how biological systems function and how molecular changes lead to disease.', 'Spatial & multimodal AI · Perturbation biology','images/research-cross-organ-modern-v5.webp'),
 ('02','brain','The biological basis of intelligence','How do molecular programs and neural circuits give rise to cognition and intelligence?', 'We connect genes, cells, and brain circuits to understand how cognition and social behavior emerge, using multimodal AI across species and disease.', 'Multimodal brain models · Cognition & behavior','images/research-brain-multimodal-profile-v18.webp'),
 ('03','discovery','AI for scientific discovery','How can AI expand our ability to understand biology and intelligence?', 'We build AI partners that help people connect evidence, uncover biological mechanisms, and expand their capabilities for scientific discovery.', 'Scientific agents · Human–AI reasoning','images/research-discovery-revealed-world-v12.webp')
]
FIGURE_ALTS = {
 'cross-organ': 'Pale blue and coral scientific illustration connects a DNA helix and molecular interactions with an organized cellular sheet.',
 'brain': 'A textured human profile combines molecular puncta inside cells, cellular neighborhoods, curved circuit connections, and three schematic electrical traces, linking biological identity, organization, and dynamics to cognition.',
 'discovery': 'A colorful natural-history-inspired painting of light revealing intricate microscopic forms, a metaphor for expanding biological understanding.'
}
ART_CREDITS = {
 'brain': 'Cells, connectivity, and neural dynamics · Concept artwork',
 'discovery': 'Revealing hidden biological structure · Concept illustration'
}
research_cards=''.join(f'''<a href="about.html#{slug}" class="direction"><img class="direction-art" src="{im}" width="840" height="840" alt="{FIGURE_ALTS[slug]}"><h3>{title}</h3><p>{desc}</p></a>''' for n,slug,title,q,desc,tag,im in DIRECTIONS)

def research_framework(prefix):
    return f'''<figure class="research-framework" aria-labelledby="{prefix}-framework-title">
<figcaption><h2 id="{prefix}-framework-title">From biological change to human function</h2><p>Our research connects mechanisms across scales. AI helps turn these connections into predictions that can be tested and refined.</p></figcaption>
<div class="framework-diagram">
<div class="framework-goal"><p class="framework-label">ONE SHARED GOAL</p><h3>Understand and improve human function</h3><p>Human health · Cognition · Human capabilities</p></div>
<svg class="framework-goal-links" viewBox="0 0 1000 58" preserveAspectRatio="none" aria-hidden="true"><defs><marker id="{prefix}-goal-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L7 4 L0 8" fill="none" stroke="#777" stroke-width="1.2"/></marker></defs><path d="M245 57 V31 H755 V57 M500 31 V3" fill="none" stroke="#999" stroke-width="1.2" vector-effect="non-scaling-stroke" marker-end="url(#{prefix}-goal-arrow)"/></svg>
<div class="framework-science"><div class="framework-domain"><p class="framework-label">01 · BIOLOGY</p><h3>Genes to function</h3><p>Genes · Cells<br>Tissues · Organs</p><p class="framework-domain-focus">Function &amp; disease</p></div>
<span class="framework-exchange" aria-label="Connected through shared biological mechanisms">⇄</span>
<div class="framework-domain"><p class="framework-label">02 · INTELLIGENCE</p><h3>Brain to cognition</h3><p>Brain activity<br>Behavior · Cognition</p><p class="framework-domain-focus">Intelligence in health &amp; disease</p></div></div>
<p class="framework-shared">Shared molecular and cellular mechanisms</p>
<svg class="framework-model-links" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><defs><marker id="{prefix}-model-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto-start-reverse"><path d="M0 0 L7 4 L0 8" fill="none" stroke="#777" stroke-width="1.2"/></marker></defs><g fill="none" stroke="#999" stroke-width="1.2" marker-start="url(#{prefix}-model-arrow)" marker-end="url(#{prefix}-model-arrow)"><path d="M245 3 V43" vector-effect="non-scaling-stroke"/><path d="M755 3 V43" vector-effect="non-scaling-stroke"/></g></svg>
<div class="framework-ai"><p class="framework-label">03 · AI FOR SCIENTIFIC DISCOVERY</p><h3>A shared discovery and validation cycle</h3><div class="framework-cycle" aria-label="Measure, model, predict, test, and repeat"><span>Measure</span><span aria-hidden="true">→</span><span>Model</span><span aria-hidden="true">→</span><span>Predict</span><span aria-hidden="true">→</span><span>Test</span><span aria-hidden="true">↺</span></div><p>Models guide experiments; new evidence refines the models.</p></div>
</div></figure>'''

SELECTED=[('594872','A shared molecular model of the brain'),('646459','AI agents for spatial biology'),('s41586-023-06569','Mapping the mouse central nervous system at molecular resolution'),('s41467-023-37477','Connecting multimodal views of cells'),('618046','Tracking neural activity over time'),('s41467-021-26044','Identifying cells and tissue structure from spatial gene expression')]
selected=''
for key,desc in SELECTED:
    p=next(p for p in DATA['publications'] if key in p['url'])
    selected+=f'''<a class="progress-row" href="{p['url']}"><img src="{p['image']}" alt="" loading="lazy"><div><h3>{esc(p['title'])}</h3><p>{desc}</p><span class="progress-venue">{p['venue']}</span></div></a>'''

home=f'''
<section class="home-intro wrap"><h1>AI for Biology and Human Intelligence</h1>
<p class="home-subtitle">The He Lab at the <a href="https://illinois.edu/">University of Illinois Urbana-Champaign</a></p>
<p class="home-affiliation">Siebel School of Computing and Data Science · Planned launch in 2027</p></section>
<section class="home-research wrap" id="research"><h2>Research</h2>
<div class="research-intro"><p>We develop AI to understand how biological changes shape human health and intelligence, and to guide ways of improving both.</p><p>Our research connects molecular and cellular mechanisms to organ function, brain dynamics, and cognition through models whose predictions can be tested experimentally.</p></div>
<div class="directions">{research_cards}</div>
<p class="research-approach">These directions form one research program: understand biological mechanisms, connect them to human function, and use AI to guide discovery and experimental testing. {link('about.html','More about our research')}</p>
{research_framework('home')}</section>
<section class="home-progress wrap" id="research-progress"><h2>Research progress</h2><p class="section-intro">Selected work by Yichun He and collaborators that forms the foundation for our future research.</p><div class="progress-list">{selected}</div>{link('publications.html','View all publications','button')}</section>
<section class="home-join wrap"><h2>Join us</h2><p>We welcome students, researchers, and partners who share our curiosity about biology and the potential of AI to benefit people. Help shape the lab as we prepare to launch at Illinois in 2027.</p>{link('join.html','Learn about joining the lab','button')}</section>'''
page('index.html','AI for Biology and Human Intelligence','AI for biological function and disease, the biological basis of human intelligence, and scientific discovery.',home,True)

research=intro('OUR RESEARCH','Research','One question connects our work: how do changes in biological systems shape human health and intelligence, and how can we predict and improve their consequences? We study this across scales, from genes and cells to organs, neural activity, and cognition.')
research+=f'<div class="wrap">{research_framework("research")}</div>'
longs=[
 ('Understanding biological function.', 'How a gene acts depends on the cell, tissue, and organism in which it operates. We aim to uncover how genetic variation, gene regulation, and spatial organization work together to produce biological function, and how disruptions lead to disease. Cross-organ comparisons provide a starting point for identifying shared mechanisms and context-dependent responses.', 'We build spatial and multimodal foundation models to connect molecular measurements with cellular states and tissue function. By integrating perturbation data with causal modeling, we seek to predict the functional consequences of genetic and regulatory changes. Our initial focus on mechanisms linking brain and metabolic disease connects this work directly to our research on brain function and cognition. Experimental collaborations help test and refine these predictions.', 'Initial directions', 'Gene-to-function modeling; cross-organ spatial models; perturbation-response prediction.'),
 ('Understanding the biological basis of intelligence.', 'Brains combine molecular diversity, spatial organization, and dynamic neural activity. We ask how these biological features work together across scales to support learning, cognition, and social behavior. Comparing brains across species and disease helps us identify shared principles and differences relevant to human intelligence.', 'Building on our work in spatial brain atlases, multimodal learning, and long-term neural decoding, we develop models that integrate molecular profiles, spatial maps, and neural recordings. We seek to connect cell identity and location with circuit dynamics and behavior, and to generate predictions that experimental collaborators can test. Our long-term aim is to inform approaches that preserve and improve human cognitive function.', 'Initial directions', 'Multimodal brain models; cell-to-circuit relationships; cognition and social behavior across species and disease.'),
 ('Expanding human scientific capabilities.', 'Scientific AI is the shared discovery framework for our work in biology and intelligence. We build agents that bring together molecular data, brain atlases, analysis tools, and literature to help researchers formulate hypotheses, identify informative perturbations, and design experiments.', 'Building on SpatialAgent and FuseMapAgent, we aim to connect measurement, modeling, prediction, and experimental testing in an iterative process. Evidence from both scientific directions can improve shared models, while the models help choose what to investigate next. Our goal is to extend human scientific capabilities while keeping reasoning traceable and predictions testable.', 'Initial directions', 'Scientific agents; hypothesis generation and experimental design; human–AI reasoning.')]
brain_model_path='''<figure class="brain-model-path" aria-labelledby="brain-model-title">
<figcaption id="brain-model-title">From multimodal measurements to models of intelligence</figcaption>
<ul class="brain-modalities"><li><strong>Molecular identity</strong><span>Genes &amp; cell types</span></li><li><strong>Spatial organization</strong><span>Cells within tissue</span></li><li><strong>Neural activity</strong><span>Dynamics over time</span></li></ul>
<svg class="brain-model-merge" viewBox="0 0 600 35" preserveAspectRatio="none" aria-hidden="true"><path d="M100 1 V15 H500 V1 M300 1 V32 M295 27 L300 32 L305 27" fill="none" stroke="currentColor" stroke-width="1" vector-effect="non-scaling-stroke"/></svg>
<div class="brain-model-method"><strong>Multimodal brain models</strong><span>Connect cell identity, location, and dynamics</span></div>
<div class="brain-model-arrow" aria-hidden="true">↓</div>
<p class="brain-model-outcomes">Circuit function · Cognition · Social behavior</p>
<p class="brain-model-context">Compare across species and disease. Test predictions with experimental collaborators.</p>
</figure>'''
for d,l in zip(DIRECTIONS,longs):
 n,slug,title,q,desc,tag,im=d; head,p1,p2,label,projects=l
 credit=f'<p class="detail-credit">{ART_CREDITS[slug]}</p>' if slug in ART_CREDITS else ""
 model_path=brain_model_path if slug=='brain' else ''
 research+=f'<section class="research-detail wrap" id="{slug}"><div class="detail-aside"><img src="{im}" alt="{FIGURE_ALTS[slug]}" loading="lazy"/>{credit}<p class="detail-tag">{tag}</p></div><div class="detail-body"><h2>{title}</h2><h3>{q}</h3><p>{p1}</p><p>{p2}</p>{model_path}<div class="research-focus"><span class="eyebrow">{label}</span><p>{projects}</p></div></div></section>'
research+='''<section id="approach" class="mission-band"><div class="wrap mission-grid"><div><h2>Our approach</h2><p>Today, we focus on AI and computational methods, working closely with experimental collaborators to define questions and test predictions. Over time, we plan to establish our own experimental platform, bringing models and measurements into closer conversation.</p><p>We choose methods in service of the question. We value predictions that can be tested, tools others can use, and research whose benefits extend beyond a single dataset.</p></div></div></section>'''
research+=f'<section class="wrap simple-cta"><h2>Join our research</h2>{link("join.html","Join the conversation","button primary")}</section>'
page('about.html','Research','Understanding biological function and disease, the biological basis of intelligence, and AI as a partner in scientific discovery.',research)

team=intro('PEOPLE','A lab is built <br><em>around people.</em>','We are building an interdisciplinary research group united by curiosity about living systems and the potential of AI to improve human lives.')
team+=f'''<section class="wrap founder"><div class="founder-photo"><img src="images/YichunHe.jpg" alt="Yichun He"><span class="eyebrow">PRINCIPAL INVESTIGATOR</span></div><div><p class="eyebrow">MEET THE PI</p><h2>Yichun He</h2><p class="founder-role">Eric and Wendy Schmidt Center Fellow <br>Broad Institute of MIT and Harvard</p><p>Yichun develops AI methods to connect molecular, spatial, and functional views of cells. Her work spans spatial atlases, multimodal learning, neural decoding, and AI agents for biological discovery.</p><p>She earned her PhD in Engineering Sciences at Harvard University, advised by Xiao Wang, and her bachelor's degree in Electrical Engineering at the University of Science and Technology of China. At the Broad Institute, she works with Caroline Uhler on causal and multimodal approaches to biology.</p><p>She plans to launch He Lab at the Siebel School of Computing and Data Science, University of Illinois Urbana-Champaign, in 2027.</p><div class="profile-links">{link('https://scholar.google.com/citations?user=LMnJmvIAAAAJ&hl=en','Google Scholar')}{link('https://yichunher.github.io/','Personal website')}{link('mailto:'+EMAIL,'Email')}</div></div></section>
<section class="wrap section"><div class="section-heading"><div><h2>Lab culture and mentorship</h2></div><p>Our aim is an environment where people can develop technical depth, learn across disciplines, and grow into independent scientists.</p></div><div class="principles"><div><span class="eyebrow">01</span><h3>Learn across boundaries</h3><p>Bring depth in one field and curiosity about another. Shared biological questions help us build a common language.</p></div><div><span class="eyebrow">02</span><h3>Think independently</h3><p>We value careful reasoning, honest discussion of uncertainty, and the willingness to change direction when evidence calls for it.</p></div><div><span class="eyebrow">03</span><h3>Make room for people</h3><p>Good science grows through supportive mentorship, different perspectives, and opportunities to contribute meaningfully.</p></div></div>{link('join.html','Help shape the lab','button primary')}</section>'''
page('team.html','People','Meet Yichun He and the research community we are building.',team)

join=intro('JOIN HE LAB','The next chapter <br><em>could include you.</em>','We welcome conversations with prospective students, researchers, and collaborators as we prepare to launch at Illinois in 2027.')
join+=f'''<section class="wrap join-layout"><aside><h2>Research opportunities</h2><p>Our initial focus is computational research in partnership with experimental groups.</p><a href="mailto:{EMAIL}" class="contact-address">{EMAIL} ↗</a></aside><div class="opportunities">
<article><span class="eyebrow">01 / GRADUATE STUDENTS</span><h3>Develop a research direction of your own.</h3><p>We are interested in people with backgrounds in machine learning, computer science, statistics, computational biology, or related fields. Biological curiosity matters alongside technical strength.</p><p>Write with a brief introduction, your research interests, and a CV. Graduate admission follows the relevant university program's application process.</p>{link('https://siebelschool.illinois.edu/academics/graduate','Explore Illinois graduate programs')}</article>
<article><span class="eyebrow">02 / POSTDOCTORAL RESEARCHERS</span><h3>Connect your expertise to a new question.</h3><p>We welcome discussions about potential projects in spatial and causal AI, multimodal biological modeling, and scientific agents. Please share your CV, representative work, and a short description of the questions you want to pursue.</p><p>Project fit, timing, and available opportunities can be discussed directly.</p></article>
<article><span class="eyebrow">03 / UNDERGRADUATE &amp; VISITING RESEARCHERS</span><h3>Start with curiosity. Bring something you have made.</h3><p>Tell us about your interests, relevant coursework or experience, and availability. A project, analysis, or piece of code can help us understand how you think.</p></article></div></section>
<section class="mission-band"><div class="wrap mission-grid"><div><h2>Collaborate with us</h2><p>We welcome conversations with experimental researchers, clinicians, industry partners, and supporters interested in AI for biological discovery and human health. Shared questions, complementary expertise, and resources can make ambitious research possible.</p>{link('mailto:'+EMAIL,'Discuss a collaboration')}</div></div></section>'''
page('join.html','Join us','Explore research opportunities and collaborations with He Lab, launching at Illinois in 2027.',join)

pubs=intro('PUBLICATIONS','The work behind <br><em>the questions.</em>','Selected publications and preprints by Yichun He and collaborators, including work completed before the launch of He Lab.')
pubs+='<section class="wrap publication-list"><p class="pub-key"># Equal contribution · * Corresponding author</p>'
for year in sorted(set(p['year'] for p in DATA['publications']),reverse=True):
 pubs+=f'<h2 class="publication-year-header">{year}</h2>'
 for p in [p for p in DATA['publications'] if p['year']==year]:
  venue=p['venue'].replace(' (listed in 2025 CV entry)','')
  related=''.join(link(url,label) for label,url in p.get('links',[]))
  pubs+=f'<article class="publication"><div class="publication-img"><img src="{p["image"]}" alt="" loading="lazy"></div><div class="publication-content"><p class="eyebrow">{venue}</p><h3><a href="{p["url"]}">{esc(p["title"])}</a></h3><p class="publication-authors">{p["authors"]}</p><div class="publication-links">{related}</div></div><a class="paper-arrow" href="{p["url"]}" aria-label="Read {esc(p["title"])}">↗</a></article>'
pubs+='</section>'
page('publications.html','Publications','Selected scientific publications and preprints by Yichun He and collaborators.',pubs)

resources=[
 ('SpatialAgent','SCIENTIFIC AGENT','AI agents that connect biological questions with spatial analysis tools, literature, and data.','https://github.com/Genentech/SpatialAgent','images/SpatialAgent.png'),
 ('FuseMap','SPATIAL FOUNDATION MODEL','Integrate spatial transcriptomic atlases and learn a shared representation of genes, cells, and tissues.','https://github.com/yichunher/FuseMap','images/fusemap.png'),
 ('molCCF','INTERACTIVE DATA PORTAL','Explore a molecular common coordinate framework spanning 18.6 million cells and 26,665 genes.','https://www.spatial-atlas.net/FuseMap/','images/fusemap.png'),
 ('ClusterMap','SPATIAL ANALYSIS','Identify cells and tissue structures directly from the spatial distribution of RNA molecules.','https://github.com/wanglab-broad/ClusterMap','images/FeatureImage-01.png'),
 ('UnitedNet','MULTIMODAL LEARNING','Integrate biological modalities, predict missing measurements, and explore interpretable relationships.','https://github.com/LiuLab-Bioelectronics-Harvard/UnitedNet','images/unitednet.png'),
 ('AutoSort','NEURAL DECODING','Decode neural signals using multimodal information for long-term recordings from the same cells.','https://github.com/LiuLab-Bioelectronics-Harvard/AutoSort','images/Autosort.png'),
 ('mCNS atlas','ATLAS & ANALYSIS CODE','Explore the spatial atlas of the mouse central nervous system at molecular resolution.','https://github.com/wanglab-broad/mCNS-atlas','images/GraphicAbstract_v2.jpg')]
res=intro('TOOLS & DATA','Built for discovery. <br><em>Shared for what comes next.</em>','Software and data resources developed by Yichun He with collaborators. Explore the repositories and portals to use them in your own research.')
res+='<section class="wrap resource-grid">'
for title,typ,desc,url,img in resources:
 res+=f'<a class="resource" href="{url}"><div class="resource-top"><span class="eyebrow">{typ}</span>{ARROW}</div><h2>{title}</h2><p>{desc}</p><div class="resource-img"><img src="{img}" alt="" loading="lazy"></div></a>'
res+='</section>'
page('resources.html','Tools & data','Explore open scientific software, AI agents, and spatial biology data resources.',res)
news=intro('NEWS & UPDATES','Milestones along <br><em>the way.</em>','Research milestones from Yichun He and collaborators, and the next chapter at Illinois.')
news+='<section class="wrap news-list">'
for year,title,desc,url in [
 ('2026','An agentic spatial molecular foundation model','The FuseMap work is accepted in Nature Methods. The preprint is available below.','https://doi.org/10.1101/2024.05.27.594872'),
 ('2025','SpatialAgent: AI for spatial biology','A collaborative effort to build autonomous AI agents for spatial biological analysis.','https://doi.org/10.1101/2025.04.03.646459'),
 ('2025','Bioelectronics that develop with the brain','Collaborative work on tissue-level-soft bioelectronics appears in Nature.','https://www.nature.com/articles/s41586-025-09106-8'),
 ('2023','A molecular-resolution atlas of the mouse CNS','A spatial reference for the cellular organization of the mouse central nervous system, published in Nature.','https://www.nature.com/articles/s41586-023-06569-5')]:
 news+=f'<article class="news-item"><span class="eyebrow">{year}</span><div><h2>{title}</h2><p>{desc}</p>{link(url,"Read the work")}</div></article>'
news+='</section>'
page('news.html','News','Research milestones and updates from He Lab.',news)
print('Built 7 pages.')
