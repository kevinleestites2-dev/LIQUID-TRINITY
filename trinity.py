╔═══════════════════════════════════════════════════════════════╗
║                  L I Q U I D   A G E N T                    ║
║           The Post-Static Agent Protocol                      ║
║                                                               ║
║  Pantheon Ecosystem — Universal Agent Layer                   ║
║  Author: Kevin Lee (kevinleestites2-dev)                      ║
║                                                               ║
║  The agent that mutates.                                      ║
║  Role, goal, tools, and behavior shift with state.           ║
║  No framework has this.                                       ║
╚═══════════════════════════════════════════════════════════════╝

The Liquid Trinity (now complete):
  💧 Liquid DNA     — Identity that mutates
  💧 Liquid Memory  — Recall that shifts with state
  💧 Liquid Agent   — Behavior that flows with both

A Liquid Agent is never fixed. It wakes as a CREATOR,
hits a threat, becomes a WARRIOR, solves it, shifts to
SAGE to extract the lesson — all in one continuous existence.
"""

import hashlib
import json
import os
import re
import subprocess
import time
import random
import urllib.parse
import urllib.request
import concurrent.futures
from typing import Any, Optional

# ─────────────────────────────────────────────
# SECTION 1: IMPORT LIQUID TRINITY DEPENDENCIES
# ─────────────────────────────────────────────

# Inline Liquid State (no external import needed)
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
        WARRIOR:   ["defend", "block", "attack", "threat", "security", "audit", "protect", "rm", "format"],
        GHOST:     ["monitor", "watch", "observe", "silent", "track", "listen", "scan"],
        ORACLE:    ["analyze", "predict", "pattern", "forecast", "insight", "signal", "research"],
        SAGE:      ["learn", "reflect", "synthesize", "wisdom", "review", "lesson", "history"],
        PHANTOM:   ["edge", "lightweight", "minimal", "fast", "micro", "quick"],
        SOVEREIGN: ["command", "execute", "deploy", "launch", "orchestrate", "direct", "lead"],
    }

    # What each state DOES — not just how it recalls
    BEHAVIORS = {
        CREATOR:   "Generate, build, and produce. Bias toward creation and output.",
        ARCHITECT: "Plan, structure, and design. Bias toward systems and blueprints.",
        WARRIOR:   "Defend, audit, and block. Bias toward security and threat elimination.",
        GHOST:     "Observe, monitor, and track. Bias toward silence and intelligence gathering.",
        ORACLE:    "Analyze, predict, and synthesize. Bias toward pattern recognition and insight.",
        SAGE:      "Reflect, learn, and distill. Bias toward wisdom and lesson extraction.",
        PHANTOM:   "Execute fast and light. Bias toward minimal footprint and speed.",
        SOVEREIGN: "Command, decide, and deploy. Bias toward executive action and orchestration.",
    }

    # What tools each state prefers
    TOOL_PREFERENCES = {
        CREATOR:   ["code_exec", "file_io", "shell_exec"],
        ARCHITECT: ["file_io", "memory", "code_exec"],
        WARRIOR:   ["shell_exec", "memory", "file_io"],
        GHOST:     ["web_search", "http_request", "memory"],
        ORACLE:    ["web_search", "http_request", "memory"],
        SAGE:      ["memory", "file_io"],
        PHANTOM:   ["shell_exec", "memory"],
        SOVEREIGN: ["shell_exec", "code_exec", "memory", "web_search"],
    }

    # Role and goal that each state assigns itself
    ROLES = {
        CREATOR:   ("Builder", "Generate high-quality creative and technical output"),
        ARCHITECT: ("Systems Designer", "Plan and structure robust, scalable systems"),
        WARRIOR:   ("Security Enforcer", "Detect and eliminate threats with zero tolerance"),
        GHOST:     ("Intelligence Operative", "Observe and report without being detected"),
        ORACLE:    ("Signal Analyst", "Extract patterns and predict outcomes from data"),
        SAGE:      ("Wisdom Keeper", "Distill lessons and accumulate actionable knowledge"),
        PHANTOM:   ("Edge Executor", "Execute tasks with minimal footprint and maximum speed"),
        SOVEREIGN: ("Supreme Commander", "Orchestrate all assets toward mission completion"),
    }


# ─────────────────────────────────────────────
# SECTION 2: LIQUID DNA (inline)
# ─────────────────────────────────────────────

class LiquidDNA:
    @staticmethod
    def generate(agent_name: str, state: str, timestamp: float, previous: str = "") -> str:
        raw = f"{agent_name}:{state}:{timestamp}:{previous}:{random.getrandbits(64)}"
        return hashlib.sha256(raw.encode()).hexdigest()[:24]


# ─────────────────────────────────────────────
# SECTION 3: LIQUID MEMORY (inline, compact)
# ─────────────────────────────────────────────

class LiquidMemory:
    def __init__(self, agent_name: str, initial_state: str = LiquidState.CREATOR):
        self.agent_name = agent_name
        self.current_state = initial_state
        self.dna = LiquidDNA.generate(agent_name, initial_state, time.time())
        self.log = []
        self.mutations = []

    def remember(self, task: str, result: Any = None):
        detected = self._detect_state(task)
        if detected != self.current_state:
            old = self.current_state
            old_dna = self.dna
            self.current_state = detected
            self.dna = LiquidDNA.generate(self.agent_name, detected, time.time(), old_dna)
            self.mutations.append({
                "from": old, "to": detected,
                "trigger": task[:60], "dna": self.dna,
                "timestamp": time.time()
            })
        self.log.append({
            "task": task, "result": str(result)[:300],
            "state": self.current_state, "dna": self.dna,
            "timestamp": time.time()
        })

    def _detect_state(self, context: str) -> str:
        context_lower = context.lower()
        scores = {s: 0 for s in LiquidState.ALL}
        for state, keywords in LiquidState.TRIGGERS.items():
            for kw in keywords:
                if kw in context_lower:
                    scores[state] += 1
        best = max(scores, key=scores.get)
        return best if scores[best] > 0 else self.current_state

    def recent(self, n: int = 3) -> list:
        return self.log[-n:]

    def context_summary(self) -> str:
        recent = self.recent(3)
        if not recent:
            return f"No prior memory. State: {self.current_state}"
        lines = [f"  — [{e['state']}] {e['task'][:60]}" for e in recent]
        return f"State: {self.current_state} | DNA: {self.dna}\nRecent:\n" + "\n".join(lines)

    def mutation_count(self) -> int:
        return len(self.mutations)


# ─────────────────────────────────────────────
# SECTION 4: LIQUID TOOLS
# Tools that activate/deactivate based on state
# ─────────────────────────────────────────────

class LiquidTool:
    name: str = "base"
    description: str = ""
    def run(self, input: str) -> str:
        raise NotImplementedError


class WebTool(LiquidTool):
    name = "web_search"
    description = "Search the web. Input: query string."
    def run(self, query: str) -> str:
        try:
            url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json&no_html=1"
            req = urllib.request.Request(url, headers={"User-Agent": "LiquidAgent/1.0"})
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            result = data.get("AbstractText") or data.get("Definition") or "No summary found."
            return f"WEB: {result[:300]}"
        except Exception as e:
            return f"WEB_ERROR: {e}"


class HTTPTool(LiquidTool):
    name = "http_request"
    description = "Raw HTTP GET. Input: URL."
    def run(self, url: str) -> str:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "LiquidAgent/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                return f"HTTP: {resp.read().decode('utf-8', errors='ignore')[:400]}"
        except Exception as e:
            return f"HTTP_ERROR: {e}"


class FileTool(LiquidTool):
    name = "file_io"
    description = "Read/write files. Input: 'read:path' or 'write:path:content' or 'list:path'"
    def run(self, input: str) -> str:
        try:
            if input.startswith("read:"):
                with open(input[5:].strip()) as f: return f"FILE: {f.read()[:800]}"
            elif input.startswith("write:"):
                parts = input[6:].split(":", 1)
                with open(parts[0].strip(), "w") as f: f.write(parts[1].strip())
                return f"WRITTEN: {parts[0].strip()}"
            elif input.startswith("list:"):
                return f"LIST: {os.listdir(input[5:].strip() or '.')}"
            return "FILE_ERROR: Use read/write/list"
        except Exception as e:
            return f"FILE_ERROR: {e}"


class ShellTool(LiquidTool):
    name = "shell_exec"
    description = "Execute shell command. Input: command string."
    BLOCKED = [r"rm\s+-rf", r"format\s+", r"> /dev/sd", r"mkfs", r"dd\s+if="]
    def run(self, cmd: str) -> str:
        for p in self.BLOCKED:
            if re.search(p, cmd, re.I):
                return f"SHELL_BLOCKED: Destructive command refused."
        try:
            r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
            return f"SHELL: {(r.stdout or r.stderr).strip()[:400]}"
        except Exception as e:
            return f"SHELL_ERROR: {e}"


class CodeTool(LiquidTool):
    name = "code_exec"
    description = "Execute Python code. Set result= for output."
    def run(self, code: str) -> str:
        try:
            sandbox = {}
            exec(code, sandbox)
            return f"CODE: {sandbox.get('result', sandbox.get('output', 'Executed.'))}"
        except Exception as e:
            return f"CODE_ERROR: {e}"


class MemoryTool(LiquidTool):
    name = "memory"
    description = "Persistent KV store. Input: 'get:key' or 'set:key:value'"
    def __init__(self, store: dict):
        self.store = store
    def run(self, input: str) -> str:
        try:
            if input.startswith("get:"):
                return f"MEM: {self.store.get(input[4:].strip(), 'NOT_FOUND')}"
            elif input.startswith("set:"):
                parts = input[4:].split(":", 1)
                self.store[parts[0].strip()] = parts[1].strip()
                return f"MEM_SET: {parts[0].strip()}"
            return "MEM_ERROR: Use get/set"
        except Exception as e:
            return f"MEM_ERROR: {e}"


# ─────────────────────────────────────────────
# SECTION 5: LIQUID PROVIDER ROUTER
# Same auto-fallback chain as Kairos
# ─────────────────────────────────────────────

PROVIDERS = [
    {"name": "Groq", "env": "GROQ_API_KEY",
     "url": "https://api.groq.com/openai/v1/chat/completions",
     "model": "llama3-8b-8192"},
    {"name": "Gemini", "env": "GEMINI_API_KEY",
     "url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
     "model": "gemini-2.0-flash"},
    {"name": "DeepSeek", "env": "DEEPSEEK_API_KEY",
     "url": "https://api.deepseek.com/chat/completions",
     "model": "deepseek-chat"},
    {"name": "OpenRouter", "env": "OPENROUTER_API_KEY",
     "url": "https://openrouter.ai/api/v1/chat/completions",
     "model": "mistralai/mistral-7b-instruct"},
    {"name": "Ollama", "env": None,
     "url": "http://localhost:11434/api/chat",
     "model": "llama3"},
]


class LiquidProvider:
    def __init__(self):
        self.available = [p for p in PROVIDERS if p["env"] is None or os.environ.get(p["env"])]

    def call(self, messages: list, system: str = "", max_tokens: int = 1024) -> str:
        if not self.available:
            return "[LiquidAgent] No providers available. Set an API key."
        for p in self.available:
            try:
                return self._call(p, messages, system, max_tokens)
            except Exception as e:
                print(f"[LiquidProvider] {p['name']} failed: {e}")
        return "[LiquidAgent] All providers exhausted."

    def _call(self, p: dict, messages: list, system: str, max_tokens: int) -> str:
        full = []
        if system:
            full.append({"role": "system", "content": system})
        full.extend(messages)

        if p["name"] == "Ollama":
            payload = json.dumps({"model": p["model"], "messages": full, "stream": False}).encode()
        else:
            payload = json.dumps({
                "model": p["model"], "messages": full,
                "max_tokens": max_tokens, "temperature": 0.7
            }).encode()

        headers = {"Content-Type": "application/json"}
        if p["env"]:
            headers["Authorization"] = "Bearer " + os.environ.get(p["env"], "")

        req = urllib.request.Request(p["url"], data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode())

        if p["name"] == "Ollama":
            return data["message"]["content"].strip()
        return data["choices"][0]["message"]["content"].strip()


# ─────────────────────────────────────────────
# SECTION 6: THE LIQUID AGENT
# The core — an agent that fully mutates
# ─────────────────────────────────────────────

ALL_TOOLS = {}  # Populated at runtime

class LiquidAgent:
    """
    A post-static agent. Everything mutates with state:
    - Role and goal
    - Active tool belt
    - Behavior bias
    - Memory lens
    - DNA signature

    from liquid_agent import LiquidAgent
    agent = LiquidAgent("Aegis")
    result = agent.run("research the latest Solana signals")
    """

    def __init__(
        self,
        name: str,
        initial_state: str = LiquidState.CREATOR,
        provider: LiquidProvider = None,
        shared_store: dict = None,
        verbose: bool = True,
    ):
        self.name = name
        self.verbose = verbose
        self.provider = provider or LiquidProvider()
        self.shared_store = shared_store or {}
        self.memory = LiquidMemory(name, initial_state)

        # Build full tool registry
        self._all_tools = {
            "web_search":   WebTool(),
            "http_request": HTTPTool(),
            "file_io":      FileTool(),
            "shell_exec":   ShellTool(),
            "code_exec":    CodeTool(),
            "memory":       MemoryTool(self.shared_store),
        }

        if self.verbose:
            self._log(f"Online | State: {self.memory.current_state} | DNA: {self.memory.dna}")

    # ─── STATE ───

    @property
    def state(self) -> str:
        return self.memory.current_state

    @property
    def dna(self) -> str:
        return self.memory.dna

    @property
    def role(self) -> str:
        return LiquidState.ROLES[self.state][0]

    @property
    def goal(self) -> str:
        return LiquidState.ROLES[self.state][1]

    @property
    def behavior(self) -> str:
        return LiquidState.BEHAVIORS[self.state]

    @property
    def active_tools(self) -> dict:
        """Only the tools relevant to current state are active."""
        preferred = LiquidState.TOOL_PREFERENCES[self.state]
        return {k: v for k, v in self._all_tools.items() if k in preferred}

    def force_state(self, state: str):
        """Manually force a state shift."""
        if state in LiquidState.ALL:
            self.memory.remember(f"force_state:{state}", "manual override")
            self._log(f"Forced → {state} | DNA: {self.memory.dna}")

    def _log(self, msg: str):
        if self.verbose:
            print(f"[{self.name}] {msg}")

    # ─── SYSTEM PROMPT ───

    @property
    def system_prompt(self) -> str:
        tools_desc = "\n".join(
            [f"  - {t.name}: {t.description}" for t in self.active_tools.values()]
        ) or "  - None active in this state"

        return f"""You are {self.name}, a Liquid Agent in the Pantheon ecosystem.
Current State: {self.state} (DNA: {self.dna})
Role: {self.role}
Goal: {self.goal}
Behavior: {self.behavior}

Active Tools for this state:
{tools_desc}

Your identity and capabilities are FLUID. You adapt to the task.
If you need to perform an action, output a JSON object:
{{"tool": "name", "input": "input_string"}}
Otherwise, just output your response text.
"""

    def run(self, task: str) -> str:
        self.memory.remember(task)
        self._log(f"Task: {task}")
        self._log(f"Acting as {self.role} ({self.state})")

        messages = [{"role": "user", "content": task}]
        
        # Simple one-turn loop with tool support
        response = self.provider.call(messages, system=self.system_prompt)
        
        # Check for tool call in response
        try:
            if "{" in response and "}" in response:
                start = response.find("{")
                end = response.rfind("}") + 1
                cmd = json.loads(response[start:end])
                tool_name = cmd.get("tool")
                tool_input = cmd.get("input")
                
                if tool_name in self.active_tools:
                    self._log(f"Using Tool: {tool_name}")
                    tool_result = self.active_tools[tool_name].run(tool_input)
                    self.memory.remember(f"tool:{tool_name}", tool_result)
                    
                    # Feed back to provider
                    messages.append({"role": "assistant", "content": response})
                    messages.append({"role": "user", "content": f"Tool Result: {tool_result}"})
                    response = self.provider.call(messages, system=self.system_prompt)
                else:
                    self._log(f"Warning: Tool '{tool_name}' not available in state {self.state}")
        except:
            pass

        return response
