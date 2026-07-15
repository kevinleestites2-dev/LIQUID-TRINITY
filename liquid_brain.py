#!/usr/bin/env python3
"""
LIQUID BRAIN — The Reasoning & Strategy Core of the Liquid Trinity
Integrates Deep-meta chain-of-thought into the DNA → Memory → Agent pipeline.
Part of LIQUID-TRINITY | Heisted Launch: July 15, 12:00 PM EDT
"""
import hashlib, json, time
from datetime import datetime, timezone

class LiquidBrain:
    """
    The cognitive layer that sits above Liquid DNA, Memory, and Agent.
    Translates raw intents into reasoned strategies with chain-of-thought.
    """

    # ─── 8-STATE COGNITIVE MODES ───
    MODES = {
        "CREATOR":   {"focus": "generation",  "temperature": 0.9, "context_window": "wide"},
        "ARCHITECT": {"focus": "structure",   "temperature": 0.4, "context_window": "focused"},
        "WARRIOR":   {"focus": "execution",   "temperature": 0.3, "context_window": "tight"},
        "GHOST":     {"focus": "stealth",     "temperature": 0.2, "context_window": "minimal"},
        "ORACLE":    {"focus": "prediction",  "temperature": 0.7, "context_window": "deep"},
        "SAGE":      {"focus": "reflection",  "temperature": 0.5, "context_window": "full"},
        "PHANTOM":   {"focus": "simulation",  "temperature": 0.8, "context_window": "parallel"},
        "SOVEREIGN": {"focus": "command",     "temperature": 0.1, "context_window": "omniscient"},
    }

    # ─── REASONING FRAMEWORKS (SAFLA-ALIGNED) ───
    FRAMEWORKS = ["OODA", "PDCA", "MARS", "OUROBOROS", "CYCLIC", "SELF_REF"]

    def __init__(self, mode="SOVEREIGN"):
        self.mode = mode.upper()
        self._verify_mode()
        self.thought_log = []
        self.strategy_stack = []
        self.chain_id = self._new_chain_id()

    def _verify_mode(self):
        if self.mode not in self.MODES:
            raise ValueError(f"Unknown mode: {self.mode}. Valid: {list(self.MODES.keys())}")

    def _new_chain_id(self):
        """Generate a unique chain-of-thought identifier."""
        raw = f"{self.mode}:{time.time_ns()}:{hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]}"
        return hashlib.sha256(raw.encode()).hexdigest()[:16]

    def _timestamp(self):
        return datetime.now(timezone.utc).strftime("%H:%M:%S UTC")

    # ─── CORE REASONING ───

    def reason(self, intent, context=None, framework="OODA"):
        """
        Process an intent through a reasoning framework.
        Returns a structured strategy with chain-of-thought.
        """
        chain_id = self._new_chain_id()
        framework = framework.upper()
        if framework not in self.FRAMEWORKS:
            framework = "OODA"

        mode_config = self.MODES[self.mode]

        thought = {
            "chain_id": chain_id,
            "mode": self.mode,
            "framework": framework,
            "intent": intent,
            "context": context or {},
            "temperature": mode_config["temperature"],
            "timestamp": self._timestamp(),
            "reasoning_steps": self._apply_framework(framework, intent, context),
            "conclusion": None,
            "confidence": None,
        }

        self.thought_log.append(thought)
        return thought

    def _apply_framework(self, framework, intent, context):
        """Apply a reasoning framework to decompose the intent."""
        steps = []
        context = context or {}

        if framework == "OODA":
            steps.append(("OBSERVE", f"Scanning environment for: {intent}"))
            steps.append(("ORIENT", f"Mapping context: {json.dumps(context)[:100]}..."))
            steps.append(("DECIDE", f"Selecting strategy under {self.mode} mode"))
            steps.append(("ACT", f"Executing with temperature {self.MODES[self.mode]['temperature']}"))

        elif framework == "PDCA":
            steps.append(("PLAN", f"Planning approach for: {intent}"))
            steps.append(("DO", f"Running execution under {self.mode} focus"))
            steps.append(("CHECK", f"Validating against context"))
            steps.append(("ACT", f"Adjusting based on {self.mode} mode"))

        elif framework == "MARS":
            steps.append(("MEMORY", f"Recalling relevant state"))
            steps.append(("ACTOR", f"Initializing action sequence"))
            steps.append(("REFLECTOR", f"Evaluating progress"))
            steps.append(("STRATEGIST", f"Updating approach"))

        elif framework == "OUROBOROS":
            steps.append(("INPUT", f"Ingesting intent: {intent}"))
            steps.append(("PROCESS", f"Running recursive analysis"))
            steps.append(("OUTPUT", f"Generating response"))
            steps.append(("FEEDBACK", f"Looping back for refinement"))

        elif framework == "CYCLIC":
            steps.append(("INIT", f"Cyclic initialization"))
            steps.append(("EXECUTE", f"Running cycle"))
            steps.append(("FEEDBACK", f"Collecting results"))
            steps.append(("RECURSE", f"Looping with updated state"))

        elif framework == "SELF_REF":
            steps.append(("SELF", f"Introspecting on: {intent}"))
            steps.append(("REFERENCE", f"Cross-referencing memory"))
            steps.append(("REFLECT", f"Evaluating self-consistency"))
            steps.append(("RESOLVE", f"Finalizing with {self.mode} authority"))

        return steps

    def conclude(self, thought, confidence=0.85):
        """Finalize a thought with a conclusion and confidence score."""
        thought["conclusion"] = f"Resolved under {self.mode} mode via {thought['framework']}"
        thought["confidence"] = min(1.0, max(0.0, confidence))
        return thought

    def mutate(self, new_mode):
        """Shift cognitive mode for the next reasoning cycle."""
        old_mode = self.mode
        self.mode = new_mode.upper()
        self._verify_mode()
        mutation = {
            "from": old_mode,
            "to": self.mode,
            "chain_id": self._new_chain_id(),
            "timestamp": self._timestamp(),
        }
        self.strategy_stack.append(mutation)
        return mutation

    # ─── CHAIN-OF-THOUGHT EXPORT ───

    def export_chain(self):
        """Export the full thought log as a portable JSON structure."""
        return {
            "brain_id": self.chain_id,
            "active_mode": self.mode,
            "thought_count": len(self.thought_log),
            "mutation_count": len(self.strategy_stack),
            "thoughts": self.thought_log[-10:],  # last 10 for context
            "mutations": self.strategy_stack,
            "exported_at": self._timestamp(),
        }

    def summarize(self):
        """Short status string for logging."""
        return (
            f"[LIQUID BRAIN] Mode: {self.mode} | "
            f"Thoughts: {len(self.thought_log)} | "
            f"Mutations: {len(self.strategy_stack)} | "
            f"Chain: {self.chain_id}"
        )

    # ─── HEISTED-SPECIFIC STRATEGY ───

    def heisted_strategy(self, pool_data=None):
        """
        Generate a pre-launch strategy for the Heisted airdrop using
        the SOVEREIGN mode.
        """
        self.mutate("SOVEREIGN")
        thought = self.reason(
            intent="Heisted airdrop launch preparation",
            context={
                "deadline": "July 15, 12:00 PM EDT",
                "pool_data": pool_data or {},
                "available_frameworks": self.FRAMEWORKS,
            },
            framework="OODA"
        )
        return self.conclude(thought, confidence=0.92)


# ─── QUICK TEST ───
if __name__ == "__main__":
    brain = LiquidBrain(mode="SOVEREIGN")
    print(brain.summarize())

    # Run a reasoning cycle
    result = brain.heisted_strategy()
    print(f"\nStrategy Chain: {result['chain_id']}")
    print(f"Framework: {result['framework']}")
    print(f"Confidence: {result['confidence']}")
    for step_type, step_desc in result['reasoning_steps']:
        print(f"  [{step_type:10s}] {step_desc}")

    # Mutate to WARRIOR
    brain.mutate("WARRIOR")
    print(f"\n{brain.summarize()}")