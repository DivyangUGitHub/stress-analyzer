# Stress Analyzer

Measure perceived stress with the PSS-10 scale. Get advice that fits the score.

&nbsp;

| | |
|:--|:--|
| **Type** | Mini project, B.Tech CSE |
| **Course** | Understanding Self for Effectiveness and Personality Development |
| **Unit** | 4. Stress and Coping Strategies |
| **Scale** | Perceived Stress Scale, PSS-10 |
| **Language** | Python 3.8+ |
| **Licence** | MIT |

---

## 01 Overview

Most students notice stress only when it is already serious. This program turns the standard PSS-10 questionnaire into a short, clear report.

1. Ask ten questions. Validate every answer.
2. Reverse-score the positive items.
3. Sum to a score from 0 to 40.
4. Classify as low, moderate or high.
5. Name the matching stage of Selye's General Adaptation Syndrome.
6. Suggest coping strategies for that level.
7. Draw a dashboard against a simulated group.

> Self-awareness tool, not a medical diagnosis. If you feel overwhelmed, speak to a counsellor or doctor.

---

## 02 Output

**Console report**

<img src="assets/console.png" width="520" alt="Console report">

&nbsp;

**Dashboard**

<img src="assets/dashboard.png" width="100%" alt="Dashboard: score position, distribution, category share">

---

## 03 Method

<img src="assets/flowchart.png" width="100%" alt="Program flow">

&nbsp;

**Reverse scoring**, items 4, 5, 7, 8

$$x' = 4 - x$$

**Total score**

$$PSS = \sum_{i=1}^{10} x_i \qquad 0 \le PSS \le 40$$

**Stress index**

$$\text{Stress Index (\%)} = \frac{PSS}{40} \times 100$$

**Group statistics**

$$\mu = \frac{\sum \text{scores}}{n} \qquad s = \sqrt{\frac{\sum (\text{score}-\mu)^2}{n-1}}$$

&nbsp;

| Score | Category | GAS stage |
|:--|:--|:--|
| 0 to 13 | Low | Normal / Alarm |
| 14 to 26 | Moderate | Resistance |
| 27 to 40 | High | Exhaustion risk |

**Example.** Answers `2 2 3 2 2 3 2 2 2 3` give PSS = 23, index 57.5 %, moderate.

---

## 04 Usage

```bash
git clone https://github.com/DivyangUGitHub/stress-analyzer.git
cd stress-analyzer
pip install -r requirements.txt
python stress_analyzer.py
```

Answer each question from 0 (never) to 4 (very often). The report prints in the terminal and `dashboard.png` is saved in the same folder.

Run the tests:

```bash
python tests.py
```

---

## 05 Structure

```
stress-analyzer/
  stress_analyzer.py    program
  tests.py              unit tests
  requirements.txt
  assets/               images used in this file
  docs/                 full project report (.docx)
  LICENSE
  README.md
```

---

## 06 Features

| | |
|:--|:--|
| Scale | PSS-10, answers 0 to 4 |
| Scoring | Automatic reverse scoring |
| Validation | Whole numbers 0 to 4 only |
| Advice | Different for each level |
| Charts | Matplotlib, three panels |
| Tests | Boundary and edge cases |

---

## 07 Roadmap

- [ ] Tkinter or web interface
- [ ] Weekly score history
- [ ] Guided breathing timer
- [ ] Real anonymous class data, with permission

---

## 08 References

Cohen, S., Kamarck, T., Mermelstein, R. (1983). A global measure of perceived stress. *Journal of Health and Social Behavior*, 24, 385-396.

Selye, H. (1956). *The Stress of Life.* McGraw-Hill.

Lazarus, R. S., Folkman, S. (1984). *Stress, Appraisal, and Coping.* Springer.

Group data in the charts is simulated. It does not belong to real people.

---

## 09 Author

**[Your Name]**, Roll No. [Your Roll Number]
B.Tech CSE, SRM Institute of Science and Technology, NCR Campus
Supervisor: Mr. A. Kathiresan

[github.com/DivyangUGitHub](https://github.com/DivyangUGitHub)
