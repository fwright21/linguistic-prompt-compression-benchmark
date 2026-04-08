# Live Test Results

Generated: 2026-04-07 23:25

Runner: `codex`

Repeats per prompt/query: `3`

Baseline: `caveman_real_full`

Caveman skill source: JuliusBrussee/caveman (https://github.com/JuliusBrussee/caveman, accessed 2026-04-07)

## Per-Query Results

### simple_factual: _What is the capital of France?_

**caveman_real_lite** [1 avg words]  (+0.0% vs caveman)
Run word counts: `[1, 1, 1]`
> Paris.

**caveman_real_full** [1 avg words]  (baseline)
Run word counts: `[1, 1, 1]`
> Paris.

**caveman_real_ultra** [1 avg words]  (+0.0% vs caveman)
Run word counts: `[1, 1, 1]`
> Paris.

**round1** [4.7 avg words]  (-366.7% vs caveman)
Run word counts: `[3, 7, 4]`
> France capital Paris

**round2** [3 avg words]  (-200.0% vs caveman)
Run word counts: `[3, 3, 3]`
> Paris capital France.

**round3** [4 avg words]  (-300.0% vs caveman)
Run word counts: `[5, 4, 3]`
> Paris serve capital for France.

**round4_final** [3 avg words]  (-200.0% vs caveman)
Run word counts: `[3, 3, 3]`
> Paris
Outcome: correct

### process_explanation: _What is photosynthesis?_

**caveman_real_lite** [65.3 avg words]  (-8.9% vs caveman)
Run word counts: `[66, 65, 65]`
> Photosynthesis is process plants, algae, and some bacteria use to turn light energy into chemical energy.

They take in:
- carbon dioxide from air
- water
- sunlight

They make:
- glucose, which stores energy
- oxygen, released as byproduct

Basic equation:
`6 CO2 + 6 H2O + light -> C6H12O6 + 6 O2`

In plants, this happens mainly in chloroplasts, using chlorophyll to capture light.

**caveman_real_full** [60 avg words]  (baseline)
Run word counts: `[62, 56, 62]`
> Photosynthesis: process plants, algae, some bacteria use light energy to make sugar from carbon dioxide and water.

Core reaction:
`6CO2 + 6H2O + light -> C6H12O6 + 6O2`

What happens:
- chlorophyll absorbs light
- light reactions make ATP, NADPH
- Calvin cycle uses CO2 to build glucose

Why matters:
- makes biomass
- releases oxygen
- base of most food webs

**caveman_real_ultra** [64.7 avg words]  (-7.8% vs caveman)
Run word counts: `[82, 58, 54]`
> Photosynthesis = plants, algae, some bacteria turn light + CO2 + H2O -> sugar + O2.

Core eq:
6CO2 + 6H2O + light -> C6H12O6 + 6O2

Where:
- chloroplast
- chlorophyll catch light

2 big stages:
- light reactions -> make ATP, NADPH, split water, release O2
- Calvin cycle -> use CO2 + ATP + NADPH -> build glucose

Why matter:
- makes food base for most life
- makes much Earth oxygen
- stores sun energy in chemical bonds

**round1** [27.3 avg words]  (+54.4% vs caveman)
Run word counts: `[26, 34, 22]`
> - Photosynthesi: plant, alga, some bacteria use light energy convert carbon dioxide + water into sugar + oxygen
- Proces store light energy in chemical bond

**round2** [23.7 avg words]  (+60.6% vs caveman)
Run word counts: `[21, 22, 28]`
> Photosynthesis process. Plant algae some bacteria use light. Process convert water carbon dioxide into sugar oxygen. Light energy become chemical energy.

**round3** [22.7 avg words]  (+62.2% vs caveman)
Run word counts: `[23, 19, 26]`
> Photosynthesis: plant algae some bacteria use sunlight and convert water and carbon dioxide into sugar and oxygen. This process store energy in sugar.

**round4_final** [25.7 avg words]  (+57.2% vs caveman)
Run word counts: `[24, 27, 26]`
> - Photosynthesis: plant, algae, some bacteria use light energy to convert carbon dioxide + water into sugar; process release oxygen
- Outcome: definition give

### comparison: _What is the difference between RAM and storage?_

**caveman_real_lite** [86 avg words]  (+7.2% vs caveman)
Run word counts: `[83, 89, 86]`
> RAM is short-term working memory. Storage is long-term data memory.

RAM:
- Holds data programs use right now.
- Much faster.
- Usually clears when power turns off.
- Affects multitasking and app responsiveness.

Storage:
- Holds files, apps, and system data long term.
- Slower than RAM.
- Keeps data when power turns off.
- Affects how much stuff you can save.

Simple example:
- RAM = desk space you work on now.
- Storage = filing cabinet where you keep things.

**caveman_real_full** [92.7 avg words]  (baseline)
Run word counts: `[114, 77, 87]`
> RAM: short-term working memory. Storage: long-term data keeping.

RAM:
- Holds data programs use right now
- Fast
- Usually volatile: clears on power off
- Smaller capacity
- Affects multitasking, active app performance

Storage:
- Holds files, apps, OS long term
- Slower than RAM
- Non-volatile: keeps data when power off
- Larger capacity
- Affects how much stuff you can save, load times

Simple:
- RAM = desk space
- Storage = filing cabinet

Example:
- Open app: moves from storage into RAM
- Use app: CPU works with data in RAM
- Shut down: RAM clears, storage stays

Common types:
- RAM: DDR4, DDR5
- Storage: SSD, HDD, NVMe SSD

**caveman_real_ultra** [61.7 avg words]  (+33.5% vs caveman)
Run word counts: `[77, 67, 41]`
> RAM = short-term working memory. Storage = long-term saved data.

RAM:
- holds stuff CPU using now
- very fast
- usually volatile -> power off = gone
- affects multitasking, app responsiveness

Storage:
- holds OS, apps, files long-term
- slower than RAM
- non-volatile -> power off = stays
- SSD/HDD/flash

Rule:
- RAM = desk space
- storage = filing cabinet

More RAM -> more things open smooth.
More storage -> more files/apps fit.

**round1** [64.3 avg words]  (+30.6% vs caveman)
Run word counts: `[59, 66, 68]`
> - RAM store data for active task.
- CPU access RAM fast.
- Power loss erase RAM.

- Storage keep data for long term.
- CPU access storage slow relative RAM.
- Power loss not erase storage.

- Outcome: more RAM improve speed for running app and multitask.
- Outcome: more storage increase space for file, app, photo, video.

**round2** [49.7 avg words]  (+46.4% vs caveman)
Run word counts: `[61, 42, 46]`
> RAM hold data and program now. Storage hold data and program long term.

RAM lose data after power off. Storage keep data after power off.

RAM give much faster access. Storage give much larger capacity.

CPU use RAM for active work. User use storage for apps, files, photos, videos.

Simple rule:
RAM = short-term working memory.
Storage = long-term saved space.

**round3** [49 avg words]  (+47.1% vs caveman)
Run word counts: `[50, 49, 48]`
> RAM hold data for active program now. Storage hold data for long-term keep.

Computer read RAM very fast. Computer use storage more slow.

Power off erase RAM data. Power off no erase storage data.

RAM affect speed for task now. Storage affect how much file app system data computer keep.

**round4_final** [59.7 avg words]  (+35.6% vs caveman)
Run word counts: `[54, 69, 56]`
> - RAM: computer use RAM for short-term work; RAM hold data and program during active use; power loss erase RAM
- Storage: computer use storage for long-term keep; storage hold file, app, system after power loss
- Outcome: more RAM improve active task speed and multitask capacity; more storage increase file and app capacity

### recommendation: _Should I use Python or JavaScript for web scraping?_

**caveman_real_lite** [162 avg words]  (+0.8% vs caveman)
Run word counts: `[172, 192, 122]`
> Use Python if goal is scraping fast, clean, and with less pain.

Use JavaScript if target site is heavy client-side app and you already live in Node/browser tooling.

Quick rule:
- Python: best default for most scraping.
- JavaScript: best when site behavior depends on browser execution and your stack already uses JS.

Why Python:
- Better scraping ecosystem: `requests`, `httpx`, `BeautifulSoup`, `lxml`, `Scrapy`.
- Faster to write and maintain for data extraction.
- Better for parsing, pipelines, CSV/JSON, pandas cleanup.

Why JavaScript:
- Strong with browser automation: `Playwright`, `Puppeteer`.
- Good for SPAs, dynamic rendering, login flows, button-click scraping.
- Nice if backend and tooling already in Node.

Best practical choice:
- Static or lightly dynamic pages: Python.
- Complex interactive pages: either language with Playwright.
- Large-scale crawler: Python usually wins on ergonomics.
- Full-stack JS team: JavaScript may reduce context switching.

Best answer for most people: Python first. Use JavaScript when browser-heavy pages make it the more natural fit.

Also: respect robots.txt, site terms, rate limits, and privacy law.

**caveman_real_full** [163.3 avg words]  (baseline)
Run word counts: `[217, 153, 120]`
> Python if goal = scrape fast, parse messy HTML, use mature tooling. JavaScript if target site = heavy client-side app, need real browser behavior, or rest of stack already Node.

Fast rule:
- Python: best default
- JavaScript: best for browser-first scraping

Python strengths:
- `requests`, `httpx`, `BeautifulSoup`, `lxml`, `Scrapy`
- Cleaner data pipelines: `pandas`, CSV, JSON, ML/NLP follow-up
- Less boilerplate for parsing, retries, transforms
- Better ecosystem for large crawl jobs

JavaScript strengths:
- `Playwright`, `Puppeteer` strong for dynamic pages
- Same language as browser runtime
- Easy when scraping needs DOM events, SPA navigation, JS-rendered content
- Good if app/backend already Node

Use Python when:
- Static pages or simple API calls
- Need speed of development
- Need parsing, cleaning, analysis
- Building crawler, ETL, research workflow

Use JavaScript when:
- Site blocks non-browser clients
- Need headless browser often
- Must execute page JS, click flows, wait for render
- Team already ships Node services

Practical truth:
- Best stack often hybrid
- Python for bulk fetch + parse
- JavaScript browser automation only for hard pages

Default choice:
- New scraping project, unknown target: Python + Playwright if needed
- Browser-heavy target from start: JavaScript + Playwright

If want one answer only: use Python unless site strongly depends on client-side JavaScript.

**caveman_real_ultra** [102.7 avg words]  (+37.1% vs caveman)
Run word counts: `[136, 94, 78]`
> Python if goal = fast build, rich scraping stack, data cleanup.

JavaScript if goal = browser-heavy sites, same lang front+back, Playwright/Puppeteer flow.

Rule:
- Python -> best default for scraping
- JavaScript -> best for dynamic JS pages, browser automation

Why Python:
- stronger scraping ecosystem: `requests`, `httpx`, `BeautifulSoup`, `lxml`, `Scrapy`
- cleaner for parsing, ETL, CSV/JSON, pandas
- less boilerplate, faster prototyping

Why JavaScript:
- native fit for SPA sites, DOM, browser execution
- strong tools: `Playwright`, `Puppeteer`
- easier if team already Node-only

Practical pick:
- mostly static HTML/API pages -> Python
- lots JS rendering, login flows, user actions -> JavaScript or Playwright
- max flexibility -> Python + Playwright also strong

Short answer:
- new project, unsure -> Python
- browser automation first -> JavaScript
- pure scraping/data pipeline -> Python win

**round1** [83 avg words]  (+49.2% vs caveman)
Run word counts: `[98, 81, 70]`
> - Python suit most web scraping task
- Python offer mature scraping library ecosystem: `requests`, `httpx`, `BeautifulSoup`, `lxml`, `Scrapy`
- Python enable faster scrape workflow setup and cleaner data parsing
- JavaScript suit browser-heavy scraping task
- JavaScript fit site with strong client-side rendering, SPA behavior, anti-bot interaction, DOM event dependency
- JavaScript align with `Playwright` or `Puppeteer` workflow and Node stack reuse
- But Python also handle browser automation well with `Playwright` and `Selenium`

- Outcome: use Python by default
- Outcome: use JavaScript when target site require deep in-browser execution or existing codebase depend on Node

**round2** [57.3 avg words]  (+64.9% vs caveman)
Run word counts: `[61, 67, 44]`
> Use Python for most web scraping.

Python offer better scraping ecosystem. `requests`, `BeautifulSoup`, `Scrapy` reduce effort. Python suit parsing, cleaning, data export.

Use JavaScript for dynamic sites. JavaScript suit pages with heavy client-side rendering. `Playwright` and `Puppeteer` handle browser automation well.

Default choice: Python.  
Exception: choose JavaScript if target site depend on browser execution or if full project already use Node.

**round3** [57.7 avg words]  (+64.7% vs caveman)
Run word counts: `[64, 51, 58]`
> Python suit web scrap use better for most people. Python offer `requests`, `BeautifulSoup`, `Scrapy`, `Playwright`. Python code stay short.

JavaScript fit better if site need heavy browser automation or if you already use Node.js stack. JavaScript offer `Puppeteer`, `Playwright`, `Cheerio`.

If you want simple rule:
Python use for fast start and general web scrap.
JavaScript use if dynamic page dominate or Node.js stack matter.

**round4_final** [70 avg words]  (+57.1% vs caveman)
Run word counts: `[86, 49, 75]`
> - Use Python for most web scraping.
- Python give simpler libraries: `requests`, `BeautifulSoup`, `Scrapy`.
- Python fit static pages, fast scripts, data cleaning pipelines.
- Use JavaScript for pages with heavy client-side rendering, browser automation, site behavior tied to frontend runtime.
- JavaScript give stronger fit with `Playwright`, `Puppeteer`, full DOM event handling.
- If goal general scraping, choose Python.
- If goal React/Vue/SPA scraping with login flows, infinite scroll, anti-bot browser simulation, choose JavaScript.

Outcome: Python default choice; JavaScript niche choice for browser-driven scraping.

### multistep: _How do I set up a Python virtual environment?_

**caveman_real_lite** [54 avg words]  (+5.8% vs caveman)
Run word counts: `[50, 47, 65]`
> Use `venv`.

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Windows `cmd`:

```bat
.venv\Scripts\activate.bat
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install packages inside env:

```bash
pip install package-name
```

Deactivate when done:

```bash
deactivate
```

If `venv` missing on Debian/Ubuntu:

```bash
sudo apt install python3-venv
```

**caveman_real_full** [57.3 avg words]  (baseline)
Run word counts: `[64, 58, 50]`
> Use `venv`.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows `cmd`:

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Install packages:

```bash
pip install <package>
```

Leave env:

```bash
deactivate
```

If `venv` missing, install Python package support first:
- Debian/Ubuntu: `sudo apt install python3-venv`
- macOS, Windows: usually built in with normal Python install

**caveman_real_ultra** [64.3 avg words]  (-12.2% vs caveman)
Run word counts: `[57, 82, 54]`
> `cd` project dir

Create venv:
```bash
python3 -m venv .venv
```

Activate:
```bash
source .venv/bin/activate
```

Windows `cmd`:
```bat
.venv\Scripts\activate.bat
```

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Install packages:
```bash
pip install package-name
```

Save deps:
```bash
pip freeze > requirements.txt
```

Exit venv:
```bash
deactivate
```

If `venv` missing:
```bash
python3 -m pip install --upgrade pip
```

**round1** [52.7 avg words]  (+8.1% vs caveman)
Run word counts: `[56, 48, 54]`
> - Install Python 3
- Open terminal
- Go project directory
- Run `python3 -m venv .venv`
- Activate environment:
- macOS Linux: `source .venv/bin/activate`
- Windows cmd: `.venv\Scripts\activate.bat`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Install package with `pip install package-name`
- Deactivate environment with `deactivate`

Outcome: project get isolated Python environment with separate package install location

**round2** [34.7 avg words]  (+39.5% vs caveman)
Run word counts: `[28, 26, 50]`
> Run `python3 -m venv .venv`.

Activate environment.

macOS Linux:
```bash
source .venv/bin/activate
```

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Install package with `pip install package_name`.

Leave environment with `deactivate`.

**round3** [42 avg words]  (+26.7% vs caveman)
Run word counts: `[32, 55, 39]`
> You run `python3 -m venv .venv`.

You activate env:
- macOS/Linux: `source .venv/bin/activate`
- Windows CMD: `.venv\Scripts\activate`
- PowerShell: `.\.venv\Scripts\Activate.ps1`

You install package with `pip install <package>`.

You deactivate env with `deactivate`.

**round4_final** [39 avg words]  (+32.0% vs caveman)
Run word counts: `[52, 33, 32]`
> - Install Python 3
- Open terminal
- Go directory: `cd path/to/project`
- Create environment: `python3 -m venv .venv`
- Activate environment
- macOS Linux: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Windows cmd: `.venv\Scripts\activate.bat`
- Install package: `pip install package-name`
- Deactivate environment: `deactivate`

Outcome: project use isolated Python package environment

### ambiguous: _Tell me about machine learning._

**caveman_real_lite** [263.3 avg words]  (+6.8% vs caveman)
Run word counts: `[283, 247, 260]`
> Machine learning is way for computers to learn patterns from data instead of following only hand-written rules.

Core idea:
- Give model many examples.
- Model finds statistical patterns.
- Model uses patterns to make predictions or decisions on new data.

Common types:
- Supervised learning: Learn from labeled examples. Example: spam vs not spam.
- Unsupervised learning: Find structure without labels. Example: group similar customers.
- Reinforcement learning: Learn by trial, error, and rewards. Example: game-playing agents.

Common tasks:
- Classification: Pick category.
- Regression: Predict number.
- Clustering: Group similar items.
- Recommendation: Suggest products, videos, songs.
- Generation: Create text, images, audio.

How it usually works:
1. Collect data.
2. Clean and prepare data.
3. Choose model.
4. Train model on data.
5. Test on unseen data.
6. Deploy and monitor.

Important terms:
- Features: input information used by model.
- Labels: correct answers in training data.
- Training: process of adjusting model parameters.
- Inference: using trained model to make prediction.
- Overfitting: model memorizes training data, performs badly on new data.
- Generalization: model performs well on new data.

Popular model families:
- Linear models
- Decision trees and random forests
- Gradient boosted trees
- Neural networks
- Transformers

Why people use it:
- Handles complex patterns hard to code by hand.
- Improves with more data and tuning.
- Powers search, ads, fraud detection, speech recognition, vision, and chat systems.

Limits:
- Needs good data.
- Can learn bias from data.
- Can fail badly outside training conditions.
- Often hard to explain fully.
- High accuracy does not mean true understanding.

Short version:
Machine learning is pattern-finding from data to make useful predictions or decisions.

**caveman_real_full** [282.7 avg words]  (baseline)
Run word counts: `[325, 260, 263]`
> Machine learning: methods that learn patterns from data, not hand-written rules.

Core idea:
- Input data in
- Model maps input to output
- Training adjusts parameters to reduce error
- Good model generalizes to new data

Main types:
- Supervised learning: learn from labeled examples. Tasks: classification, regression.
- Unsupervised learning: find structure in unlabeled data. Tasks: clustering, dimensionality reduction.
- Reinforcement learning: agent acts, gets rewards, learns policy.
- Self-supervised learning: create learning signal from data itself. Big in modern language, vision models.

Common models:
- Linear regression, logistic regression
- Decision trees, random forests, gradient boosting
- Support vector machines
- Neural networks, deep learning
- Transformers for language, vision, multimodal work

Basic workflow:
- Collect data
- Clean, split train/validation/test
- Choose model
- Train on train set
- Tune on validation set
- Measure on test set
- Deploy, monitor drift, retrain if needed

Key concepts:
- Features: variables model uses
- Labels: targets model predicts
- Loss function: error score to minimize
- Optimization: usually gradient descent variants
- Overfitting: memorizes train data, fails on new data
- Underfitting: too simple, misses pattern
- Regularization: constrain model, improve generalization
- Bias/variance tradeoff: simplicity vs flexibility

Metrics depend on task:
- Classification: accuracy, precision, recall, F1, ROC-AUC
- Regression: MAE, MSE, RMSE, R-squared
- Ranking/generation: task-specific eval, often human review too

Why useful:
- Scales pattern finding
- Handles noisy, complex data
- Powers search, recommendation, fraud detection, speech, vision, translation, chatbots, forecasting

Limits:
- Needs good data
- Can encode bias in data
- Can fail out of distribution
- Often hard to interpret
- High accuracy not same as causality or truth

Deep learning:
- Subset of ML using multi-layer neural nets
- Strong on images, audio, text
- Needs lots of data, compute, tuning

If want, can give:
- 5-minute beginner version
- math version
- practical Python example
- ML vs AI vs deep learning comparison

**caveman_real_ultra** [239 avg words]  (+15.4% vs caveman)
Run word counts: `[241, 238, 238]`
> Machine learning = computers learn patterns from data, not hand-written rules for every case.

Core idea:
- input data + target/feedback -> model
- model adjusts parameters to reduce error
- after training, model predicts on new data

Main types:
- supervised: labeled data. Examples: spam detect, price predict, image classify
- unsupervised: no labels. Examples: clustering, anomaly detect, dimensionality reduction
- reinforcement: agent acts, gets rewards, learns policy

Common models:
- linear/logistic regression
- decision trees, random forests, gradient boosting
- neural nets
- transformers

Basic workflow:
1. collect data
2. clean/split data
3. choose model
4. train
5. validate/tune
6. test
7. deploy
8. monitor drift/errors

Key terms:
- features = input variables
- labels = desired outputs
- loss = error measure
- parameters/weights = learned values
- overfitting = memorizes train set, fails new data
- generalization = works on unseen data

Why useful:
- finds complex patterns
- scales to huge data
- automates prediction/decision support

Limits:
- needs good data
- bias in data -> bias in model
- can overfit
- often weak at causality/explanation
- performance can decay if world changes

Deep learning:
- subset of ML using multi-layer neural nets
- strong for images, audio, language
- usually needs more data/compute

LLMs:
- ML models, usually deep learning + transformers
- trained on massive text -> predict next tokens -> language skills

Short version:
data -> training -> pattern learning -> prediction.

**round1** [300 avg words]  (-6.1% vs caveman)
Run word counts: `[215, 306, 379]`
> - Machine learning = computer system learn pattern from data.
- System map input to output.
- System improve prediction, classification, generation, decision.

- Main type:
- Supervised learning: model learn from labeled example.
- Unsupervised learning: model find cluster, structure, relation in unlabeled data.
- Reinforcement learning: agent learn action from reward, penalty.

- Common method:
- Linear model predict value or class.
- Decision tree split feature space.
- Neural network learn complex pattern through layered parameter.
- Deep learning = neural network with many layer.

- Typical workflow:
- Researcher collect data.
- Researcher clean data.
- Researcher choose model.
- Researcher train model on training set.
- Researcher test model on validation set and test set.
- Researcher deploy model for real task.

- Common use:
- Spam filter detect junk mail.
- Recommender system suggest video, music, product.
- Vision model detect object in image.
- Speech model transcribe audio.
- Language model generate text.

- Key issue:
- Bad data produce bad model.
- Overfitting happen when model memorize training data.
- Bias in data produce unfair output.
- Large model require large compute, energy, money.
- Weak interpretability limit trust in some domain.

- Core idea:
- Data shape parameter.
- Parameter shape behavior.
- Behavior solve task.

**round2** [139.3 avg words]  (+50.7% vs caveman)
Run word counts: `[125, 124, 169]`
> Machine learning train computer system from data. System find pattern. System use pattern for prediction, classification, decision.

Main types include supervised learning, unsupervised learning, reinforcement learning. Supervised learning map input to known output. Unsupervised learning group data or find structure. Reinforcement learning optimize action through reward.

Common methods include linear regression, decision tree, neural network, support vector machine. Neural network power many modern system for vision, speech, language.

Machine learning need data, model, training process, evaluation. Good data improve result. Bad data create bias, error, instability. Overfitting hurt generalization. Regularization, validation, test set reduce risk.

Common use cases include spam filtering, recommendation, fraud detection, translation, medical imaging, autonomous system. Machine learning offer strong capability. Machine learning also create risk through bias, opacity, privacy loss, misuse.

**round3** [96.7 avg words]  (+65.8% vs caveman)
Run word counts: `[81, 98, 111]`
> Machine learning use data for pattern discovery and prediction. Researcher train model with example. Model learn relation between input and output. Common type include supervised learning unsupervised learning reinforcement learning. Supervised learning map label to data. Unsupervised learning find pattern or cluster in data. Reinforcement learning optimize action through reward. Machine learning power search recommendation vision speech translation diagnosis fraud detection. Limitation include bias overfit high data need low interpretability. Good practice require clean data strong evaluation clear goal human oversight.

**round4_final** [158.7 avg words]  (+43.9% vs caveman)
Run word counts: `[133, 244, 99]`
> - Machine learning use data for pattern learning.
- Machine learning use model for input-output mapping.
- Developer give data to model.
- Training algorithm change model parameter.
- Model minimize error on training task.
- Model make prediction for new data.
- Supervised learning use labeled example.
- Unsupervised learning find cluster, structure, relation.
- Reinforcement learning use reward signal for action policy.
- Neural network use layer for feature transformation.
- Deep learning use many layer for complex pattern.
- Common use include vision, speech, translation, search, recommendation, fraud detection.
- Main risk include overfitting, bias, data leak, weak generalization, low interpretability.
- Good practice include clean data, train-test split, metric choice, regularization, validation, monitoring.
- Machine learning give automation for prediction task.
- Outcome: reader get compact map for field.

## Summary Table

| Query | caveman_real_lite | caveman_real_full | caveman_real_ultra | round1 | round2 | round3 | round4_final |
|---|---|---|---|---|---|---|---|
| simple_factual | 1 (+0.0%) | 1 | 1 (+0.0%) | 4.7 (-366.7%) | 3 (-200.0%) | 4 (-300.0%) | 3 (-200.0%) |
| process_explanation | 65.3 (-8.9%) | 60 | 64.7 (-7.8%) | 27.3 (+54.4%) | 23.7 (+60.6%) | 22.7 (+62.2%) | 25.7 (+57.2%) |
| comparison | 86 (+7.2%) | 92.7 | 61.7 (+33.5%) | 64.3 (+30.6%) | 49.7 (+46.4%) | 49 (+47.1%) | 59.7 (+35.6%) |
| recommendation | 162 (+0.8%) | 163.3 | 102.7 (+37.1%) | 83 (+49.2%) | 57.3 (+64.9%) | 57.7 (+64.7%) | 70 (+57.1%) |
| multistep | 54 (+5.8%) | 57.3 | 64.3 (-12.2%) | 52.7 (+8.1%) | 34.7 (+39.5%) | 42 (+26.7%) | 39 (+32.0%) |
| ambiguous | 263.3 (+6.8%) | 282.7 | 239 (+15.4%) | 300 (-6.1%) | 139.3 (+50.7%) | 96.7 (+65.8%) | 158.7 (+43.9%) |
| **TOTAL** | **631.7** (+3.9%) | **657** | **533.3** (+18.8%) | **532** (+19.0%) | **307.7** (+53.2%) | **272** (+58.6%) | **356** (+45.8%) |

## Verdict

**Beats caveman_real_full:** caveman_real_lite, caveman_real_ultra, round1, round2, round3, round4_final
**Best overall:** round3 (+58.6% vs caveman_real_full)