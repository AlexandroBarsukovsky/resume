from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import importlib

router = APIRouter()

class AgentRunRequest(BaseModel):
    params: Dict[str, Any] = {}

@router.post("/run/{agent_name}")
async def run_agent(agent_name: str, request: AgentRunRequest):
    try:
        module_path = f"app.agents.{agent_name}"
        module = importlib.import_module(module_path)
        if hasattr(module, "run"):
            result = module.run(request.params)
            return {"status": "ok", "result": result}
        else:
            raise HTTPException(400, f"Agent {agent_name} has no run() method")
    except ImportError:
        raise HTTPException(404, f"Agent {agent_name} not found")

@router.get("/status")
async def list_agents():
    agents = [
        "level1.intent_monitor", "level1.account_scorer", "level1.usage_analyzer",
        "level1.competitor_intelligence", "level1.news_monitor",
        "level2.conservative_strategist", "level2.balanced_strategist",
        "level2.aggressive_strategist", "level2.risk_manager", "level2.marketing_analyst",
        "level3.segment_coordinators", "level3.archivist", "level3.supervisor", "level3.resource_planner",
        "level4.task_creator", "level4.forecast_updater", "level4.report_generator", "level4.notification_sender"
    ]
    return {"agents": agents}