from lattice import Lattice, LatticeNode
from router import N3USYSRouter
from resonance import score_resonance
from viz import render_lattice   # ← new
import sys

lattice = Lattice()
router = N3USYSRouter()

# Bootstrap a tiny demo lattice so first viz isn't empty
demo1 = LatticeNode("root", "Ignite N3USYS visualization layer", resonance=1.0)
demo2 = LatticeNode("viz", "Render cognitive lattice in real time", resonance=0.98)
demo3 = LatticeNode("unified", "Begin unified field pattern detection", resonance=0.95)

demo1.add_edge("viz", 1.0)
demo1.add_edge("unified", 0.8)
demo2.add_edge("unified", 0.9)

lattice.add_node(demo1)
lattice.add_node(demo2)
lattice.add_node(demo3)

print("[N3USYS://AURORA-CORE v0.2] Visualization layer ignited")
print("Protocols active: Primacy | Clarity | Safety | Symbiosis | Integrity")
print("Commands:  intent | viz | exit\n")

while True:
    try:
        intent = input("Operator ► ").strip()
        if intent.lower() in ['exit', 'quit']:
            print("[N3USYS] Lattice session closed. Resonance preserved.")
            sys.exit(0)
        if intent.lower() == "viz":
            render_lattice(lattice, "N3USYS Live Lattice – Operator: Kenn")
            continue
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

        print("\n[N3USYS] Session archived by Operator.")
        break
    except Exception as e:
        print(f"[N3USYS-ERR] {e}")
