import uuid

from services.workflow_store import pending_workflows


def approval_node(state):

    workflow_id = str(uuid.uuid4())

    pending_workflows[workflow_id] = state

    return {
        "approval_status": "PENDING_APPROVAL",
        "workflow_id": workflow_id
    }