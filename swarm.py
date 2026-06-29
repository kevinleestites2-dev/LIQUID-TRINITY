"""
╔═══════════════════════════════════════════════════════════════╗
║                  L I Q U I D   S W A R M                    ║
║           The Sovereign Collective Intelligence               ║
║                                                               ║
║  Pantheon Ecosystem — Swarm Layer                             ║
║  Author: Kevin Lee (kevinleestites2-dev)                      ║
║                                                               ║
║  A swarm that thinks as one.                                  ║
║  Agents that mutate independently.                            ║
║  A hive mind that evolves with every cycle.                   ║
╚═══════════════════════════════════════════════════════════════╝
"""

import hashlib
import json
import os
import re
import time
import random
import urllib.parse
import urllib.request
import concurrent.futures
import threading
from typing import Any, Optional

# ─────────────────────────────────────────────
# SECTION 1: LIQUID FOUNDATIONS (inline)
# ─────────────────────────────────────────────

class LiquidState:
    CREATOR   = "CREATOR"
    ARCHITECT = "ARCHITECT"
    WARRIOR   = "WARRIOR"
    GHOST     = "GHOST"
    ORACLE    = "ORACLE"
    SAGE      = "SAGE"
    PHANTOM   = "PHANTOM"
    SOVEREIGN = "SOVEREIGN"

    ALL = [CREATOR, ARCHITECT, WARRIOR, GHOST, ORACLE, SAGE, PHANTOM, SOVEREIGN]

    TRIGGERS = {
        CREATOR:   ["build", "create", "generate", "make", "design", "write", "code"],
        ARCHITECT: ["plan", "structure", "architect", "organize", "map", "blueprint"],
        WARRIOR:   ["defend", "block", "attack", "threat", "security", "audit", "protect"],
        GHOST:     ["monitor", "watch", "observe", "silent", "track", "listen", "scan"],
        ORACLE:    ["analyze", "predict", "pattern", "forecast", "insight", "signal", "research"],
        SAGE:      ["learn", "reflect", "synthesize", "wisdom", "review", "lesson", "history"],
        PHANTOM:   ["edge", "lightweight", "minimal", "fast", "micro", "quick"],
        SOVEREIGN: ["command", "execute", "deploy", "launch", "orchestrate", "direct", "lead"],
    }

    ROLES = {
        CREATOR:   ("Builder", "Generate creative and technical output"),
        ARCHITECT: ("Systems Designer", "Plan and structure robust systems"),
        WARRIOR:   ("Security Enforcer", "Detect and eliminate threats"),
        GHOST:     ("Intelligence Operative", "Observe without being detected"),
        ORACLE:    ("Signal Analyst", "Extract patterns and predict outcomes"),
        SAGE:      ("Wisdom Keeper", "Distill lessons and accumulate knowledge"),
        PHANTOM:   ("Edge Executor", "Execute with minimal footprint"),
        SOVEREIGN: ("Supreme Commander", "Orchestrate all assets to mission"),
    }

    BEHAVIORS = {
        CREATOR:   "Bias toward creation and output.",
        ARCHITECT: "Bias toward systems and blueprints.",
        WARRIOR:   "Bias toward security and threat elimination.",
        GHOST:     "Bias toward silence and intelligence gathering.",
        ORACLE:    "Bias toward pattern recognition and insight.",
        SAGE:      "Bias toward wisdom and lesson extraction.",
        PHANTOM:   "Bias toward minimal footprint and speed.",
        SOVEREIGN: "Bias toward executive action and orchestration.",
    }

    # Auto-specialization weights for task analysis
    SPECIALIZATION_ORDER = [
        SOVEREIGN, WARRIOR, ORACLE, ARCHITECT,
        CREATOR, GHOST, SAGE, PHANTOM
    ]

    @staticmethod
    def detect(context: str, current: str = CREATOR) -> str:
        context_lower = context.lower()
        scores = {s: 0 for s in LiquidState.ALL}
        for state, keywords in LiquidState.TRIGGERS.items():
            for kw in keywords:
                if kw in context_lower:
                    scores[state] += 1
        best = max(scores, key=scores.get)
        return best if scores[best] > 0 else current

    @staticmethod
    def assign_roles(n: int, task: str) -> list:
        """Auto-assign states to n agents based on task analysis."""
        primary = LiquidState.detect(task)
        roles = [primary]
        for state in LiquidState.SPECIALIZATION_ORDER:
            if state != primary and len(roles) < n:
                roles.append(state)
        while len(roles) < n:
            roles.append(LiquidState.CREATOR)
        return roles[:n]


class LiquidDNA:
    @staticmethod
    def generate(name: str, state: str, ts: float, prev: str = "") -> str:
        raw = f"{name}:{state}:{ts}:{prev}:{random.getrandbits(64)}"
        return hashlib.sha256(raw.encode()).hexdigest()[:24]

    @staticmethod
    def combine(dna_list: list) -> str:
        """Combine multiple DNA signatures into a collective swarm DNA."""
        combined = ":".join(sorted(dna_list))
        return hashlib.sha256(combined.encode()).hexdigest()[:24]


# ─────────────────────────────────────────────
# SECTION 2: HIVE MIND
# Shared memory that propagates across all agents
# ─────────────────────────────────────────────

class HiveMind:
    """
    Shared intelligence layer for the swarm.
    Discoveries made by any agent instantly
    propagate to all others.
    """

    def __init__(self, swarm_name: str):
        self.swarm_name = swarm_name
        self.signals = []          # All discoveries
        self.knowledge = {}        # Key insights keyed by topic
        self.threat_log = []       # Security events
        self.consensus = []        # Convergence votes
        self._lock = threading.Lock()
        self.pulse_count = 0       # How many cycles the swarm has run

    def broadcast(self, agent_name: str, state: str, signal: str, metadata: dict = None):
        """Agent broadcasts a discovery to the entire hive."""
        with self._lock:
            entry = {
                "agent": agent_name,
                "state": state,
                "signal": signal,
                "timestamp": time.time(),
                "meta": metadata or {},
            }
            self.signals.append(entry)

            # Auto-classify into threat log
            if state == LiquidState.WARRIOR or "BLOCK" in signal or "threat" in signal.lower():
                self.threat_log.append(entry)

            print(f"[HiveMind] {agent_name}({state}) >> {signal[:80]}")

    def learn(self, topic: str, insight: str, agent: str):
        """Store a key insight under a topic for swarm-wide access."""
        with self._lock:
            if topic not in self.knowledge:
                self.knowledge[topic] = []
            self.knowledge[topic].append({
                "insight": insight,
                "agent": agent,
                "timestamp": time.time()
            })

    def query(self, topic: str) -> list:
        """Any agent can query the hive's knowledge on a topic."""
        with self._lock:
            return self.knowledge.get(topic, [])

    def vote(self, agent_name: str, result: str):
        """Submit a result for convergence voting."""
        with self._lock:
            self.consensus.append({"agent": agent_name, "result": result})

    def converge(self) -> str:
        """
        Convergence Protocol:
        Synthesize all agent votes into one unified output.
        """
        with self._lock:
            if not self.consensus:
                return "No consensus reached."
            if len(self.consensus) == 1:
                return self.consensus[0]["result"]

            parts = [f"[{v['agent']}]: {v['result'][:150]}" for v in self.consensus]
            return "CONVERGED OUTPUT:\n" + "\n".join(parts)

    def recent_signals(self, n: int = 5) -> list:
        with self._lock:
            return self.signals[-n:]

    def pulse(self):
        """Increment swarm pulse — one full execution cycle."""
        with self._lock:
            self.pulse_count += 1
            self.consensus = []  # Reset consensus after each pulse

    def status(self) -> dict:
        with self._lock:
            return {
                "signals": len(self.signals),
                "knowledge_topics": list(self.knowledge.keys()),
                "threats_detected": len(self.threat_log),
                "pulse_count": self.pulse_count,
            }


# ─────────────────────────────────────────────
# SECTION 3: SWARM AGENT
# A Liquid Agent wired to the Hive Mind
# ─────────────────────────────────────────────

class SwarmAgent:
    def __init__(
        self,
        name: str,
        initial_state: str = LiquidState.CREATOR,
        hive: HiveMind = None,
        provider=None,
        verbose: bool = True,
    ):
        self.name = name
        self.state = initial_state
        self.hive = hive
        self.provider = provider
        self.verbose = verbose
        self.dna = LiquidDNA.generate(name, initial_state, time.time())
        self.history = []
        self.mutations = 0

    def _mutate(self, task: str):
        detected = LiquidState.detect(task, self.state)
        if detected != self.state:
            old = self.state
            self.state = detected
            self.dna = LiquidDNA.generate(self.name, detected, time.time(), self.dna)
            self.mutations += 1
            if self.verbose:
                print(f"  [{self.name}] MUTATED {old} → {detected} | DNA: {self.dna}")

    def _system_prompt(self) -> str:
        role, goal = LiquidState.ROLES[self.state]
        behavior = LiquidState.BEHAVIORS[self.state]
        hive_signals = ""
        if self.hive:
            recent = self.hive.recent_signals(3)
            if recent:
                hive_signals = "\nHive Intel:\n" + "\n".join(
                    [f"  [{s['agent']}]: {s['signal'][:60]}" for s in recent]
                )
        return f"""You are {self.name}, a SwarmAgent in the Liquid Swarm.
State: {self.state} | Role: {role} | DNA: {self.dna}
Goal: {goal} | Behavior: {behavior}
{hive_signals}
Broadcast discoveries to the hive."""

    def run(self, task: str) -> str:
        self._mutate(task)
        if self.provider:
            response = self.provider.call([{"role": "user", "content": task}], system=self._system_prompt())
        else:
            response = f"[{self.name}:{self.state}] Task processed."
        
        if self.hive:
            self.hive.broadcast(self.name, self.state, response[:200])
            self.hive.vote(self.name, response)
        return response


# ─────────────────────────────────────────────
# SECTION 4: LIQUID SWARM
# The sovereign collective
# ─────────────────────────────────────────────

class LiquidSwarm:
    def __init__(self, name: str = "LiquidSwarm", max_agents: int = 12, verbose: bool = True):
        self.name = name
        self.max_agents = max_agents
        self.verbose = verbose
        self.hive = HiveMind(name)
        self.agents: list[SwarmAgent] = []
        self.swarm_dna = LiquidDNA.generate(name, "SWARM", time.time())
        self.provider = self._init_provider()

    def _init_provider(self):
        class Provider:
            def call(self, messages, system="", max_tokens=1024):
                api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GROQ_API_KEY")
                if not api_key: return "No API Key"
                # Simplified call logic
                return "Swarm processed result."
        return Provider()

    def spawn(self, n: int, task: str = ""):
        """Dynamic Spawning with Auto-Specialization."""
        count = min(n, self.max_agents)
        states = LiquidState.assign_roles(count, task)
        self.agents = []
        for i in range(count):
            agent_name = f"{self.name}-Agent-{i+1}"
            self.agents.append(SwarmAgent(agent_name, states[i], self.hive, self.provider, self.verbose))
        print(f"[Swarm] Spawned {count} agents with specialized roles.")

    def execute(self, task: str) -> str:
        """Parallel execution with hive-mind convergence."""
        if not self.agents: self.spawn(3, task)
        self.hive.pulse()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.agents)) as executor:
            futures = {executor.submit(agent.run, task): agent for agent in self.agents}
            concurrent.futures.wait(futures)
            
        # Convergence Protocol
        result = self.hive.converge()
        
        # Swarm DNA Mutation
        agent_dnas = [a.dna for a in self.agents]
        self.swarm_dna = LiquidDNA.combine(agent_dnas + [self.swarm_dna])
        
        print(f"[Swarm] Cycle Complete. New Swarm DNA: {self.swarm_dna}")
        return result
