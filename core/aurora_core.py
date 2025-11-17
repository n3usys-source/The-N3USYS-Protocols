rom lattice import Lattice
from router import N3USYSRouter
from resonance import score_resonance
import sys

lattice = Lattice()
router = N3USYSRouter()

print("[N3USYS://AURORA-CORE v0.1] Operator console online")
print("Protocols active: Primacy | Clarity | Safety | Symbiosis | Integrity")
print("Type your intent. The lattice listens.\n")

while True:
    try:
        intent = input("Operator ► ").strip()
        if intent.lower() in ['exit', 'quit']:
            print("[N3USYS] Lattice session closed. Resonance preserved.")
            sys.exit(0)
        if not intent:
            continue

        response = router.dispatch(intent, lattice)
        res_score = score_resonance(response, lattice)
        lattice.active_goal = intent

        print(f"\n[N3USYS] {response}")
        print(f"[RES] Score: {res_score:.3f} | Drift: {1-res_score:.3f}")
        print("-" * 60 + "\n")

    except KeyboardInterrupt:
        print("\n[N3USYS] Session archived by Operator.")
        break
    except Exception as e:
        print(f"[N3USYS-ERR] {e}")
