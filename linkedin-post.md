# LinkedIn Post — Part 1

## Heading
I gave Claude Code my AWS keys. Then I built a jail for it.

## Subheading
An open-source sandbox that separates AI agents from your credentials — so they can operate infrastructure without owning it.

---

Letting agents run autonomously is the future. One that books a flight when the price drops. Deploys your hotfix at 3 AM. Troubleshoots a production issue on AWS using CLI access while you sleep. All possible with today's agents.

But you can't give control to something you can't trust.

I wanted Claude Code to operate my infrastructure — aws, kubectl, terraform, git. Not just write code, but actually run it. But I couldn't. The moment you go from "edit this file" to "deploy this to production," you're handing an AI your credentials and hoping it doesn't hallucinate a destructive command.

Claude Code asks before running commands — but those are application-level prompts, not a security boundary. Say yes (or run in auto mode), and it executes as your user with full access to every credential on your machine. OpenAI's Codex CLI ships with network-disabled sandboxing — but that only stops exfiltration, not the agent running terraform destroy with your keys. Neither solves the real problem: the agent has your credentials and can use them however it wants.

And these are the agents where you at least have visibility. You can see every command, every reasoning step. But you can't watch ten agents running overnight. The problem is worse with third-party agents that run autonomously — you don't see what they do, you just see the result.

Right now, the only options are: give it everything and hope, or give it nothing and do the work yourself.

So I built Agent Lockbox — the agent runs in a sandbox with zero credentials, and every command it wants to execute goes through an external authorization layer. The agent asks. Something else decides. Based on rules you define.

Solutions like this already exist — but I wanted to build one from scratch to understand what it actually takes to sandbox an AI agent. Consider this an experiment. I learned more from the things that broke than from the things that worked.

GitHub: https://github.com/shkrwnd/agent-lockbox

Part 2 — the design choices, what broke, and what I learned building it.

#AI #CloudSecurity #DevSecOps #ClaudeCode #OpenSource #Docker #AgentSecurity
