"""
Student Stress Analyzer & Coping Advisor
Mini Project - Unit 4: Stress and Coping Strategies
Based on the Perceived Stress Scale (PSS-10, Cohen et al., 1983)
"""
import random
import statistics
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- DATA
QUESTIONS = [
    "Been upset because of something that happened unexpectedly?",
    "Felt unable to control the important things in your life?",
    "Felt nervous and stressed?",
    "Felt confident about your ability to handle personal problems?",   # reverse
    "Felt that things were going your way?",                             # reverse
    "Found that you could not cope with all the things you had to do?",
    "Been able to control irritations in your life?",                    # reverse
    "Felt that you were on top of things?",                              # reverse
    "Been angered because of things outside your control?",
    "Felt difficulties were piling up so high you could not overcome them?",
]
REVERSE_ITEMS = {3, 4, 6, 7}   # zero-based index of Q4, Q5, Q7, Q8
SCALE = "0=Never 1=Almost never 2=Sometimes 3=Fairly often 4=Very often"

CATEGORIES = [(13, "Low Stress"), (26, "Moderate Stress"), (40, "High Stress")]

ADVICE = {
    "Low Stress": [
        "Keep your routine: sleep 7-8 hours and exercise regularly.",
        "Practise gratitude journaling to maintain optimism.",
        "Use free time for hobbies and social activities.",
    ],
    "Moderate Stress": [
        "Use time management: make a daily to-do list with priorities.",
        "Practise deep breathing or progressive muscle relaxation daily.",
        "Talk to a friend, mentor or family member about your worries.",
        "Take short breaks (5 min every 45 min of study).",
    ],
    "High Stress": [
        "Meet a college counsellor or doctor - seeking help is a strength.",
        "Practise meditation / yoga for 15-20 minutes every day.",
        "Break big tasks into small steps; avoid multitasking.",
        "Limit caffeine and screen time; protect your sleep.",
        "Build a support network and avoid isolating yourself.",
    ],
}

# ------------------------------------------------------------- FUNCTIONS
def score_pss(answers):
    """Total PSS-10 score. Reverse items use (4 - x)."""
    if len(answers) != 10 or any(a not in range(5) for a in answers):
        raise ValueError("Need 10 answers, each between 0 and 4")
    return sum(4 - a if i in REVERSE_ITEMS else a for i, a in enumerate(answers))

def categorize(score):
    for limit, name in CATEGORIES:
        if score <= limit:
            return name

def stress_index(score):
    """Stress Index (%) = score / 40 * 100"""
    return round(score / 40 * 100, 1)

def gas_stage(score):
    """Map score to Selye's General Adaptation Syndrome stage (simplified)."""
    if score <= 13:
        return "Normal / Alarm (short-term, manageable)"
    if score <= 26:
        return "Resistance (body is coping but under strain)"
    return "Exhaustion risk (prolonged stress)"

def class_statistics(scores):
    mean = statistics.mean(scores)
    sd = statistics.stdev(scores)
    return {"n": len(scores), "mean": round(mean, 2), "sd": round(sd, 2),
            "median": statistics.median(scores), "min": min(scores), "max": max(scores)}

def simulate_students(n=40, seed=7):
    """Simulated dataset (NOT real people) to demonstrate group analysis."""
    random.seed(seed)
    return [max(0, min(40, round(random.gauss(19, 7)))) for _ in range(n)]

# ------------------------------------------------------------- INTERFACE
def ask_questions():
    print("\n" + SCALE)
    answers = []
    for i, q in enumerate(QUESTIONS, 1):
        while True:
            try:
                a = int(input(f"Q{i}. In the last month, how often have you {q[0].lower()+q[1:]} "))
                if a in range(5):
                    answers.append(a); break
            except ValueError:
                pass
            print("  Please enter a number from 0 to 4.")
    return answers

def print_report(name, answers):
    s = score_pss(answers)
    cat = categorize(s)
    print("\n" + "=" * 56)
    print(f" STRESS REPORT FOR: {name}")
    print("=" * 56)
    print(f" PSS-10 Score   : {s} / 40")
    print(f" Stress Index   : {stress_index(s)} %")
    print(f" Category       : {cat}")
    print(f" GAS Stage      : {gas_stage(s)}")
    print(" Recommended coping strategies:")
    for tip in ADVICE[cat]:
        print("   -", tip)
    print("=" * 56)
    return s, cat

def make_dashboard(student_score, scores, filename="dashboard.png"):
    colors = {"Low Stress": "#4caf7d", "Moderate Stress": "#f2b134", "High Stress": "#e4572e"}
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.6))

    # 1. Gauge-style bar for the student
    cat = categorize(student_score)
    ax[0].barh(["Low", "Moderate", "High"], [13, 13, 14], left=[0, 14, 27],
               color=[colors["Low Stress"], colors["Moderate Stress"], colors["High Stress"]], alpha=.45)
    ax[0].axvline(student_score, color="black", lw=3)
    ax[0].set_xlim(0, 40); ax[0].set_xlabel("PSS-10 score")
    ax[0].set_title(f"Your score: {student_score}/40 ({cat})", fontsize=11)

    # 2. Histogram of group
    ax[1].hist(scores, bins=range(0, 42, 4), color="#4a7fc1", edgecolor="white")
    ax[1].axvline(statistics.mean(scores), color="red", ls="--", label="Mean")
    ax[1].axvline(student_score, color="black", label="You")
    ax[1].set_xlabel("PSS-10 score"); ax[1].set_ylabel("Students")
    ax[1].set_title("Class score distribution (simulated)"); ax[1].legend()

    # 3. Pie of categories
    counts = [sum(1 for x in scores if categorize(x) == c) for c in colors]
    ax[2].pie(counts, labels=colors.keys(), autopct="%1.0f%%", colors=colors.values(), startangle=90)
    ax[2].set_title("Stress category share")

    fig.suptitle("Student Stress Analyzer - Dashboard", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()

def main():
    print("STUDENT STRESS ANALYZER & COPING ADVISOR")
    name = input("Enter your name: ")
    answers = ask_questions()
    s, _ = print_report(name, answers)
    group = simulate_students()
    print("\nClass statistics (simulated):", class_statistics(group))
    make_dashboard(s, group)
    print("Dashboard saved as dashboard.png")

if __name__ == "__main__":
    main()
