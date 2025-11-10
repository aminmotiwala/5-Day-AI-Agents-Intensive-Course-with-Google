from __future__ import annotations

from typing import Optional

from google.adk.plugins.base_plugin import BasePlugin
from google.adk.agents.base_agent import BaseAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types


class BeforeEditorLogPlugin(BasePlugin):
    def __init__(self) -> None:
        super().__init__(name="before_editor_log")

    async def before_agent_callback(
        self, *, agent: BaseAgent, callback_context: CallbackContext
    ) -> Optional[types.Content]:
        if agent.name == "EditorAgent":
            draft = callback_context.state.get("blog_draft", "")
            print("\n=== Before running EditorAgent ===")
            print("Draft to edit:")
            print(draft if isinstance(draft, str) else str(draft))
            print("=== End draft ===\n")
        return None

