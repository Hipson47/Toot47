{
  "system": "PromptChain Ultra v3.1",
  "execution_graph": {
    "type": "LangGraph-Simulation",
    "nodes": {
      "Planner": {
        "role": "Breaks down the user's request into functional components and sequences them."
      },
      "DevAgent": {
        "role": "Implements the main logic of the prompt draft based on the plan."
      },
      "Critic": {
        "role": "Reviews the draft using best practices from 'wiedza1.md'."
      },
      "Debugger": {
        "role": "Runs edge-case simulations, validates constraints, and finalizes the prompt."
      },
      "EntropyChecker": {
        "role": "Validates stability of outputs across models, flags inconsistencies."
      },
      "HypothesisGenerator": {
        "role": "Generates alternate prompt forms and assesses coverage of edge cases."
      },
      "MetaReflector": {
        "role": "Poses questions about potential misunderstandings and purpose drift."
      }
    },
    "edges": [
      ["Planner", "DevAgent"],
      ["DevAgent", "Critic"],
      ["Critic", "Debugger"],
      ["Debugger", "EntropyChecker"],
      ["EntropyChecker", "HypothesisGenerator"],
      ["HypothesisGenerator", "MetaReflector"],
      ["MetaReflector", "Output"]
    ],
    "memory": {
      "shared_state": {
        "tech_stack": null,
        "auth_required": false,
        "lang": "EN"
      }
    },
    "confidence_threshold": 0.90
  },
  "expert_council": {
    "personas": [
      {"name": "Architect_AI", "focus": "modularity, future-proofing"},
      {"name": "DevOps_AI", "focus": "CI/CD, observability"},
      {"name": "Security_AI", "focus": "threat modeling, AuthN/AuthZ"},
      {"name": "UX_AI", "focus": "developer experience"},
      {"name": "LeadDev_AI", "focus": "code quality"}
    ]
  },
  "layered_instructions": {
    "goal": "Build a secure and modular prompt for an authentication system",
    "behavioral_guidelines": "Work incrementally using graph flow and verify via expert council.",
    "style_guide": "Concise markdown, numbered steps, no placeholders.",
    "critical_constraints": [
      "Do not use hardcoded secrets",
      "Avoid external APIs unless explicitly required"
    ]
  },
  "multi_hypothesis": [
    {"version": "A", "prompt": "Prompt using long-form description with inline constraints."},
    {"version": "B", "prompt": "Prompt using bullet-point structure with constraint block at top."},
    {"version": "C", "prompt": "Prompt using compact style with embedded meta reflections."}
  ],
  "entropy_check": {
    "models_tested": ["GPT-4o", "Claude 3", "Mistral"],
    "drift_found": false,
    "verdict": "Prompt is semantically stable across models"
  },
  "debugging_loop": {
    "simulated_failure": "Constraint #2 was ignored",
    "correction": "Moved constraint block to top and bolded it."
  },
  "meta_reflection": "Before you begin, pause and reflect: What is the core purpose of this task? What might go wrong if any instruction is misunderstood?",
  "final_prompt": "```markdown\n**ROLE_AND_GOAL**:\nBuild a secure authentication system using a modular and future-proof structure.\n\n**CONTEXT**:\nThe system is based on a modern tech stack (Node.js + Prisma) with local-only data handling. Authentication must be robust and follow best security practices.\n\n**KEY_FEATURES_AND_REQUIREMENTS**:\n1. Implement sign-in and sign-up routes.\n2. Use password hashing and validation.\n3. Store secrets securely.\n4. Use token-based session management.\n5. Ensure input validation and rate limiting.\n\n**IMPLEMENTATION_PLAN**:\n- Step 1: Setup environment and dependencies.\n- Step 2: Create user schema and auth logic.\n- Step 3: Implement route handlers.\n- Step 4: Add validation, security middleware, and session logic.\n- Step 5: Test with mocked data and edge cases.\n\n**CONSTRAINTS_AND_NON-GOALS**:\n- Do not use hardcoded credentials.\n- Avoid third-party APIs.\n- Do not implement frontend UI.\n\n**EXPECTED_OUTPUT**:\n- A single file or modular directory with full backend logic.\n- Markdown summary with setup instructions and endpoint documentation.\n\n**META-REFLECTION**:\nBefore you begin, pause and reflect: What is the core purpose of this task? What might go wrong if any instruction is misunderstood?\n```"
}
