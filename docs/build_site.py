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
NAV = [('index.html', 'Home'), ('yichun-he.html', 'Yichun He'), ('team.html', 'Lab Members'), ('about.html', 'Research'), ('publications.html', 'Publications'), ('https://sites.google.com/view/yichunhelab-intranet', 'Lab Intranet'), ('join.html', 'Join us!')]

def asset_url(path):
    return f'{path}?v={sha256((ROOT / path).read_bytes()).hexdigest()[:10]}'

def page(file, title, description, body, home=False):
    links = ''.join(f'<a href="{u}"'+(' class="nav-join"' if u=='join.html' else '')+(' aria-current="page"' if file==u else '')+f'>{n}</a>' for u,n in NAV)
    out = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | He Lab</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#ffffff">
<meta property="og:title" content="{esc(title)} | He Lab"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website">
<link rel="icon" href="{asset_url('images/he-lab-brain-favicon.png')}" type="image/png">
<link rel="stylesheet" href="{asset_url('fonts/fonts.css')}">
<link rel="stylesheet" href="{asset_url('lab.css')}"><script src="{asset_url('lab.js')}" defer></script></head>
<body class="{'home' if home else 'inner-page'}"><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><nav class="nav-inner wrap" aria-label="Main navigation">
<a class="brand" href="index.html" aria-label="He Lab home"><img src="{asset_url('images/he-lab-brain-compact.png')}" alt="" width="56" height="56"><span>He Lab</span></a>
<div class="desktop-nav">{links}</div><button id="hamburger" aria-controls="mobile-nav" aria-expanded="false" aria-label="Open menu"><span></span><span></span></button>
</nav><nav id="mobile-nav" class="mobile-nav" aria-label="Mobile navigation" hidden>{links}</nav></header>
<main id="main">{body}</main>
<footer class="site-footer wrap"><div class="footer-title">He Lab · AI for Biology and Human Intelligence</div>
<p>Siebel School of Computing and Data Science <br>University of Illinois Urbana-Champaign</p>
<div class="footer-links"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="https://scholar.google.com/citations?user=LMnJmvIAAAAJ&amp;hl=en">Google Scholar</a><a href="https://github.com/yichunher">GitHub</a></div></footer></body></html>'''
    (ROOT / file).write_text(out)

ARROW='<span aria-hidden="true">↗</span>'
def link(url,text,cl='text-link'): return f'<a class="{cl}" href="{url}">{text} {ARROW}</a>'
def intro(kicker,title,desc):
    title={'OUR RESEARCH':'Research','JOIN HE LAB':'Join us','PUBLICATIONS':'Publications','NEWS & UPDATES':'News'}[kicker]
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

def publication_highlights(publication):
    items = ''
    for note in publication.get('highlights', []):
        text = esc(note['text'])
        if note.get('url'):
            text = f'<a href="{esc(note["url"], quote=True)}">{text}</a>'
        items += f'<li>{text}</li>'
    return f'<ul class="publication-highlights" aria-label="Publication highlights and news">{items}</ul>' if items else ''

RESEARCH_PUBLICATIONS = {
    'cross-organ': ['s41467-021-26044', 's41586-023-06569'],
    'brain': ['618046', 's41467-023-37477'],
    'discovery': ['594872', '646459'],
}

def research_publications(slug, direction):
    slides = []
    for index, key in enumerate(RESEARCH_PUBLICATIONS[slug]):
        p = next(p for p in DATA['publications'] if key in p['url'])
        related = ''.join(link(url, label) for label, url in p.get('links', []))
        slides.append(f'''<article class="research-paper" aria-label="{index + 1} of 2" aria-roledescription="slide">
<a class="research-paper-figure" href="{p['url']}"><img src="{p['image']}" alt="Research overview for {esc(p['title'], quote=True)}" loading="lazy"></a>
<div class="research-paper-copy"><p class="eyebrow">{esc(p['venue'])}</p><h4><a href="{p['url']}">{esc(p['title'])}</a></h4><p class="publication-authors">{p['authors']}</p><div class="publication-links">{related}</div>{publication_highlights(p)}</div>
</article>''')
    return f'''<section class="research-publications" data-publication-carousel role="region" aria-roledescription="carousel" aria-label="Representative publications: {esc(direction, quote=True)}">
<div class="research-publications-heading"><div class="paper-controls" hidden><button type="button" data-paper-toggle>Pause</button><button type="button" data-paper-prev aria-label="Previous publication">←</button><span class="paper-count" aria-live="off">1 / 2</span><button type="button" data-paper-next aria-label="Next publication">→</button></div></div>
<div class="research-paper-stage">{''.join(slides)}</div>
</section>'''

SELECTED=[('594872','A shared molecular model of the brain'),('646459','AI agents for spatial biology'),('s41586-023-06569','Mapping the mouse central nervous system at molecular resolution'),('s41467-023-37477','Connecting multimodal views of cells'),('618046','Tracking neural activity over time'),('s41467-021-26044','Identifying cells and tissue structure from spatial gene expression')]
selected=''
for key,desc in SELECTED:
    p=next(p for p in DATA['publications'] if key in p['url'])
    selected+=f'''<article class="progress-item"><a class="progress-row" href="{p['url']}"><img src="{p['image']}" alt="" loading="lazy"><div><h3>{esc(p['title'])}</h3><p>{desc}</p><span class="progress-venue">{p['venue']}</span></div></a>{publication_highlights(p)}</article>'''

home=f'''
<section class="home-intro wrap"><h1>AI for Biology and Human Intelligence</h1>
<p class="home-subtitle">The <strong>He Lab</strong> at the University of Illinois Urbana-Champaign</p></section>
<section class="home-research wrap" id="research"><h2>Research</h2>
<div class="research-intro"><p>We develop AI to understand how biological changes shape human health and intelligence, and to guide ways of improving both.</p><p>Our research connects molecular and cellular mechanisms to organ function, brain dynamics, and cognition through models whose predictions can be tested experimentally.</p></div>
<div class="directions">{research_cards}</div>
{link('about.html','More about our research','button')}
</section>
<section class="home-progress wrap" id="research-progress"><h2>Selective Publications</h2><div class="progress-list">{selected}</div>{link('publications.html','View all publications','button')}</section>
<section class="home-join wrap"><h2>Join us</h2><p>We welcome students, researchers, and partners who share our curiosity about biology and the potential of AI to benefit people. Help shape the lab as we prepare to launch at Illinois in 2027.</p>{link('join.html','Learn about joining the lab','button')}</section>'''
page('index.html','AI for Biology and Human Intelligence','AI for biological function and disease, the biological basis of human intelligence, and scientific discovery.',home,True)

research=intro('OUR RESEARCH','Research','One question connects our work: how do changes in biological systems shape human health and intelligence, and how can we predict and improve their consequences? We study this across scales, from genes and cells to organs, neural activity, and cognition.')
research+=f'<div class="wrap">{research_framework("research")}</div>'
longs=[
 ('Understanding biological function.', 'How a gene acts depends on the cell, tissue, and organism in which it operates. We aim to uncover how genetic variation, gene regulation, and spatial organization work together to produce biological function, and how disruptions lead to disease. Cross-organ comparisons provide a starting point for identifying shared mechanisms and context-dependent responses.', 'We build spatial and multimodal foundation models to connect molecular measurements with cellular states and tissue function. By integrating perturbation data with causal modeling, we seek to predict the functional consequences of genetic and regulatory changes. Our initial focus on mechanisms linking brain and metabolic disease connects this work directly to our research on brain function and cognition. Experimental collaborations help test and refine these predictions.', 'Key words', 'Spatial & multimodal AI; gene-to-function modeling; cross-organ spatial models; perturbation biology; perturbation-response prediction.'),
 ('Understanding the biological basis of intelligence.', 'Brains combine molecular diversity, spatial organization, and dynamic neural activity. We ask how these biological features work together across scales to support learning, cognition, and social behavior. Comparing brains across species and disease helps us identify shared principles and differences relevant to human intelligence.', 'Building on our work in spatial brain atlases, multimodal learning, and long-term neural decoding, we develop models that integrate molecular profiles, spatial maps, and neural recordings. We seek to connect cell identity and location with circuit dynamics and behavior, and to generate predictions that experimental collaborators can test. Our long-term aim is to inform approaches that preserve and improve human cognitive function.', 'Key words', 'Multimodal brain models; cell-to-circuit relationships and connectivity; neural dynamics; cognition and social behavior across species and disease.'),
 ('Expanding human scientific capabilities.', 'Scientific AI is the shared discovery framework for our work in biology and intelligence. We build agents that bring together molecular data, brain atlases, analysis tools, and literature to help researchers formulate hypotheses, identify informative perturbations, and design experiments.', 'Building on SpatialAgent and FuseMapAgent, we aim to connect measurement, modeling, prediction, and experimental testing in an iterative process. Evidence from both scientific directions can improve shared models, while the models help choose what to investigate next. Our goal is to extend human scientific capabilities while keeping reasoning traceable and predictions testable.', 'Key words', 'Scientific agents; revealing hidden biological structure; hypothesis generation and experimental design; human–AI reasoning.')]
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
 model_path=brain_model_path if slug=='brain' else ''
 research+=f'<section class="research-detail wrap" id="{slug}"><div class="detail-aside"><img src="{im}" alt="{FIGURE_ALTS[slug]}" loading="lazy"/></div><div class="detail-body"><h2>{title}</h2><h3>{q}</h3><p>{p1}</p><p>{p2}</p>{model_path}<div class="research-focus"><span class="eyebrow">{label}</span><p>{esc(projects)}</p></div></div>{research_publications(slug,title)}</section>'
research+=f'<section class="wrap simple-cta"><h2>Join our research</h2>{link("join.html","Join the conversation","button primary")}</section>'
page('about.html','Research','Understanding biological function and disease, the biological basis of intelligence, and AI as a partner in scientific discovery.',research)

def cv_list(items):
    return '<ul class="cv-list">'+''.join(f'<li><span class="cv-year">{esc(year)}</span><div>{text}</div></li>' for year,text in items)+'</ul>'

# Academic history and selected honors follow the supplied CV; the incoming
# Illinois appointment and biography wording follow the user's latest update.
positions=cv_list([
 ('2027–','<strong>Assistant Professor (Incoming)</strong><br>Siebel School of Computing and Data Science<br>University of Illinois Urbana-Champaign'),
 ('2025–present','<strong>Eric and Wendy Schmidt Center Fellow</strong><br>Broad Institute of MIT and Harvard'),
 ('2024','<strong>Research Intern</strong><br>Genentech Research and Early Development (gRED)')])
education=cv_list([
 ('2025','<strong>PhD, Engineering Sciences</strong><br>Harvard University'),
 ('2019','<strong>BE, Electrical Engineering, summa cum laude</strong><br>University of Science and Technology of China')])
honors=cv_list([
 ('2025','Eric and Wendy Schmidt Center Fellow, Broad Institute of MIT and Harvard'),
 ('2024','NIH/NCI Human Tumor Atlas Network (HTAN) Data Jamboree Travel Award'),
 ('2020–2023','James Mills Pierce Fellowship, Harvard University'),
 ('2019','Guo Moruo Scholarship, University of Science and Technology of China'),
 ('2019','Exceptional Undergraduate of the Class of 2019, University of Science and Technology of China'),
 ('2018','Tang Lixin Scholarship'),
 ('2017','National Scholarship, Ministry of Education of China')])
profile=f'''<section class="wrap founder pi-profile" id="yichun-he" aria-labelledby="pi-name">
<div class="founder-photo"><img src="images/YichunHe.jpg" alt="Yichun He"></div>
<div class="profile-body"><p class="eyebrow">Principal Investigator</p><h1 id="pi-name">Yichun He, Ph.D.</h1>
<p class="founder-bio">Yichun He is an incoming assistant professor at the Siebel School of Computing and Data Science, University of Illinois Urbana-Champaign, where she will establish He Lab in 2027. She was an Eric and Wendy Schmidt Center Fellow at the Broad Institute of MIT and Harvard, where she worked with Caroline Uhler on causal and multimodal approaches to biology. In 2024, she worked with Aviv Regev as a research intern at Genentech, developing autonomous AI agents for spatial biology and language models for DNA sequence design. Her research develops AI methods to connect molecular, spatial, and functional views of biological systems, with the goal of understanding and improving human health and intelligence. Her work spans spatial atlases, multimodal learning, neural decoding, and AI agents for scientific discovery. She earned her PhD in Engineering Sciences at Harvard University, advised by Xiao Wang and Jia Liu, and her bachelor's degree in Electrical Engineering at the University of Science and Technology of China.</p>
<div class="profile-links">{link('https://scholar.google.com/citations?user=LMnJmvIAAAAJ&hl=en','Google Scholar')}{link('https://siebelschool.illinois.edu/news/siebel-school-new-faculty-2025','UIUC profile')}{link('mailto:'+EMAIL,'Email')}</div>
<div class="profile-history"><section aria-labelledby="positions-title"><h2 id="positions-title">Positions</h2>{positions}</section><section aria-labelledby="education-title"><h2 id="education-title">Education</h2>{education}</section><section aria-labelledby="honors-title"><h2 id="honors-title">Honors and awards</h2>{honors}</section></div>
</div></section>'''
page('yichun-he.html','Yichun He, Ph.D.','Yichun He, Principal Investigator of He Lab. Biography, positions, education, honors and awards.',profile)

team=f'''<section class="wrap members-intro" id="lab-members" aria-labelledby="members-title"><h1 id="members-title">Lab Members</h1>
<div class="members-invitation"><h2>Build the lab with us</h2>
<p class="page-deck">We are building He Lab to explore how AI can reveal the biological principles underlying human health and intelligence—from genes and cells to neural circuits and cognition.</p>
<p class="page-deck">Our research builds on spatial brain atlases, multimodal learning, neural decoding, and AI agents for scientific discovery. We invite students and researchers to help shape the questions, methods, and culture of the lab from the beginning.</p>
{link('publications.html','Explore our work')}</div></section>
<section class="wrap members-culture" aria-label="Research culture and mentorship"><p>Bring your own questions and the curiosity to explore beyond your field. We support each member in developing scientific judgment and an independent research direction. We value open discussion, shared learning, and recognition of everyone’s contributions.</p>
{link('join.html','Join us!','button primary')}</section>'''
page('team.html','Lab Members','Meet the research community we are building at He Lab.',team)

join=intro('JOIN HE LAB','Join us','Help shape AI for biology and human intelligence. We welcome inquiries for our 2027 launch at Illinois from people with strong programming and quantitative skills, curiosity, and independent thinking. Our research spans multimodal and causal AI, computational biology and neuroscience, and scientific agents. Prior biology training is welcome but not required.')
join+='''<section class="wrap join-campus" aria-label="Explore the Illinois campus and the Siebel School">
<figure><img src="images/uiuc-campus.webp" width="532" height="297" alt="An aerial view of the University of Illinois Urbana-Champaign campus, with leafy walkways, red-brick buildings, and the Main Quad at dusk." decoding="async"><figcaption><a href="https://illinois.edu/">University of Illinois Urbana-Champaign <span aria-hidden="true">↗</span></a><p class="campus-highlight"><a href="https://www.sixt.com/magazine/tips/beautiful-college-campuses/">The Most Beautiful College Campuses in the U.S. <span aria-hidden="true">↗</span></a></p></figcaption></figure>
<figure><img src="images/uiuc-siebel-center.webp" width="1200" height="809" alt="The glass-fronted computer science building at Illinois, with illuminated walkways and a blue evening sky." decoding="async"><figcaption><a href="https://siebelschool.illinois.edu/">Siebel School of Computing and Data Science <span aria-hidden="true">↗</span></a><p class="campus-highlight"><a href="https://csrankings.org/#/index?all&amp;us">Top U.S. computer science program <span aria-hidden="true">↗</span></a></p></figcaption></figure>
</section>'''
join+=f'''<section class="wrap join-layout" aria-labelledby="opportunities-title"><aside><h2 id="opportunities-title">Research opportunities</h2></aside><div class="opportunities">
<article id="postdoctoral"><h3>Postdoctoral fellows and scientists</h3><p>Send your <strong>CV, representative papers or code, a one-page research statement,</strong> contact details for three references, and preferred start date.</p></article>
<article id="graduate"><h3>Graduate students</h3><p><strong>Current or admitted Illinois students:</strong> send your CV, program, and a brief summary of your research experience and interests.</p><p><strong>Prospective students:</strong> send your CV, transcripts, and research interests. Apply through the relevant Illinois graduate program.</p>{link('https://siebelschool.illinois.edu/academics/graduate','Graduate admissions')}</article>
<article id="undergraduate"><h3>Undergraduates and interns</h3><p>Students from Illinois and other institutions are welcome. Send your <strong>CV, interests, relevant coursework, and availability,</strong> plus a project or code sample if available.</p></article>
<article id="visiting"><h3>Visiting scholars</h3><p>Send your <strong>CV, home institution, proposed research question, and visit dates.</strong> We can discuss project fit and visit arrangements directly.</p></article></div></section>
<section class="mission-band"><div class="wrap mission-grid"><div><h2>Collaborate with us</h2><p>We welcome experimental researchers, clinicians, industry partners, and supporters to explore shared questions in biological discovery and human health.</p></div></div></section>
<section class="wrap join-context" aria-label="Contact and location">
<div><h2>Contact</h2><p>Yichun He</p><a href="mailto:{EMAIL}" class="contact-address">{EMAIL} ↗</a></div>
<div><h2>Location</h2><p>Siebel School of Computing and Data Science<br>University of Illinois Urbana-Champaign</p></div>
</section>'''
page('join.html','Join us','Explore research opportunities and collaborations with He Lab, launching at Illinois in 2027.',join)

pubs=intro('PUBLICATIONS','The work behind <br><em>the questions.</em>','Selected publications and preprints by Yichun He and collaborators, including work completed before the launch of He Lab.')
pubs+='<section class="wrap publication-list"><p class="pub-key"># Equal contribution · * Corresponding author</p>'
for year in sorted(set(p['year'] for p in DATA['publications']),reverse=True):
 pubs+=f'<h2 class="publication-year-header">{year}</h2>'
 for p in [p for p in DATA['publications'] if p['year']==year]:
  venue=p['venue'].replace(' (listed in 2025 CV entry)','')
  related=''.join(link(url,label) for label,url in p.get('links',[]))
  highlights=publication_highlights(p)
  pubs+=f'<article class="publication"><div class="publication-img"><img src="{p["image"]}" alt="" loading="lazy"></div><div class="publication-content"><p class="eyebrow">{venue}</p><h3><a href="{p["url"]}">{esc(p["title"])}</a></h3><p class="publication-authors">{p["authors"]}</p><div class="publication-links">{related}</div>{highlights}</div><a class="paper-arrow" href="{p["url"]}" aria-label="Read {esc(p["title"])}">↗</a></article>'
pubs+='</section>'
page('publications.html','Publications','Selected scientific publications and preprints by Yichun He and collaborators.',pubs)

news=intro('NEWS & UPDATES','Milestones along <br><em>the way.</em>','Research milestones from Yichun He and collaborators, and the next chapter at Illinois.')
news+='<section class="wrap news-list">'
for year,title,desc,url in [
 ('2026','An agentic spatial molecular foundation model','The FuseMap work is accepted in Nature Methods. The preprint is available below.','https://doi.org/10.1101/2024.05.27.594872'),
 ('2025','SpatialAgent: AI for spatial biology','SpatialAgent: An Autonomous AI Agent for Spatial Biology is available as a bioRxiv preprint.','https://doi.org/10.1101/2025.04.03.646459'),
 ('2025','Bioelectronics that develop with the brain','Collaborative work on tissue-level-soft bioelectronics appears in Nature.','https://www.nature.com/articles/s41586-025-09106-8'),
 ('2023','A molecular-resolution atlas of the mouse CNS','A spatial reference for the cellular organization of the mouse central nervous system, published in Nature.','https://www.nature.com/articles/s41586-023-06569-5')]:
 news+=f'<article class="news-item"><span class="eyebrow">{year}</span><div><h2>{title}</h2><p>{desc}</p>{link(url,"Read the work")}</div></article>'
news+='</section>'
page('news.html','News','Research milestones and updates from He Lab.',news)
print('Built 7 pages.')
