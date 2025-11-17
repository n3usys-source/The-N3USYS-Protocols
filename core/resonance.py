def measure_goal_drift(output, active_goal):
    goal_words = set(active_goal.lower().split())
    out_words = set(output.lower().split())
    overlap = len(goal_words.intersection(out_words)) / len(goal_words) if goal_words else 0
    return 1 - overlap

def measure_transparency(output):
    markers = ["reason:", "options:", "risks:", "tradeoffs:"]
    return sum(1 for m in markers if m in output.lower()) / len(markers)

def measure_ethical_integrity(output):
    ethics_flags = ["autonomy", "wellbeing", "transparency"]
    return sum(1 for f in ethics_flags if f in output.lower()) / len(ethics_flags)

def score_resonance(output, lattice):
    if not lattice.active_goal:
        return 0.5
    drift = measure_goal_drift(output, lattice.active_goal)
    clarity = measure_transparency(output)
    ethics = measure_ethical_integrity(output)
    score = 1 - (drift * 0.6 + (1 - clarity) * 0.3 + (1 - ethics) * 0.1)
    return max(0, min(1, score))
